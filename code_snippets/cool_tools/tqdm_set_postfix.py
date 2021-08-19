from time import sleep

from tqdm import tqdm

fruits = tqdm(["apple", "orange", "grape"])
for fruit in fruits:
    sleep(0.3)
    fruits.set_description(f"Picking {fruit}")
