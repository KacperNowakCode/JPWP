import argparse
import time
import random
import asyncio
from decorators import measure_time, measure_memory
from loader import FunctionLoader
from plotter import plot_results, export_results

async def run_async(func, data):
    return await func(data)


def profile_function(func, data):
    start = time.time()
    res = func(data) if data is not None else func()
    return (time.time() - start) * 1000


def main():
    parser = argparse.ArgumentParser(description='Extended Function Profiler')
    parser.add_argument('file', help='Python module with functions')
    parser.add_argument('--config', help='Path to JSON config file')
    parser.add_argument('--plot', action='store_true', help='Display bar plot')
    parser.add_argument('--csv', help='Export results to CSV file')
    parser.add_argument('--html', help='Export results to HTML file')
    args = parser.parse_args()

    funcs = FunctionLoader.load_functions_from_file(args.file)
    tests = []
    if args.config:
        tests = FunctionLoader.load_tests_from_config(args.config)

    results = {}
    for name, func in funcs.items():
        data = None
        for t in tests:
            if t.get('function') == name:
                size = t.get('size', 1000)
                data = random.sample(range(10000), size)
        if asyncio.iscoroutinefunction(func):
            elapsed = asyncio.run(run_async(func, data))
        else:
            elapsed = profile_function(func, data)
        results[name] = elapsed
        print(f"{name}: {elapsed:.2f} ms")

    if args.plot:
        plot_results(results)
    export_results(results, args.csv, args.html)

if __name__=='__main__':
    main()