# Python and Data Science Code Snippets
Source code of Python and data science snippets posted daily at [Data Science Simplified](https://mathdatasimplified.com/). You can receive these daily tips in your mailbox for free by [subscribing to the website](https://mathdatasimplified.com/).

You can also get extra examples and practice questions for each tip by [being my offical Patron](https://www.patreon.com/khuyentran)
# Contents
* [Python Built-in Methods](#python)
* [Pandas](#pandas)
* [Numpy](#numpy)
* [Data Science Tools](#data-science-tools)
* [Terminal](#terminal)
* [Cool Tools](#cool-tools)
* [Jupyter Notebook](#jupyter-notebook)


<h1 id='python'> Python Built-in Methods <img src="images/python.png"> </h1>

### Number

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Get Multiples of a Number Using Modulus | [link](https://mathdatasimplified.com/2021/04/22/get-multiples-of-a-numbers-using-modulus/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/multiples_of_a_number.py)
 | fractions: Get Numerical Results in Fractions instead of Decimals | [link](https://mathdatasimplified.com/2021/02/27/fractions-get-numerical-results-in-fractions-instead-of-decimals/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/fractions_example.py)
| How to Use Underscores to Format Large Numbers in Python | [link](https://mathdatasimplified.com/2021/01/12/how-to-use-underscores-to-format-large-numbers-in-python/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/underscore_large_number.py)
 | Confirm whether a variable is a number | [link](https://mathdatasimplified.com/2020/11/23/confirm-whether-a-variable-is-a-number/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/check_if_number.py)

### Boolean

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Boolean Operators: Connect Two Boolean Expressions into One Expression | [link](https://mathdatasimplified.com/2021/05/15/boolean-operators-connect-two-boolean-expressions-into-one-expression/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/boolean_operators.py)

### String

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| `__str__` and `__repr__`: Create a String Representation of a Python Object | [link](https://mathdatasimplified.com/2021/05/11/__str__-and-__repr__-create-a-string-representation-of-a-python-bbject/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/__str__and__repr.py)
| String find: Find the Index of a Substring in a Python String | [link](https://mathdatasimplified.com/2021/05/01/string-find-find-the-index-of-a-substring-in-a-python-string/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/string_find.py)
| eval: Turn a Python String into a Variable or Function | [link](https://mathdatasimplified.com/2021/03/13/eval-turn-a-python-string-into-a-variable-or-function/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/eval_example.py)
| re.sub: Replace One String with Another String Using Regular Expression | [link](https://mathdatasimplified.com/2021/03/07/re-sub-replace-one-string-with-another-string-using-regular-expression/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/re_sub_example.py)

### List 

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| any: Check if Any Element of an Iterable is True | [link](https://mathdatasimplified.com/2021/06/01/any-check-if-any-element-of-an-iterable-is-true/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/any_example.py)
| Extended Iterable Unpacking: Ignore Multiple Values when Unpacking a Python Iterable | [link](https://mathdatasimplified.com/2021/05/03/extended-iterable-unpacking-ignore-multiple-values-when-unpacking-a-python-iterable/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/extended_iterable_unpacking.py)
| How to Unpack Iterables in Python | [link](https://mathdatasimplified.com/2021/04/07/how-to-unpack-iterables-in-python/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/unpack_iterables.py)
| random.choice: Get a Randomly Selected Element from a Python List | [link](https://mathdatasimplified.com/2021/02/28/random-choice-get-a-randomly-selected-element-from-a-python-list/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/random_choice.py)
| filter: Get the Elements of an Iterable that a Function Returns True | [link](https://mathdatasimplified.com/2021/06/11/filter-get-the-elements-of-an-iterable-that-a-function-returns-true/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/filter_example.py)
| heapq: Find n Max Values of a Python List | [link](https://mathdatasimplified.com/2021/03/28/heapq-find-n-max-values-of-a-python-list/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/heapq_example.py)
| join method: Turn an Iterable into a Python String | [link](https://mathdatasimplified.com/2021/06/17/join-method-turn-an-iterable-to-a-python-string/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/join_list.py)
| Zip: Associate Elements from Two Iterators based on the Order | [link](https://mathdatasimplified.com/2021/02/05/zip-associate-elements-from-two-iterators-based-on-the-order/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/zip_example.py)
| collections.Counter: Count the Occurrences of Items in a List |[link](https://mathdatasimplified.com/2021/02/02/collections-counter-count-the-occurrences-of-items-in-a-list/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/collections_counter.py)
| Zip Function: Create Pairs of Elements from Two Lists in Python | [link](https://mathdatasimplified.com/2021/01/11/zip-function-create-pairs-of-elements-from-two-lists-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/zip_function.py)
| Stop using = operator to create a copy of a Python list. Use copy method instead | [link](https://mathdatasimplified.com/2021/01/09/stop-using-operator-to-create-a-copy-of-a-python-list-use-copy-method-instead/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/copy_method.py) 
| itertools.combinations: A better way to iterate through a pair of values in a Python list | [link](https://mathdatasimplified.com/2020/12/12/itertools-combinations-a-better-way-to-iterate-through-a-pair-of-values-in-a-python-list/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/itertools_combinations_example.py)
 | Enumerate | [link](https://mathdatasimplified.com/2020/11/23/enumerate/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/enumerate_example.py)

### Tuple

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
 | namedtuple: A Lightweight Python Structure to Mange your Data | [link](https://mathdatasimplified.com/2021/02/22/namedtuple-a-lightweight-python-structure-to-mange-your-data/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/namedtuple_example.py)
  | slice: Make your Indices more Readable by Naming your Slice | [link](https://mathdatasimplified.com/2021/02/16/slice-make-your-indices-more-readable-by-naming-your-slice/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/slice_example.py)

### Dictionary

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Defaultdict: Return a default value when a key is not available | [link](https://mathdatasimplified.com/2020/12/09/how-to-return-a-default-value-when-a-key-is-not-in-python-dictionary/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/collections_defaultdict.py)
| Ordered dictionary in Python | [link](https://mathdatasimplified.com/2020/11/23/ordered-dictionary-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/collections_ordereddict.py)

### Datetime

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| datetime + timedelta: Calculate End DateTime based on Start DateTime and Duration | [link](https://mathdatasimplified.com/2021/03/04/datetime-timedelta-calculate-end-datetime-based-on-start-datetime-and-duration/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/datetime_timedelta.py)
 | Use Dates in a Month as the Feature | [link](https://mathdatasimplified.com/2020/11/23/use-dates-in-a-month-as-the-feature/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/dates_in_month_as_feature.py)

### Function

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| *iterator: Pass Values of an Iterator to a Function | [link](https://mathdatasimplified.com/2021/05/05/iterator-pass-values-of-an-iterator-to-a-function/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/args_example.py)
| Use Python Built-in Functions to Speed your Code | [link](https://mathdatasimplified.com/2021/01/29/use-python-built-in-functions-to-speed-your-code/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/built_in_functions_speed.py)
| **kwargs: Pass multiple arguments to a function in Python |[link](https://mathdatasimplified.com/2020/12/26/kwargs-pass-multiple-arguments-to-a-function-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/kwargs.py)
| Return Multiple Values from a Function Using Python Dictionary | [link](https://mathdatasimplified.com/2020/12/11/return-multiple-values-from-a-function-using-python-dictionary/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/return_multiple_values_with_dictionary.py)
| Decorator in Python| [link](https://mathdatasimplified.com/2020/11/25/decorator-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/decorator_example.py)

### Classes

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Abstract Classes: Declare Methods without Implementation | [link](https://mathdatasimplified.com/2021/06/08/abstract-classes-declare-methods-without-implementation/)  | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/abc_example.py) |
| classmethod: What is it and When to Use it | [link](https://mathdatasimplified.com/2021/04/24/classmethod-what-is-it-and-when-to-use-it/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/classmethod_example.py)
 | getattr: a Better Way to Get the Attribute of a Class | [link](https://mathdatasimplified.com/2021/02/23/getattr-a-better-way-to-get-the-attribute-of-a-class/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/getattr_example.py)
 | `__call__`: You can Call your Class Instance like a Function. Here is how | [link](https://mathdatasimplified.com/2021/01/22/__call__-you-can-call-your-class-instance-like-a-function-here-is-how/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/__call__example.py)
 | Static method: use the function without adding the attributes required for a new instance | [link](https://mathdatasimplified.com/2020/11/23/static-method-use-the-function-without-adding-the-attributes-required-for-a-new-instance/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/staticmethod_example.py)

### Files

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Shutil: Move Files in Python | [link](https://mathdatasimplified.com/2021/06/03/shutil-move-files-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/move_files/move_files.py)
| pathlith.Path | [link](https://mathdatasimplified.com/2020/11/23/pathlith-path/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/pathlib_path)
| pathlib: Create, Write, and Rename Files in One Line of Code | [link](https://mathdatasimplified.com/2021/02/14/pathlib-create-write-and-rename-files-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/pathlib_write)
| Pathlib: Iterate Over All Files that End with ‘.csv’ in a Directory | [link](https://mathdatasimplified.com/2020/12/31/pathlib-iterate-over-all-files-that-end-with-csv-in-a-directory/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/pathlib_iterate_files_end_with)
| How to Improve the Readability of your JSON file using Indent| [link](https://mathdatasimplified.com/2021/04/27/how-to-improve-the-readability-of-your-json-file-using-indent/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/improve_json_readability.py)
| `__main__.py`: Run a Directory like a Main Script | [link](https://mathdatasimplified.com/2021/03/15/__main__-py-run-a-directory-like-a-main-script/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/main_example)

### Error handling

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Assert in Python: Output a Customized Message When the Assertion Fails | [link](https://mathdatasimplified.com/2021/04/13/assert-in-python-output-a-customized-message-when-the-assertion-fails/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/assert_customize_message.py)
| warnings: Ignore Warnings when Running Python Code | [link](https://mathdatasimplified.com/2021/03/11/warnings-ignore-warnings-when-running-python-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/warnings_example.py)

### Interact with Terminal

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| How to Execute Shell Commands in a Python Script | [link](https://mathdatasimplified.com/2021/04/10/how-to-execute-shell-commands-in-a-python-script/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/os_system.py)
| argparse: Python Library to Parse Arguments from Command Line | [link](https://mathdatasimplified.com/2020/12/23/argparse-python-library-to-parse-arguments-from-command-line/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/argparse_example.py)

### Best Practices

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Stop Writing Code Comments. Use Meaningful Names Instead | [link](https://mathdatasimplified.com/2021/01/14/stop-writing-code-comments-use-meaningful-names-instead/) 
| Underscore(_): Ignore values that will not be used | [link](https://mathdatasimplified.com/2020/12/25/underscore_-ignore-values-that-will-not-be-used/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/ignore_variables.py)
| Underscore “_”: Ignore the index in Python for loops | [link](https://mathdatasimplified.com/2020/12/20/underscore-_-ignore-the-index-in-python-for-loops/)|  [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/underscore_for_loop.py)
| Save Immediate Output when an Error Occurs | [link](https://mathdatasimplified.com/2020/12/10/save-immediate-output-when-an-error-occurs/)
| Print error without stopping the for loop in Python | [link](https://mathdatasimplified.com/2020/12/06/print-error-without-stopping-the-for-loop-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/print_error.py)
| Python Pass Statement | [link](https://mathdatasimplified.com/2020/12/02/python-pass-statement/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/pass_statement.py)
 | Type hint in Python 3.9 | [link](https://mathdatasimplified.com/2020/11/23/type-hint-in-python-3-9/)

### Code Speed
 
 | Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
 | Concurrently execute tasks on separate CPUs | [link](https://mathdatasimplified.com/2020/11/23/concurrently-execute-tasks-on-separate-cpus/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/multiprocessing_example.py)
 | Compare the execution time between 2 functions |[link](https://mathdatasimplified.com/2020/11/23/compare-the-execution-time-between-2-functions/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/compare_execution_time.py)


<h1 id='pandas'> Pandas <img src="images/panda.png"> </h1>

### Change Values

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| pd.DataFrame.agg: Aggregate over Columns or Rows Using Multiple Operations | [link](https://mathdatasimplified.com/2021/05/09/pd-dataframe-agg-aggregate-over-columns-or-rows-using-multiple-operations/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pd_dataframe_agg.py)
| DataFrame.pipe: Increase the Readability of your Code when Applying Multiple Functions to a DataFrame | [link](https://mathdatasimplified.com/2021/04/20/dataframe-pipe-increase-the-readability-of-your-code-when-applying-multiple-functions-to-a-dataframe/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/dataframe_pipe.py)
| pd.Series.map: Change Values of a Pandas Series Using a Dictionary | [link](https://mathdatasimplified.com/2021/05/21/pd-series-map-change-values-of-a-pandas-series-using-a-dictionary/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/any_example.py)
| pd.Series.str: Manipulate Text Data in a pandas Series | [link](https://mathdatasimplified.com/2021/04/03/pd-series-str-manipulate-text-data-in-a-pandas-series/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pd_series_str.py)
| set_categories in pandas: Sort Categorical Column by a Specific Ordering | [link](https://mathdatasimplified.com/2021/02/09/set_categories-in-pandas-how-to-sort-categorical-column-by-a-specific-ordering/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/set_categories.py)
| parse_dates: Convert Columns into Datetime When Using Pandas to Read CSV Files | [link](https://mathdatasimplified.com/2021/01/02/parse_dates-convert-columns-into-datetime-when-using-pandas-to-read-csv-files/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/parse_dates.py)
| Filter Rows only if Column Contains Values from another List | [link](https://mathdatasimplified.com/2020/12/19/filter-rows-only-if-column-contains-values-from-another-list/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/s.is_in.py)
| Specify suffixes when using df.merge() | [link](https://mathdatasimplified.com/2020/12/01/specify-suffixes-when-using-df-merge/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/df_merge.py)
| Specify the datatype to speed up your code and reduce memory | [link](https://mathdatasimplified.com/2020/11/23/specify-the-datatype-to-speed-up-your-code-and-reduce-memory/)
| Highlight your pandas DataFrame | [link](https://mathdatasimplified.com/2020/11/23/highlight-your-pandas-dataframe/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/highlight_pandas.ipynb)
| Assign Values to Multiple New Columns | [link](https://mathdatasimplified.com/2020/11/23/assign-values-to-multiple-new-columns/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/df_assign.py)
| Reduce pd.DataFrame’s Memory | [link](https://mathdatasimplified.com/2020/11/23/reduce-pd-dataframes-memory/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/reduce_memory.py)

### Get Values

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| df.columns.str.startswith: Find DataFrame’s Columns that Start with a Pattern | [link](https://mathdatasimplified.com/2021/05/27/df-columns-str-startswith-find-dataframes-columns-that-start-with-a-pattern/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/df_columns_str_start_with.py)
| pandas.DataFrame.iterrows: Iterate over Rows of a DataFrame | [link](https://mathdatasimplified.com/2021/06/15/pandas-dataframe-iterrows-iterate-over-rows-of-a-dataframe/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pd_dataframe_iterrows.py)
| pandas.Series.dt: Access Datetime Properties of pandas Series | [link](https://mathdatasimplified.com/2021/05/13/pandas-series-dt-access-datetime-properties-of-pandas-series/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pd_series_dt.py)
| pd.Series.between: Select Rows in a pandas Series Containing Values between 2 Numbers | [link](https://mathdatasimplified.com/2021/03/03/pd-series-between-obtain-the-rows-with-values-lie-between-2-numbers/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pd_series_between.py)
| DataFrame rolling: Find the average of the previous n datapoints using Pandas | [link](https://mathdatasimplified.com/2021/01/31/dataframe-rolling-find-the-average-of-the-previous-n-datapoints-using-pandas/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/df_rolling.py)
| select_dtypes: Return a subset of a DataFrame including/excluding columns based on their dtype | [link](https://mathdatasimplified.com/2021/01/26/select_dtypes-return-a-subset-of-a-dataframe-including-excluding-columns-based-on-their-dtype/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/select_dtypes.py)
| pct_change: Find the percentage change between the current and a prior element in a pandas Series | [link](https://mathdatasimplified.com/2021/01/19/pct_change-find-the-percentage-change-between-the-current-and-a-prior-element-in-a-pandas-series/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/pct_change.py)
| DataFrame.diff and DataFrame.shift: Take the Difference between Rows within a Column in Pandas | [link](https://mathdatasimplified.com/2021/01/07/dataframe-diff-and-dataframe-shift-take-the-difference-between-rows-within-a-column-in-pandas/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/df_diff.py)
| Pandas DataFrame: How to select all columns that start with a word | [link](https://mathdatasimplified.com/2020/11/27/pandas-dataframe-how-to-select-all-columns-that-start-with-a-word/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/select_columns_start_with.py)
| Exclude Outliers | [link](https://mathdatasimplified.com/2020/11/23/exclude-outliers/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/exclude_outliers.py)
| Pandas DataFrame Get Data in a Year Range | [link](https://mathdatasimplified.com/2020/11/23/pandas-dataframe-get-data-in-a-year-range/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/get_data_in_year_range.py)

### Testing

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| assert_frame equal: Test whether Two DataFrames are Similar | [link](https://mathdatasimplified.com/2021/04/15/assert_frame-equal-test-whether-two-dataframes-are-similar/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/pandas/assert_frame_equal.py)



<h1 id='numpy'> Numpy <img src="images/numpy.png"> </h1>

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| np.ravel: Flatten a Numpy Array | [link](https://mathdatasimplified.com/2021/05/18/np-ravel-flatten-a-numpy-array/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/numpy/np_ravel.py)
| Use List to Change the Positions of Rows or Columns in a Numpy Array | [link](https://mathdatasimplified.com/2021/05/07/use-list-to-change-the-positions-of-rows-or-columns-in-a-numpy-array/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/numpy/use_list_to_change_position_of_arrays.py)
| Key Parameter in Max(): Find the Key with the Largest Value | [link](https://mathdatasimplified.com/2021/02/19/key-parameter-in-max-find-the-key-with-the-largest-value/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/key_in_max.py)
| Difference between Numpy’s All and Any Methods | [link](https://mathdatasimplified.com/2021/03/31/difference-between-numpys-all-and-any-methods/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/numpy/any_all.py)
| Double np.argsort: Get Rank of Values in an Array | [link](https://mathdatasimplified.com/2021/01/03/double-np-argsort-get-rank-of-values-in-an-array/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/numpy/double_np_argsort.py)
| Get the index of the max value in a Numpy array | [link](https://mathdatasimplified.com/2020/12/15/get-the-index-of-the-max-value-in-a-numpy-array/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/numpy/np_argmax.py)
| np.all: Test Whether All Elements along a Given Axis of a NumPy Array Evaluate to True | [link](https://mathdatasimplified.com/2021/06/22/np-all-test-whether-all-elements-along-a-given-axis-of-a-numpy-array-evaluate-to-true/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/blob/master/code_snippets/numpy/np_array_all.py)
| array-to-latex: Turn a Numpy Array into Latex | [link](https://mathdatasimplified.com/2021/06/23/array_to_latex-turn-a-numpy-array-into-latex/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/blob/master/code_snippets/numpy/array_to_latex_example.ipynb)


<h1 id='data-science-tools'> Data Science Tools <img src="images/data-science.png"> </h1>

### Testing

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| snoop : Smart Print to Debug your Python Function | [link](https://mathdatasimplified.com/2021/05/28/snoop-smart-print-to-debug-your-python-function/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/snoop_example.py)
| pytest benchmark: A Pytest Fixture to Benchmark your Code | [link](https://mathdatasimplified.com/2021/05/19/pytest-benchmark-a-pytest-fixture-to-benchmark-your-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pytest_benchmark.py)
| pytest.mark.parametrize: Test your Functions with Multiple Inputs | [link](https://mathdatasimplified.com/2021/06/09/pytest-mark-parametrize-test-your-functions-with-multiple-inputs/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pytest_parametrize.py)
| Pytest: Shows only Failed Tests | [link](https://mathdatasimplified.com/2021/01/27/pytest-shows-only-failed-tests/) 
| Pytest Fixtures: Use the same data for different tests | [link](https://mathdatasimplified.com/2020/12/05/pytest-fixtures-use-the-same-data-for-different-tests/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pytest_fixture.py)
|Pytest repeat | [link](https://mathdatasimplified.com/2020/11/23/pytest-repeat/)|[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pytest_repeat.py)
| Pandera: a Python Library to Validate Your Pandas DataFrame | [link](https://mathdatasimplified.com/2021/01/17/pandera-a-python-library-to-validate-your-pandas-dataframe/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pandera_example.py)

### Data

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| faker: Create Fake Data in One Line of Code |[link](https://mathdatasimplified.com/2021/05/14/faker-create-fake-data-in-one-line-of-code/)|[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/faker_example.py)
| DVC: A Data Version Control Tool for your Data Science Projects | [link](https://mathdatasimplified.com/2021/05/06/dvc-a-data-version-control-tool-for-your-data-science-projects/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/dvc_example.sh)
| fetch_openml: Get OpenML’s Dataset in One Line of Code | [link](https://mathdatasimplified.com/2021/04/23/fetch_openml-get-openmls-dataset-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/fetch_openml_example.py)
| github-to-sqlite: Download the Data of your Starred GitHub Repositories in One Command Line | [link](https://mathdatasimplified.com/2021/03/30/github-to-sqlite-download-the-data-of-your-starred-github-repositories-in-one-command-line/)
| Autoscraper | [link](https://mathdatasimplified.com/2020/11/23/autoscraper/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/autoscraper_example.py)
| Extract series data from various Internet sources directly into a pandas DataFrame | [link](https://mathdatasimplified.com/2020/11/23/extract-series-data-from-various-internet-sources-directly-into-a-pandas-dataframe/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/extract_various_data.py)
| Compare the similar features between 2 different datasets | [link](https://mathdatasimplified.com/2020/11/23/compare-the-similar-features-between-2-different-datasets/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/compare_2_datasets)

### Feature extraction

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| datefinder: Automatically Find Dates and Time in a Python String | [link](https://mathdatasimplified.com/2021/05/08/datefinder-automatically-find-dates-and-time-in-a-python-string/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/datefinder_example.py)
| dill’s getname: Get Names a Python Object | [link](https://mathdatasimplified.com/2021/04/29/dills-getname-get-names-a-python-object/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/getname_example.py)
| pytrend: Get the Trend of a Keyword on Google Search Over Time | [link](https://mathdatasimplified.com/2021/04/12/pytrend-get-the-trend-of-a-keyword-on-google-search-over-time/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pytrends_example.ipynb)
| add_datepart: Add Relevant DateTime Features in One Line of Code | [link](https://mathdatasimplified.com/2021/02/11/add_datepart-add-relevant-datetime-features-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/add_datepart_example.py)
| Geopy: Extract Location Based on Python String | [link](https://mathdatasimplified.com/2020/12/08/geopy-extract-location-based-on-python-string/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/geopy_example.py)
| Maya: Convert the string to datetime automatically | [link](https://mathdatasimplified.com/2020/11/23/maya-convert-the-string-to-datetime-automatically/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/maya_example.py)
| Select the features by their relevance | [link](https://mathdatasimplified.com/2020/11/23/select-the-features-by-their-relevance/) 
| Extract holiday from date column | [link](https://mathdatasimplified.com/2020/11/23/extract-holiday-from-date-column/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/extract_holidays.py)

### Visualization

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| D-Tale: A Python Library to Visualize and Analyze your Data Without Code | [link](https://mathdatasimplified.com/2021/05/16/d-tale-a-python-library-to-visualize-and-analyze-your-data-without-code/)
| Graphviz: Create a Flowchart to Capture your Ideas in Python | [link](https://mathdatasimplified.com/2021/02/06/graphviz-create-a-flowchart-to-capture-your-ideas-in-python/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/environment_variables)
| Create an interactive map in Python | [link](https://mathdatasimplified.com/2020/12/03/create-an-interactive-map-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/folium_example.ipynb)

### Sharing and Downloading

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Datapane: Publish your Python Objects on the Web in 2 Lines of Code | [link](https://mathdatasimplified.com/2021/04/25/datapane-publish-your-python-objects-on-the-web-in-2-lines-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/datapane_example.py)
| gdown: Download a File from Google Drive in Python | [link](https://mathdatasimplified.com/2021/01/04/gdown-download-a-file-from-google-drive-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/gdown_example.py)

### Natural Language Processing

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| TextBlob: Processing Text in One Line of Code | [link](https://mathdatasimplified.com/2021/04/16/textblob-processing-text-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/textblob_example.py)
| sumy: Summarize Text in One Line of Code | [link](https://mathdatasimplified.com/2021/03/10/sumy-summarize-text-in-one-line-of-code/)
| Spacy_streamlit: Create a Web App to Visualize your Text in 3 Lines of Code | [link](https://mathdatasimplified.com/2020/12/29/spacy_streamlit-create-a-web-app-to-visualize-your-text-in-3-lines-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/streamlit_app.py)
| Extract a contiguous sequence of 2 words | [link](https://mathdatasimplified.com/2020/11/23/extract-a-contiguous-sequence-of-2-words/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/spacy_ngram.py)
| Detect the “almost similar” articles | [link](https://mathdatasimplified.com/2020/11/23/detect-the-almost-similar-articles/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/difflib_example.py)
| Convert number to words | [link](https://mathdatasimplified.com/2020/11/23/convert-number-to-words/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/convert_number_to_words.py)

### Tools for Best Python Practices

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Don’t Hard-Code. Use Hydra Instead | [link](https://mathdatasimplified.com/2021/04/08/dont-hard-code-use-hydra-instead/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/hydra_example)
| python-dotenv: How to Load the Secret Information from .env File | [link](https://mathdatasimplified.com/2021/02/20/python-dotenv-how-to-load-the-secret-information-from-env-file/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/dotenv_example)
| kedro pipeline: Create Pipeline for your Data Science Projects in Python | [link](https://mathdatasimplified.com/2021/02/03/kedro-pipeline-create-pipeline-for-your-data-science-projects-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/kedro_example.py)
| docopt: Create Beautiful Command-line Interfaces for Documentation in Python | [link](https://mathdatasimplified.com/2021/03/18/docopt-create-beautiful-command-line-interfaces-for-documentation-in-python/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/docopt_example.py)

### Speed Up Code

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| fastai’s df_shrink: Shrink DataFrame’s Memory Usage in One Line of Code | [link](https://mathdatasimplified.com/2021/02/24/fastais-df_shrink-shrink-dataframes-memory-usage-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/fastai_df_shrink.py)
| Swifter: Add One Word to Make your Pandas Apply 23 Times Faster | [link](https://mathdatasimplified.com/2021/01/13/swifter-add-one-word-to-make-your-pandas-apply-23-times-faster/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/swifter_example.py)

### Better Pandas

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:| 
| rich-dataframe: Create Animated and Colorful Pandas Dataframe | [link](https://mathdatasimplified.com/2021/02/17/rich-dataframe-create-animated-and-colorful-pandas-dataframe/) 
| tqdm: Add Progress Bar to your Pandas Apply | [link](https://mathdatasimplified.com/2020/12/30/tqdm-add-progress-bar-to-your-pandas-apply/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/tqdm_example.py)

### Machine Learning

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:| 
| causalimpact: Find Causal Relation of an Event and a Variable in Python | [link](https://mathdatasimplified.com/2021/01/25/causalimpact-find-causal-relation-of-an-event-and-a-variable-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/causalimpact_example.ipynb)
| Pipeline + GridSearchCV: Prevent Data Leakage when Scaling the Data | [link](https://mathdatasimplified.com/2020/12/27/pipeline-gridsearchcv-prevent-data-leakage-when-scaling-the-data/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/pipeline_gridsearchcv.py)
| Decompose high dimensional data into two or three dimensions | [link](https://mathdatasimplified.com/2020/11/23/decompose-high-dimensional-data-into-two-or-three-dimensions/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/data_science_tools/decompose_high_dementional_data.ipynb)
| Cross Validation with Time Series | [link](https://mathdatasimplified.com/2020/11/23/cross-validation-with-time-series/)

<h1 id='terminal'> Terminal <img src="images/command-window.png"> </h1>

### Text

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| tr Command: Translate Characters to Improve Readability In Unix/Linux | [link](https://mathdatasimplified.com/2021/04/05/tr-command-translate-characters-to-improve-readability-in-unix-linux/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/tr_command.sh)
| Sed Command: Replace a string with another string on the command line | [link](https://mathdatasimplified.com/2020/12/17/sed-command-replace-a-string-with-another-string-on-the-command-line/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/sed_command)

### Files

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| fd: a Simple Tool to Search for Files or Directories Fast | [link](https://mathdatasimplified.com/2021/04/09/fd-a-simple-tool-to-search-for-files-or-directories-fast/)
| ln -s: Create Symbolic Link Between 2 Files | [link](https://mathdatasimplified.com/2021/04/11/ln-s-create-symbolic-link-between-2-files/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/create_symbolic_link.sh)
| tee: Save Command Output to a File | [link](https://mathdatasimplified.com/2021/03/06/tee-save-command-output-to-a-file/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/tee_example.sh)
| Make Important Files Impossible to be Deleted | [link](https://mathdatasimplified.com/2021/01/15/make-important-files-impossible-to-be-deleted/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/make_file_immutable.sh)
| View tree structure of your file | [link](https://mathdatasimplified.com/2020/11/23/view-tree-structure-of-your-file/)

### Tracking

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| timeit on the Command Line: Measure Execution Time of Small Code Snippets | [link](https://mathdatasimplified.com/2021/05/25/timeit-on-the-command-line-measure-execution-time-of-small-code-snippets/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/timeit_command_line.sh)
| Time Command: Track the Time it Takes to Execute a File in Linux | [link](https://mathdatasimplified.com/2021/01/24/time-command-track-the-time-it-takes-to-execute-a-file-in-linux/)
| htop | [link](https://mathdatasimplified.com/2020/11/23/htop/)

### Python 

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Python Shell as an Calculator: Grab the Last Output Using “_” | [link](https://mathdatasimplified.com/2021/03/16/python-shell-as-an-calculator-grab-the-last-output-using-_/)
| Find version of a Python library using pip list and grep | [link](https://mathdatasimplified.com/2020/12/04/find-version-of-a-python-library-using-pip-list-and-grep/)
| Conda rollback to the last revision | [link](https://mathdatasimplified.com/2020/11/23/conda-rollback-to-the-last-revision/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/conda_rollback.sh)
| How to Check Whether a Library is Installed | [link](https://mathdatasimplified.com/2020/11/23/1006/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/check_if_library_is_installed.sh)

### Prettify Terminal

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| colorls: Beautify your ls Command with Color and Icons | [link](https://mathdatasimplified.com/2021/04/18/colorls-beautify-your-ls-command-with-color-and-icons/)
| Colorama: Produce a colored terminal text in Python | [link](https://mathdatasimplified.com/2020/12/13/colorama-produce-a-colored-terminal-text-in-python/) 

### Sharing

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| terminalizer: Record and Share your Terminal Sessions | [link](https://mathdatasimplified.com/2021/03/08/termanalizer-record-and-share-your-terminal-sessions/)

### Productive Hacks

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Bash For Loop: Stop Staring at your Screen. Write a Bash For Loop instead | [link](https://mathdatasimplified.com/2021/03/29/bash-for-loop-stop-staring-at-your-screen-write-a-bash-for-loop-instead/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/bash_for_loop.sh)
| Environment Variables: Save Private Information in your Local Machine | [link](https://mathdatasimplified.com/2021/02/07/environment-variables-save-private-information-in-your-local-machine/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/environment_variables)
| Pet: A Command-line Snippet Tool That Allows you to Store your Favorite Commands | [link](https://mathdatasimplified.com/2021/01/17/pet-a-command-line-snippet-tool-that-allows-you-to-store-your-favorite-commands/)
| Loop through a list of data on your terminal | [link](https://mathdatasimplified.com/2020/11/23/loop-through-a-list-of-data-on-your-terminal/)
| Multi-run command | [link](https://mathdatasimplified.com/2020/11/23/multi-run-command/) 
| Run multiple commands in one line of code | [link](https://mathdatasimplified.com/2020/11/23/run-multiple-commands-in-one-line-of-code/)

<h1 id='cool-tools'> Cool Tools <img src="images/cool.png"> </h1>

### Better Output

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| How to Strip Outputs and Execute Interactive Code in a Python Script | [link](https://mathdatasimplified.com/2021/05/12/how-to-strip-outputs-and-execute-interactive-code-in-a-python-script/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/strip_interactive_example.py)
| rich.inspect: Produce a Beautiful Report on any Python Object | [link](https://mathdatasimplified.com/2021/04/28/rich-inspect-produce-a-beautiful-report-on-any-python-object/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/rich_inspect.py)
| Rich’s Console: Debug your Python Function in One Line of Code | [link](https://mathdatasimplified.com/2021/02/12/richs-console-debug-your-python-function-in-one-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/rich_console.py)
| loguru: Print Readable Traceback in Python | [link](https://mathdatasimplified.com/2021/01/23/loguru-print-readable-traceback-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/loguru_example.py)
| Icecream: Adding a Datetime Stamp to Python print | [link](https://mathdatasimplified.com/2021/01/15/icecream-adding-a-datetime-stamp-to-python-print/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/icecream_datetime.py)
| Icrecream: Never use print() to debug again | [link](https://mathdatasimplified.com/2021/01/01/icrecream-never-use-print-to-debug-again/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/icecream_example.py)
| Pyfiglet: Make large and unique letters out of ordinary text in Python | [link](https://mathdatasimplified.com/2020/12/22/pyfiglet-make-large-and-unique-letters-out-of-ordinary-text-in-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/pyfiglet_example.py)

### Tracking

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Stacer: Visualize the History of your CPU and Memory Usage | [link](https://mathdatasimplified.com/2021/05/02/stacer-visualize-the-history-of-your-cpu-and-memory-usage/)

### Data

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| sherlock: Search for a Username Across 298 Popular Website | [link](https://mathdatasimplified.com/2021/03/09/sherlock-search-for-a-username-across-298-popular-websites/)
| getme forecast: Get the Weather Forecast Through your Terminal | [link](https://mathdatasimplified.com/2021/01/10/getme-forecast-get-the-weather-forecast-through-your-terminal/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/getme_forecast.sh)

### Automation

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| notion-py: Access and Edit your Notion App Using Python | [link](https://mathdatasimplified.com/2021/04/01/notion-py-access-and-edit-your-notion-app-using-python/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/notion_example.py)
| organize: Automate Organizing Files with Command Line | [link](https://mathdatasimplified.com/2021/03/14/organize-automate-organizing-files-with-command-line/) 
| Schedule: Schedule your Python Functions to Run At a Specific Time | [link](https://mathdatasimplified.com/2021/01/30/schedule-schedule-your-python-functions-to-run-at-a-specific-time/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/schedule_example.py)
| notify-send: Send a Desktop Notification after Finishing Executing a File | [link](https://mathdatasimplified.com/2021/01/20/notify-send-send-a-desktop-notification-after-finishing-executing-a-file/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/notify_send.sh)
| isort: Automatically Sort your Python Imports in 1 Line of Code | [link](https://mathdatasimplified.com/2021/01/06/isort-automatically-sort-your-python-imports-in-1-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/isort_example.py)
| knockknock: Receive an email when your code finishes executing | [link](https://mathdatasimplified.com/2020/11/23/knockknock-receive-an-email-when-your-code-finishes-executing/)| [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/knockknock_example.py)

### Git and GitHub

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Github CLI: Brings GitHub to your Terminal | [link](https://mathdatasimplified.com/2021/02/21/github-cli-brings-github-to-your-terminal/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/gh_cli.sh)
| Pull one file from another branch using git | [link](https://mathdatasimplified.com/2020/11/23/pull-one-file-from-another-branch-using-git/)
| Download a file on Github using wget | [link](https://mathdatasimplified.com/2020/11/23/download-a-file-on-github-using-wget/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/download_github_file.sh)
| github1s: Read GitHub Code with VS Code on your Browser in One Second | [link](https://mathdatasimplified.com/2021/02/15/github1s-read-github-code-with-vs-code-on-your-browser-in-one-second/)
| PyGithub: Manage your Github resources using Python | [link](https://mathdatasimplified.com/2020/12/24/pygithub-manage-your-github-resources-using-python/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/pygithub_example.py)
| Astral: Organize your Github stars with ease | [link](https://mathdatasimplified.com/2020/12/18/astral-organize-your-github-stars-with-ease/)

### Alternative Approach

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| Box: Using Dot Notation to Access Keys in a Python Dictionary | [link](https://mathdatasimplified.com/2021/03/02/box-using-dot-notation-to-access-keys-in-a-python-dictionary/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/box_example.py)
| virtualenv-clone: Create a Copy of a Virtual Environment | [link](https://mathdatasimplified.com/2021/02/01/virtualenv-clone-create-a-copy-of-a-virtual-environment/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/terminal/virtualenv_clone.sh)

<h1 id='jupyter-notebook'> Jupyter Notebook <img src="images/notebook.png"> </h1>

| Title        | Explanation | Code  |
| ------------- |:-------------:| :-----:|
| nbdime: Better Version Control for Jupyter Notebook | [link](https://mathdatasimplified.com/2021/06/04/nbdime-better-version-control-for-jupyter-notebook/) 
| display in IPython: Display math equations in Jupyter Notebook | [link](https://mathdatasimplified.com/2021/03/01/display-in-ipython-display-math-equations-in-jupyter-notebook/) |[link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/notebook/display_math_equations.ipynb)
| Reuse the notebook to run the same code across different data | [link](https://mathdatasimplified.com/2020/11/23/reuse-the-notebook-to-run-the-same-code-across-different-data/)
| ngrok: Create a Public Server for your Jupyter Notebook in 1 Line of Code | [link](https://mathdatasimplified.com/2021/05/26/ngrok-create-a-public-server-for-your-jupyter-notebook-in-1-line-of-code/) | [link](https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/cool_tools/ngrok_example.sh)
