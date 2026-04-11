# Class DefaultRowSorter<M,​I>

**Source:** `java.desktop\javax\swing\DefaultRowSorter.html`

### Class Description

```java
public abstract class
DefaultRowSorter<M,​I>

extends
RowSorter
<M>
```

An implementation of

RowSorter

that provides sorting and
filtering around a grid-based data model.
Beyond creating and installing a

RowSorter

, you very rarely
need to interact with one directly. Refer to

TableRowSorter

for a concrete
implementation of

RowSorter

for

JTable

.

Sorting is done based on the current

SortKey

s, in order.
If two objects are equal (the

Comparator

for the
column returns 0) the next

SortKey

is used. If no

SortKey

s remain or the order is

UNSORTED

, then
the order of the rows in the model is used.

Sorting of each column is done by way of a

Comparator

that you can specify using the

setComparator

method.
If a

Comparator

has not been specified, the

Comparator

returned by

Collator.getInstance()

is used on the results of
calling

toString

on the underlying objects. The

Comparator

is never passed

null

. A

null

value is treated as occurring before a
non-

null

value, and two

null

values are
considered equal.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

**Type Parameters:** M

- the type of the model
**Type Parameters:** I

- the type of the identifier passed to the

RowFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultRowSorter()

Creates an empty

DefaultRowSorter

.

---

### Method Details

#### protected final void setModelWrapper​(
DefaultRowSorter.ModelWrapper
<
M
,​
I
> modelWrapper)

Sets the model wrapper providing the data that is being sorted and
filtered.

**Parameters:**
- modelWrapper

- the model wrapper responsible for providing the
data that gets sorted and filtered

**Throws:**
- IllegalArgumentException

- if

modelWrapper

is

null

---

#### protected final
DefaultRowSorter.ModelWrapper
<
M
,​
I
> getModelWrapper()

Returns the model wrapper providing the data that is being sorted and
filtered.

**Returns:**
- the model wrapper responsible for providing the data that
gets sorted and filtered

---

#### public final
M
getModel()

Returns the underlying model.

**Specified by:**
- getModel

in class

RowSorter

<

M

>

**Returns:**
- the underlying model

---

#### public void setSortable​(int column,
boolean sortable)

Sets whether or not the specified column is sortable. The specified
value is only checked when

toggleSortOrder

is invoked.
It is still possible to sort on a column that has been marked as
unsortable by directly setting the sort keys. The default is
true.

**Parameters:**
- column

- the column to enable or disable sorting on, in terms
of the underlying model
- sortable

- whether or not the specified column is sortable

**Throws:**
- IndexOutOfBoundsException

- if

column

is outside
the range of the model

**See Also:**
- toggleSortOrder(int)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

---

#### public boolean isSortable​(int column)

Returns true if the specified column is sortable; otherwise, false.

**Parameters:**
- column

- the column to check sorting for, in terms of the
underlying model

**Returns:**
- true if the column is sortable

**Throws:**
- IndexOutOfBoundsException

- if column is outside
the range of the underlying model

---

#### public void setSortKeys​(
List
<? extends
RowSorter.SortKey
> sortKeys)

Sets the sort keys. This creates a copy of the supplied

List

; subsequent changes to the supplied

List

do not effect this

DefaultRowSorter

.
If the sort keys have changed this triggers a sort.

**Specified by:**
- setSortKeys

in class

RowSorter

<

M

>

**Parameters:**
- sortKeys

- the new

SortKeys

;

null

is a shorthand for specifying an empty list,
indicating that the view should be unsorted

**Throws:**
- IllegalArgumentException

- if any of the values in

sortKeys

are null or have a column index outside
the range of the model

---

#### public
List
<? extends
RowSorter.SortKey
> getSortKeys()

Returns the current sort keys. This returns an unmodifiable

non-null List

. If you need to change the sort keys,
make a copy of the returned

List

, mutate the copy
and invoke

setSortKeys

with the new list.

**Specified by:**
- getSortKeys

in class

RowSorter

<

M

>

**Returns:**
- the current sort order

---

#### public void setMaxSortKeys​(int max)

Sets the maximum number of sort keys. The number of sort keys
determines how equal values are resolved when sorting. For
example, assume a table row sorter is created and

setMaxSortKeys(2)

is invoked on it. The user
clicks the header for column 1, causing the table rows to be
sorted based on the items in column 1. Next, the user clicks
the header for column 2, causing the table to be sorted based
on the items in column 2; if any items in column 2 are equal,
then those particular rows are ordered based on the items in
column 1. In this case, we say that the rows are primarily
sorted on column 2, and secondarily on column 1. If the user
then clicks the header for column 3, then the items are
primarily sorted on column 3 and secondarily sorted on column
2. Because the maximum number of sort keys has been set to 2
with

setMaxSortKeys

, column 1 no longer has an
effect on the order.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

**Parameters:**
- max

- the maximum number of sort keys

**Throws:**
- IllegalArgumentException

- if

max

< 1

---

#### public int getMaxSortKeys()

Returns the maximum number of sort keys.

**Returns:**
- the maximum number of sort keys

---

#### public void setSortsOnUpdates​(boolean sortsOnUpdates)

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked). For
example, if this is true and the user edits an entry the
location of that item in the view may change. The default is
false.

**Parameters:**
- sortsOnUpdates

- whether or not to sort on update events

---

#### public boolean getSortsOnUpdates()

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

**Returns:**
- whether or not to sort when the model is updated

---

#### public void setRowFilter​(
RowFilter
<? super
M
,​? super
I
> filter)

Sets the filter that determines which rows, if any, should be
hidden from the view. The filter is applied before sorting. A value
of

null

indicates all values from the model should be
included.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

**Parameters:**
- filter

- the filter used to determine what entries should be
included

---

#### public
RowFilter
<? super
M
,​? super
I
> getRowFilter()

Returns the filter that determines which rows, if any, should
be hidden from view.

**Returns:**
- the filter

---

#### public void toggleSortOrder​(int column)

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order. If
the specified column is not sortable, this method has no
effect.

**Specified by:**
- toggleSortOrder

in class

RowSorter

<

M

>

**Parameters:**
- column

- index of the column to make the primary sorted column,
in terms of the underlying model

**Throws:**
- IndexOutOfBoundsException

- if column is outside the range of
the underlying model

**See Also:**
- setSortable(int,boolean)

,

setMaxSortKeys(int)

---

#### public int convertRowIndexToView​(int index)

Returns the location of

index

in terms of the
view. That is, for the row

index

in the
coordinates of the underlying model this returns the row index
in terms of the view.

**Specified by:**
- convertRowIndexToView

in class

RowSorter

<

M

>

**Parameters:**
- index

- the row index in terms of the underlying model

**Returns:**
- row index in terms of the view, or -1 if index has been
filtered out of the view

**Throws:**
- IndexOutOfBoundsException

- if

index

is outside
the range of the model

---

#### public int convertRowIndexToModel​(int index)

Returns the location of

index

in terms of the
underlying model. That is, for the row

index

in
the coordinates of the view this returns the row index in terms
of the underlying model.

**Specified by:**
- convertRowIndexToModel

in class

RowSorter

<

M

>

**Parameters:**
- index

- the row index in terms of the underlying view

**Returns:**
- row index in terms of the view

**Throws:**
- IndexOutOfBoundsException

- if

index

is outside the
range of the view

---

#### public void sort()

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter. An empty

sortKeys

list
indicates that the view should unsorted, the same as the model.

**See Also:**
- setRowFilter(javax.swing.RowFilter<? super M, ? super I>)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

---

#### protected boolean useToString​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting. If true

ModelWrapper.getStringValueAt

will be used, otherwise

ModelWrapper.getValueAt

will be used. It is up to
subclasses, such as

TableRowSorter

, to honor this value
in their

ModelWrapper

implementation.

**Parameters:**
- column

- the index of the column to test, in terms of the
underlying model

**Returns:**
- true if values are to be converted to strings before doing
comparisons when sorting

**Throws:**
- IndexOutOfBoundsException

- if

column

is not valid

---

#### public void setComparator​(int column,

Comparator
<?> comparator)

Sets the

Comparator

to use when sorting the specified
column. This does not trigger a sort. If you want to sort after
setting the comparator you need to explicitly invoke

sort

.

**Parameters:**
- column

- the index of the column the

Comparator

is
to be used for, in terms of the underlying model
- comparator

- the

Comparator

to use

**Throws:**
- IndexOutOfBoundsException

- if

column

is outside
the range of the underlying model

---

#### public
Comparator
<?> getComparator​(int column)

Returns the

Comparator

for the specified
column. This will return

null

if a

Comparator

has not been specified for the column.

**Parameters:**
- column

- the column to fetch the

Comparator

for, in
terms of the underlying model

**Returns:**
- the

Comparator

for the specified column

**Throws:**
- IndexOutOfBoundsException

- if column is outside
the range of the underlying model

---

#### public void rowsInserted​(int firstRow,
int endRow)

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:**
- rowsInserted

in class

RowSorter

<

M

>

**Parameters:**
- firstRow

- the first row
- endRow

- the last row

**Throws:**
- IndexOutOfBoundsException

- if either argument is invalid, or

firstRow

>

endRow

---

#### public void rowsDeleted​(int firstRow,
int endRow)

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:**
- rowsDeleted

in class

RowSorter

<

M

>

**Parameters:**
- firstRow

- the first row
- endRow

- the last row

**Throws:**
- IndexOutOfBoundsException

- if either argument is outside
the range of the model before the change, or

firstRow

>

endRow

---

#### public void rowsUpdated​(int firstRow,
int endRow)

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:**
- rowsUpdated

in class

RowSorter

<

M

>

**Parameters:**
- firstRow

- the first row, in terms of the underlying model
- endRow

- the last row, in terms of the underlying model

**Throws:**
- IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model, or

firstRow

>

endRow

---

#### public void rowsUpdated​(int firstRow,
int endRow,
int column)

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:**
- rowsUpdated

in class

RowSorter

<

M

>

**Parameters:**
- firstRow

- the first row, in terms of the underlying model
- endRow

- the last row, in terms of the underlying model
- column

- the column that has changed, in terms of the underlying
model

**Throws:**
- IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model after the change,

firstRow

>

endRow

, or

column

is outside the range of the underlying
model

---

### Additional Sections

#### Class DefaultRowSorter<M,​I>

java.lang.Object

- javax.swing.RowSorter

<M>
- - javax.swing.DefaultRowSorter<M,​I>

javax.swing.RowSorter

<M>

- javax.swing.DefaultRowSorter<M,​I>

javax.swing.DefaultRowSorter<M,​I>

**Type Parameters:** M

- the type of the model
**Type Parameters:** I

- the type of the identifier passed to the

RowFilter

**Direct Known Subclasses:** TableRowSorter

```java
public abstract class
DefaultRowSorter<M,​I>

extends
RowSorter
<M>
```

An implementation of

RowSorter

that provides sorting and
filtering around a grid-based data model.
Beyond creating and installing a

RowSorter

, you very rarely
need to interact with one directly. Refer to

TableRowSorter

for a concrete
implementation of

RowSorter

for

JTable

.

Sorting is done based on the current

SortKey

s, in order.
If two objects are equal (the

Comparator

for the
column returns 0) the next

SortKey

is used. If no

SortKey

s remain or the order is

UNSORTED

, then
the order of the rows in the model is used.

Sorting of each column is done by way of a

Comparator

that you can specify using the

setComparator

method.
If a

Comparator

has not been specified, the

Comparator

returned by

Collator.getInstance()

is used on the results of
calling

toString

on the underlying objects. The

Comparator

is never passed

null

. A

null

value is treated as occurring before a
non-

null

value, and two

null

values are
considered equal.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

**Since:** 1.6
**See Also:** TableRowSorter

,

DefaultTableModel

,

Collator

public abstract class

DefaultRowSorter<M,​I>

extends

RowSorter

<M>

An implementation of

RowSorter

that provides sorting and
filtering around a grid-based data model.
Beyond creating and installing a

RowSorter

, you very rarely
need to interact with one directly. Refer to

TableRowSorter

for a concrete
implementation of

RowSorter

for

JTable

.

Sorting is done based on the current

SortKey

s, in order.
If two objects are equal (the

Comparator

for the
column returns 0) the next

SortKey

is used. If no

SortKey

s remain or the order is

UNSORTED

, then
the order of the rows in the model is used.

Sorting of each column is done by way of a

Comparator

that you can specify using the

setComparator

method.
If a

Comparator

has not been specified, the

Comparator

returned by

Collator.getInstance()

is used on the results of
calling

toString

on the underlying objects. The

Comparator

is never passed

null

. A

null

value is treated as occurring before a
non-

null

value, and two

null

values are
considered equal.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

Sorting is done based on the current

SortKey

s, in order.
If two objects are equal (the

Comparator

for the
column returns 0) the next

SortKey

is used. If no

SortKey

s remain or the order is

UNSORTED

, then
the order of the rows in the model is used.

Sorting of each column is done by way of a

Comparator

that you can specify using the

setComparator

method.
If a

Comparator

has not been specified, the

Comparator

returned by

Collator.getInstance()

is used on the results of
calling

toString

on the underlying objects. The

Comparator

is never passed

null

. A

null

value is treated as occurring before a
non-

null

value, and two

null

values are
considered equal.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

Sorting of each column is done by way of a

Comparator

that you can specify using the

setComparator

method.
If a

Comparator

has not been specified, the

Comparator

returned by

Collator.getInstance()

is used on the results of
calling

toString

on the underlying objects. The

Comparator

is never passed

null

. A

null

value is treated as occurring before a
non-

null

value, and two

null

values are
considered equal.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

If you specify a

Comparator

that casts its argument to
a type other than that provided by the model, a

ClassCastException

will be thrown when the data is sorted.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

In addition to sorting,

DefaultRowSorter

provides the
ability to filter rows. Filtering is done by way of a

RowFilter

that is specified using the

setRowFilter

method. If no filter has been specified all
rows are included.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

By default, rows are in unsorted order (the same as the model) and
every column is sortable. The default

Comparator

s are
documented in the subclasses (for example,

TableRowSorter

).

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. To
find the default

Comparator

s, see the concrete
implementation (for example,

TableRowSorter

). The default
sort order is unsorted (the same as the model), and columns are
sortable by default.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

DefaultRowSorter

is an abstract class. Concrete
subclasses must provide access to the underlying data by invoking

setModelWrapper

. The

setModelWrapper

method

must

be invoked soon after the constructor is
called, ideally from within the subclass's constructor.
Undefined behavior will result if you use a

DefaultRowSorter

without specifying a

ModelWrapper

.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

DefaultRowSorter

has two formal type parameters. The
first type parameter corresponds to the class of the model, for example

DefaultTableModel

. The second type parameter
corresponds to the class of the identifier passed to the

RowFilter

. Refer to

TableRowSorter

and

RowFilter

for more details on the type parameters.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

.

- Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultRowSorter

()

Creates an empty

DefaultRowSorter

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

convertRowIndexToModel

​(int index)

Returns the location of

index

in terms of the
underlying model.

int

convertRowIndexToView

​(int index)

Returns the location of

index

in terms of the
view.

Comparator

<?>

getComparator

​(int column)

Returns the

Comparator

for the specified
column.

int

getMaxSortKeys

()

Returns the maximum number of sort keys.

M

getModel

()

Returns the underlying model.

protected

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

getModelWrapper

()

Returns the model wrapper providing the data that is being sorted and
filtered.

RowFilter

<? super

M

,​? super

I

>

getRowFilter

()

Returns the filter that determines which rows, if any, should
be hidden from view.

List

<? extends

RowSorter.SortKey

>

getSortKeys

()

Returns the current sort keys.

boolean

getSortsOnUpdates

()

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

boolean

isSortable

​(int column)

Returns true if the specified column is sortable; otherwise, false.

void

rowsDeleted

​(int firstRow,
int endRow)

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

void

rowsInserted

​(int firstRow,
int endRow)

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

void

rowsUpdated

​(int firstRow,
int endRow)

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

void

rowsUpdated

​(int firstRow,
int endRow,
int column)

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

void

setComparator

​(int column,

Comparator

<?> comparator)

Sets the

Comparator

to use when sorting the specified
column.

void

setMaxSortKeys

​(int max)

Sets the maximum number of sort keys.

protected void

setModelWrapper

​(

DefaultRowSorter.ModelWrapper

<

M

,​

I

> modelWrapper)

Sets the model wrapper providing the data that is being sorted and
filtered.

void

setRowFilter

​(

RowFilter

<? super

M

,​? super

I

> filter)

Sets the filter that determines which rows, if any, should be
hidden from the view.

void

setSortable

​(int column,
boolean sortable)

Sets whether or not the specified column is sortable.

void

setSortKeys

​(

List

<? extends

RowSorter.SortKey

> sortKeys)

Sets the sort keys.

void

setSortsOnUpdates

​(boolean sortsOnUpdates)

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked).

void

sort

()

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter.

void

toggleSortOrder

​(int column)

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order.

protected boolean

useToString

​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

- Methods declared in class javax.swing.

RowSorter

addRowSorterListener

,

allRowsChanged

,

fireRowSorterChanged

,

fireSortOrderChanged

,

getModelRowCount

,

getViewRowCount

,

modelStructureChanged

,

removeRowSorterListener

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

.

- Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

---

#### Nested Class Summary

DefaultRowSorter.ModelWrapper

is responsible for providing
the data that gets sorted by

DefaultRowSorter

.

Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

---

#### Nested classes/interfaces declared in class javax.swing. RowSorter

Constructor Summary

Constructors

Constructor

Description

DefaultRowSorter

()

Creates an empty

DefaultRowSorter

.

---

#### Constructor Summary

Creates an empty

DefaultRowSorter

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

convertRowIndexToModel

​(int index)

Returns the location of

index

in terms of the
underlying model.

int

convertRowIndexToView

​(int index)

Returns the location of

index

in terms of the
view.

Comparator

<?>

getComparator

​(int column)

Returns the

Comparator

for the specified
column.

int

getMaxSortKeys

()

Returns the maximum number of sort keys.

M

getModel

()

Returns the underlying model.

protected

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

getModelWrapper

()

Returns the model wrapper providing the data that is being sorted and
filtered.

RowFilter

<? super

M

,​? super

I

>

getRowFilter

()

Returns the filter that determines which rows, if any, should
be hidden from view.

List

<? extends

RowSorter.SortKey

>

getSortKeys

()

Returns the current sort keys.

boolean

getSortsOnUpdates

()

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

boolean

isSortable

​(int column)

Returns true if the specified column is sortable; otherwise, false.

void

rowsDeleted

​(int firstRow,
int endRow)

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

void

rowsInserted

​(int firstRow,
int endRow)

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

void

rowsUpdated

​(int firstRow,
int endRow)

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

void

rowsUpdated

​(int firstRow,
int endRow,
int column)

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

void

setComparator

​(int column,

Comparator

<?> comparator)

Sets the

Comparator

to use when sorting the specified
column.

void

setMaxSortKeys

​(int max)

Sets the maximum number of sort keys.

protected void

setModelWrapper

​(

DefaultRowSorter.ModelWrapper

<

M

,​

I

> modelWrapper)

Sets the model wrapper providing the data that is being sorted and
filtered.

void

setRowFilter

​(

RowFilter

<? super

M

,​? super

I

> filter)

Sets the filter that determines which rows, if any, should be
hidden from the view.

void

setSortable

​(int column,
boolean sortable)

Sets whether or not the specified column is sortable.

void

setSortKeys

​(

List

<? extends

RowSorter.SortKey

> sortKeys)

Sets the sort keys.

void

setSortsOnUpdates

​(boolean sortsOnUpdates)

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked).

void

sort

()

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter.

void

toggleSortOrder

​(int column)

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order.

protected boolean

useToString

​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

- Methods declared in class javax.swing.

RowSorter

addRowSorterListener

,

allRowsChanged

,

fireRowSorterChanged

,

fireSortOrderChanged

,

getModelRowCount

,

getViewRowCount

,

modelStructureChanged

,

removeRowSorterListener

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the location of

index

in terms of the
underlying model.

Returns the location of

index

in terms of the
view.

Returns the

Comparator

for the specified
column.

Returns the maximum number of sort keys.

Returns the underlying model.

Returns the model wrapper providing the data that is being sorted and
filtered.

Returns the filter that determines which rows, if any, should
be hidden from view.

Returns the current sort keys.

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

Returns true if the specified column is sortable; otherwise, false.

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

Sets the

Comparator

to use when sorting the specified
column.

Sets the maximum number of sort keys.

Sets the model wrapper providing the data that is being sorted and
filtered.

Sets the filter that determines which rows, if any, should be
hidden from the view.

Sets whether or not the specified column is sortable.

Sets the sort keys.

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked).

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter.

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order.

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

Methods declared in class javax.swing.

RowSorter

addRowSorterListener

,

allRowsChanged

,

fireRowSorterChanged

,

fireSortOrderChanged

,

getModelRowCount

,

getViewRowCount

,

modelStructureChanged

,

removeRowSorterListener

---

#### Methods declared in class javax.swing. RowSorter

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultRowSorter

```java
public DefaultRowSorter()
```

Creates an empty

DefaultRowSorter

.

============ METHOD DETAIL ==========

- Method Detail

- setModelWrapper

```java
protected final void setModelWrapper​(
DefaultRowSorter.ModelWrapper
<
M
,​
I
> modelWrapper)
```

Sets the model wrapper providing the data that is being sorted and
filtered.

**Parameters:** modelWrapper

- the model wrapper responsible for providing the
data that gets sorted and filtered
**Throws:** IllegalArgumentException

- if

modelWrapper

is

null

- getModelWrapper

```java
protected final
DefaultRowSorter.ModelWrapper
<
M
,​
I
> getModelWrapper()
```

Returns the model wrapper providing the data that is being sorted and
filtered.

**Returns:** the model wrapper responsible for providing the data that
gets sorted and filtered

- getModel

```java
public final
M
getModel()
```

Returns the underlying model.

**Specified by:** getModel

in class

RowSorter

<

M

>
**Returns:** the underlying model

- setSortable

```java
public void setSortable​(int column,
boolean sortable)
```

Sets whether or not the specified column is sortable. The specified
value is only checked when

toggleSortOrder

is invoked.
It is still possible to sort on a column that has been marked as
unsortable by directly setting the sort keys. The default is
true.

**Parameters:** column

- the column to enable or disable sorting on, in terms
of the underlying model
**Parameters:** sortable

- whether or not the specified column is sortable
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the model
**See Also:** toggleSortOrder(int)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

- isSortable

```java
public boolean isSortable​(int column)
```

Returns true if the specified column is sortable; otherwise, false.

**Parameters:** column

- the column to check sorting for, in terms of the
underlying model
**Returns:** true if the column is sortable
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

- setSortKeys

```java
public void setSortKeys​(
List
<? extends
RowSorter.SortKey
> sortKeys)
```

Sets the sort keys. This creates a copy of the supplied

List

; subsequent changes to the supplied

List

do not effect this

DefaultRowSorter

.
If the sort keys have changed this triggers a sort.

**Specified by:** setSortKeys

in class

RowSorter

<

M

>
**Parameters:** sortKeys

- the new

SortKeys

;

null

is a shorthand for specifying an empty list,
indicating that the view should be unsorted
**Throws:** IllegalArgumentException

- if any of the values in

sortKeys

are null or have a column index outside
the range of the model

- getSortKeys

```java
public
List
<? extends
RowSorter.SortKey
> getSortKeys()
```

Returns the current sort keys. This returns an unmodifiable

non-null List

. If you need to change the sort keys,
make a copy of the returned

List

, mutate the copy
and invoke

setSortKeys

with the new list.

**Specified by:** getSortKeys

in class

RowSorter

<

M

>
**Returns:** the current sort order

- setMaxSortKeys

```java
public void setMaxSortKeys​(int max)
```

Sets the maximum number of sort keys. The number of sort keys
determines how equal values are resolved when sorting. For
example, assume a table row sorter is created and

setMaxSortKeys(2)

is invoked on it. The user
clicks the header for column 1, causing the table rows to be
sorted based on the items in column 1. Next, the user clicks
the header for column 2, causing the table to be sorted based
on the items in column 2; if any items in column 2 are equal,
then those particular rows are ordered based on the items in
column 1. In this case, we say that the rows are primarily
sorted on column 2, and secondarily on column 1. If the user
then clicks the header for column 3, then the items are
primarily sorted on column 3 and secondarily sorted on column
2. Because the maximum number of sort keys has been set to 2
with

setMaxSortKeys

, column 1 no longer has an
effect on the order.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

**Parameters:** max

- the maximum number of sort keys
**Throws:** IllegalArgumentException

- if

max

< 1

- getMaxSortKeys

```java
public int getMaxSortKeys()
```

Returns the maximum number of sort keys.

**Returns:** the maximum number of sort keys

- setSortsOnUpdates

```java
public void setSortsOnUpdates​(boolean sortsOnUpdates)
```

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked). For
example, if this is true and the user edits an entry the
location of that item in the view may change. The default is
false.

**Parameters:** sortsOnUpdates

- whether or not to sort on update events

- getSortsOnUpdates

```java
public boolean getSortsOnUpdates()
```

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

**Returns:** whether or not to sort when the model is updated

- setRowFilter

```java
public void setRowFilter​(
RowFilter
<? super
M
,​? super
I
> filter)
```

Sets the filter that determines which rows, if any, should be
hidden from the view. The filter is applied before sorting. A value
of

null

indicates all values from the model should be
included.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

**Parameters:** filter

- the filter used to determine what entries should be
included

- getRowFilter

```java
public
RowFilter
<? super
M
,​? super
I
> getRowFilter()
```

Returns the filter that determines which rows, if any, should
be hidden from view.

**Returns:** the filter

- toggleSortOrder

```java
public void toggleSortOrder​(int column)
```

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order. If
the specified column is not sortable, this method has no
effect.

**Specified by:** toggleSortOrder

in class

RowSorter

<

M

>
**Parameters:** column

- index of the column to make the primary sorted column,
in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if column is outside the range of
the underlying model
**See Also:** setSortable(int,boolean)

,

setMaxSortKeys(int)

- convertRowIndexToView

```java
public int convertRowIndexToView​(int index)
```

Returns the location of

index

in terms of the
view. That is, for the row

index

in the
coordinates of the underlying model this returns the row index
in terms of the view.

**Specified by:** convertRowIndexToView

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying model
**Returns:** row index in terms of the view, or -1 if index has been
filtered out of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside
the range of the model

- convertRowIndexToModel

```java
public int convertRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
underlying model. That is, for the row

index

in
the coordinates of the view this returns the row index in terms
of the underlying model.

**Specified by:** convertRowIndexToModel

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying view
**Returns:** row index in terms of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside the
range of the view

- sort

```java
public void sort()
```

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter. An empty

sortKeys

list
indicates that the view should unsorted, the same as the model.

**See Also:** setRowFilter(javax.swing.RowFilter<? super M, ? super I>)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

- useToString

```java
protected boolean useToString​(int column)
```

Returns whether or not to convert the value to a string before
doing comparisons when sorting. If true

ModelWrapper.getStringValueAt

will be used, otherwise

ModelWrapper.getValueAt

will be used. It is up to
subclasses, such as

TableRowSorter

, to honor this value
in their

ModelWrapper

implementation.

**Parameters:** column

- the index of the column to test, in terms of the
underlying model
**Returns:** true if values are to be converted to strings before doing
comparisons when sorting
**Throws:** IndexOutOfBoundsException

- if

column

is not valid

- setComparator

```java
public void setComparator​(int column,

Comparator
<?> comparator)
```

Sets the

Comparator

to use when sorting the specified
column. This does not trigger a sort. If you want to sort after
setting the comparator you need to explicitly invoke

sort

.

**Parameters:** column

- the index of the column the

Comparator

is
to be used for, in terms of the underlying model
**Parameters:** comparator

- the

Comparator

to use
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the underlying model

- getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. This will return

null

if a

Comparator

has not been specified for the column.

**Parameters:** column

- the column to fetch the

Comparator

for, in
terms of the underlying model
**Returns:** the

Comparator

for the specified column
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

- rowsInserted

```java
public void rowsInserted​(int firstRow,
int endRow)
```

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsInserted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is invalid, or

firstRow

>

endRow

- rowsDeleted

```java
public void rowsDeleted​(int firstRow,
int endRow)
```

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsDeleted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the model before the change, or

firstRow

>

endRow

- rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow)
```

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model, or

firstRow

>

endRow

- rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow,
int column)
```

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Parameters:** column

- the column that has changed, in terms of the underlying
model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model after the change,

firstRow

>

endRow

, or

column

is outside the range of the underlying
model

Constructor Detail

- DefaultRowSorter

```java
public DefaultRowSorter()
```

Creates an empty

DefaultRowSorter

.

---

#### Constructor Detail

DefaultRowSorter

```java
public DefaultRowSorter()
```

Creates an empty

DefaultRowSorter

.

---

#### DefaultRowSorter

public DefaultRowSorter()

Creates an empty

DefaultRowSorter

.

Method Detail

- setModelWrapper

```java
protected final void setModelWrapper​(
DefaultRowSorter.ModelWrapper
<
M
,​
I
> modelWrapper)
```

Sets the model wrapper providing the data that is being sorted and
filtered.

**Parameters:** modelWrapper

- the model wrapper responsible for providing the
data that gets sorted and filtered
**Throws:** IllegalArgumentException

- if

modelWrapper

is

null

- getModelWrapper

```java
protected final
DefaultRowSorter.ModelWrapper
<
M
,​
I
> getModelWrapper()
```

Returns the model wrapper providing the data that is being sorted and
filtered.

**Returns:** the model wrapper responsible for providing the data that
gets sorted and filtered

- getModel

```java
public final
M
getModel()
```

Returns the underlying model.

**Specified by:** getModel

in class

RowSorter

<

M

>
**Returns:** the underlying model

- setSortable

```java
public void setSortable​(int column,
boolean sortable)
```

Sets whether or not the specified column is sortable. The specified
value is only checked when

toggleSortOrder

is invoked.
It is still possible to sort on a column that has been marked as
unsortable by directly setting the sort keys. The default is
true.

**Parameters:** column

- the column to enable or disable sorting on, in terms
of the underlying model
**Parameters:** sortable

- whether or not the specified column is sortable
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the model
**See Also:** toggleSortOrder(int)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

- isSortable

```java
public boolean isSortable​(int column)
```

Returns true if the specified column is sortable; otherwise, false.

**Parameters:** column

- the column to check sorting for, in terms of the
underlying model
**Returns:** true if the column is sortable
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

- setSortKeys

```java
public void setSortKeys​(
List
<? extends
RowSorter.SortKey
> sortKeys)
```

Sets the sort keys. This creates a copy of the supplied

List

; subsequent changes to the supplied

List

do not effect this

DefaultRowSorter

.
If the sort keys have changed this triggers a sort.

**Specified by:** setSortKeys

in class

RowSorter

<

M

>
**Parameters:** sortKeys

- the new

SortKeys

;

null

is a shorthand for specifying an empty list,
indicating that the view should be unsorted
**Throws:** IllegalArgumentException

- if any of the values in

sortKeys

are null or have a column index outside
the range of the model

- getSortKeys

```java
public
List
<? extends
RowSorter.SortKey
> getSortKeys()
```

Returns the current sort keys. This returns an unmodifiable

non-null List

. If you need to change the sort keys,
make a copy of the returned

List

, mutate the copy
and invoke

setSortKeys

with the new list.

**Specified by:** getSortKeys

in class

RowSorter

<

M

>
**Returns:** the current sort order

- setMaxSortKeys

```java
public void setMaxSortKeys​(int max)
```

Sets the maximum number of sort keys. The number of sort keys
determines how equal values are resolved when sorting. For
example, assume a table row sorter is created and

setMaxSortKeys(2)

is invoked on it. The user
clicks the header for column 1, causing the table rows to be
sorted based on the items in column 1. Next, the user clicks
the header for column 2, causing the table to be sorted based
on the items in column 2; if any items in column 2 are equal,
then those particular rows are ordered based on the items in
column 1. In this case, we say that the rows are primarily
sorted on column 2, and secondarily on column 1. If the user
then clicks the header for column 3, then the items are
primarily sorted on column 3 and secondarily sorted on column
2. Because the maximum number of sort keys has been set to 2
with

setMaxSortKeys

, column 1 no longer has an
effect on the order.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

**Parameters:** max

- the maximum number of sort keys
**Throws:** IllegalArgumentException

- if

max

< 1

- getMaxSortKeys

```java
public int getMaxSortKeys()
```

Returns the maximum number of sort keys.

**Returns:** the maximum number of sort keys

- setSortsOnUpdates

```java
public void setSortsOnUpdates​(boolean sortsOnUpdates)
```

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked). For
example, if this is true and the user edits an entry the
location of that item in the view may change. The default is
false.

**Parameters:** sortsOnUpdates

- whether or not to sort on update events

- getSortsOnUpdates

```java
public boolean getSortsOnUpdates()
```

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

**Returns:** whether or not to sort when the model is updated

- setRowFilter

```java
public void setRowFilter​(
RowFilter
<? super
M
,​? super
I
> filter)
```

Sets the filter that determines which rows, if any, should be
hidden from the view. The filter is applied before sorting. A value
of

null

indicates all values from the model should be
included.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

**Parameters:** filter

- the filter used to determine what entries should be
included

- getRowFilter

```java
public
RowFilter
<? super
M
,​? super
I
> getRowFilter()
```

Returns the filter that determines which rows, if any, should
be hidden from view.

**Returns:** the filter

- toggleSortOrder

```java
public void toggleSortOrder​(int column)
```

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order. If
the specified column is not sortable, this method has no
effect.

**Specified by:** toggleSortOrder

in class

RowSorter

<

M

>
**Parameters:** column

- index of the column to make the primary sorted column,
in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if column is outside the range of
the underlying model
**See Also:** setSortable(int,boolean)

,

setMaxSortKeys(int)

- convertRowIndexToView

```java
public int convertRowIndexToView​(int index)
```

Returns the location of

index

in terms of the
view. That is, for the row

index

in the
coordinates of the underlying model this returns the row index
in terms of the view.

**Specified by:** convertRowIndexToView

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying model
**Returns:** row index in terms of the view, or -1 if index has been
filtered out of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside
the range of the model

- convertRowIndexToModel

```java
public int convertRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
underlying model. That is, for the row

index

in
the coordinates of the view this returns the row index in terms
of the underlying model.

**Specified by:** convertRowIndexToModel

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying view
**Returns:** row index in terms of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside the
range of the view

- sort

```java
public void sort()
```

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter. An empty

sortKeys

list
indicates that the view should unsorted, the same as the model.

**See Also:** setRowFilter(javax.swing.RowFilter<? super M, ? super I>)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

- useToString

```java
protected boolean useToString​(int column)
```

Returns whether or not to convert the value to a string before
doing comparisons when sorting. If true

ModelWrapper.getStringValueAt

will be used, otherwise

ModelWrapper.getValueAt

will be used. It is up to
subclasses, such as

TableRowSorter

, to honor this value
in their

ModelWrapper

implementation.

**Parameters:** column

- the index of the column to test, in terms of the
underlying model
**Returns:** true if values are to be converted to strings before doing
comparisons when sorting
**Throws:** IndexOutOfBoundsException

- if

column

is not valid

- setComparator

```java
public void setComparator​(int column,

Comparator
<?> comparator)
```

Sets the

Comparator

to use when sorting the specified
column. This does not trigger a sort. If you want to sort after
setting the comparator you need to explicitly invoke

sort

.

**Parameters:** column

- the index of the column the

Comparator

is
to be used for, in terms of the underlying model
**Parameters:** comparator

- the

Comparator

to use
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the underlying model

- getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. This will return

null

if a

Comparator

has not been specified for the column.

**Parameters:** column

- the column to fetch the

Comparator

for, in
terms of the underlying model
**Returns:** the

Comparator

for the specified column
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

- rowsInserted

```java
public void rowsInserted​(int firstRow,
int endRow)
```

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsInserted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is invalid, or

firstRow

>

endRow

- rowsDeleted

```java
public void rowsDeleted​(int firstRow,
int endRow)
```

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsDeleted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the model before the change, or

firstRow

>

endRow

- rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow)
```

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model, or

firstRow

>

endRow

- rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow,
int column)
```

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Parameters:** column

- the column that has changed, in terms of the underlying
model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model after the change,

firstRow

>

endRow

, or

column

is outside the range of the underlying
model

---

#### Method Detail

setModelWrapper

```java
protected final void setModelWrapper​(
DefaultRowSorter.ModelWrapper
<
M
,​
I
> modelWrapper)
```

Sets the model wrapper providing the data that is being sorted and
filtered.

**Parameters:** modelWrapper

- the model wrapper responsible for providing the
data that gets sorted and filtered
**Throws:** IllegalArgumentException

- if

modelWrapper

is

null

---

#### setModelWrapper

protected final void setModelWrapper​(

DefaultRowSorter.ModelWrapper

<

M

,​

I

> modelWrapper)

Sets the model wrapper providing the data that is being sorted and
filtered.

getModelWrapper

```java
protected final
DefaultRowSorter.ModelWrapper
<
M
,​
I
> getModelWrapper()
```

Returns the model wrapper providing the data that is being sorted and
filtered.

**Returns:** the model wrapper responsible for providing the data that
gets sorted and filtered

---

#### getModelWrapper

protected final

DefaultRowSorter.ModelWrapper

<

M

,​

I

> getModelWrapper()

Returns the model wrapper providing the data that is being sorted and
filtered.

getModel

```java
public final
M
getModel()
```

Returns the underlying model.

**Specified by:** getModel

in class

RowSorter

<

M

>
**Returns:** the underlying model

---

#### getModel

public final

M

getModel()

Returns the underlying model.

setSortable

```java
public void setSortable​(int column,
boolean sortable)
```

Sets whether or not the specified column is sortable. The specified
value is only checked when

toggleSortOrder

is invoked.
It is still possible to sort on a column that has been marked as
unsortable by directly setting the sort keys. The default is
true.

**Parameters:** column

- the column to enable or disable sorting on, in terms
of the underlying model
**Parameters:** sortable

- whether or not the specified column is sortable
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the model
**See Also:** toggleSortOrder(int)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

---

#### setSortable

public void setSortable​(int column,
boolean sortable)

Sets whether or not the specified column is sortable. The specified
value is only checked when

toggleSortOrder

is invoked.
It is still possible to sort on a column that has been marked as
unsortable by directly setting the sort keys. The default is
true.

isSortable

```java
public boolean isSortable​(int column)
```

Returns true if the specified column is sortable; otherwise, false.

**Parameters:** column

- the column to check sorting for, in terms of the
underlying model
**Returns:** true if the column is sortable
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

---

#### isSortable

public boolean isSortable​(int column)

Returns true if the specified column is sortable; otherwise, false.

setSortKeys

```java
public void setSortKeys​(
List
<? extends
RowSorter.SortKey
> sortKeys)
```

Sets the sort keys. This creates a copy of the supplied

List

; subsequent changes to the supplied

List

do not effect this

DefaultRowSorter

.
If the sort keys have changed this triggers a sort.

**Specified by:** setSortKeys

in class

RowSorter

<

M

>
**Parameters:** sortKeys

- the new

SortKeys

;

null

is a shorthand for specifying an empty list,
indicating that the view should be unsorted
**Throws:** IllegalArgumentException

- if any of the values in

sortKeys

are null or have a column index outside
the range of the model

---

#### setSortKeys

public void setSortKeys​(

List

<? extends

RowSorter.SortKey

> sortKeys)

Sets the sort keys. This creates a copy of the supplied

List

; subsequent changes to the supplied

List

do not effect this

DefaultRowSorter

.
If the sort keys have changed this triggers a sort.

getSortKeys

```java
public
List
<? extends
RowSorter.SortKey
> getSortKeys()
```

Returns the current sort keys. This returns an unmodifiable

non-null List

. If you need to change the sort keys,
make a copy of the returned

List

, mutate the copy
and invoke

setSortKeys

with the new list.

**Specified by:** getSortKeys

in class

RowSorter

<

M

>
**Returns:** the current sort order

---

#### getSortKeys

public

List

<? extends

RowSorter.SortKey

> getSortKeys()

Returns the current sort keys. This returns an unmodifiable

non-null List

. If you need to change the sort keys,
make a copy of the returned

List

, mutate the copy
and invoke

setSortKeys

with the new list.

setMaxSortKeys

```java
public void setMaxSortKeys​(int max)
```

Sets the maximum number of sort keys. The number of sort keys
determines how equal values are resolved when sorting. For
example, assume a table row sorter is created and

setMaxSortKeys(2)

is invoked on it. The user
clicks the header for column 1, causing the table rows to be
sorted based on the items in column 1. Next, the user clicks
the header for column 2, causing the table to be sorted based
on the items in column 2; if any items in column 2 are equal,
then those particular rows are ordered based on the items in
column 1. In this case, we say that the rows are primarily
sorted on column 2, and secondarily on column 1. If the user
then clicks the header for column 3, then the items are
primarily sorted on column 3 and secondarily sorted on column
2. Because the maximum number of sort keys has been set to 2
with

setMaxSortKeys

, column 1 no longer has an
effect on the order.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

**Parameters:** max

- the maximum number of sort keys
**Throws:** IllegalArgumentException

- if

max

< 1

---

#### setMaxSortKeys

public void setMaxSortKeys​(int max)

Sets the maximum number of sort keys. The number of sort keys
determines how equal values are resolved when sorting. For
example, assume a table row sorter is created and

setMaxSortKeys(2)

is invoked on it. The user
clicks the header for column 1, causing the table rows to be
sorted based on the items in column 1. Next, the user clicks
the header for column 2, causing the table to be sorted based
on the items in column 2; if any items in column 2 are equal,
then those particular rows are ordered based on the items in
column 1. In this case, we say that the rows are primarily
sorted on column 2, and secondarily on column 1. If the user
then clicks the header for column 3, then the items are
primarily sorted on column 3 and secondarily sorted on column
2. Because the maximum number of sort keys has been set to 2
with

setMaxSortKeys

, column 1 no longer has an
effect on the order.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

The maximum number of sort keys is enforced by

toggleSortOrder

. You can specify more sort
keys by invoking

setSortKeys

directly and they will
all be honored. However if

toggleSortOrder

is subsequently
invoked the maximum number of sort keys will be enforced.
The default value is 3.

getMaxSortKeys

```java
public int getMaxSortKeys()
```

Returns the maximum number of sort keys.

**Returns:** the maximum number of sort keys

---

#### getMaxSortKeys

public int getMaxSortKeys()

Returns the maximum number of sort keys.

setSortsOnUpdates

```java
public void setSortsOnUpdates​(boolean sortsOnUpdates)
```

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked). For
example, if this is true and the user edits an entry the
location of that item in the view may change. The default is
false.

**Parameters:** sortsOnUpdates

- whether or not to sort on update events

---

#### setSortsOnUpdates

public void setSortsOnUpdates​(boolean sortsOnUpdates)

If true, specifies that a sort should happen when the underlying
model is updated (

rowsUpdated

is invoked). For
example, if this is true and the user edits an entry the
location of that item in the view may change. The default is
false.

getSortsOnUpdates

```java
public boolean getSortsOnUpdates()
```

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

**Returns:** whether or not to sort when the model is updated

---

#### getSortsOnUpdates

public boolean getSortsOnUpdates()

Returns true if a sort should happen when the underlying
model is updated; otherwise, returns false.

setRowFilter

```java
public void setRowFilter​(
RowFilter
<? super
M
,​? super
I
> filter)
```

Sets the filter that determines which rows, if any, should be
hidden from the view. The filter is applied before sorting. A value
of

null

indicates all values from the model should be
included.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

**Parameters:** filter

- the filter used to determine what entries should be
included

---

#### setRowFilter

public void setRowFilter​(

RowFilter

<? super

M

,​? super

I

> filter)

Sets the filter that determines which rows, if any, should be
hidden from the view. The filter is applied before sorting. A value
of

null

indicates all values from the model should be
included.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

RowFilter

's

include

method is passed an

Entry

that wraps the underlying model. The number
of columns in the

Entry

corresponds to the
number of columns in the

ModelWrapper

. The identifier
comes from the

ModelWrapper

as well.

This method triggers a sort.

This method triggers a sort.

getRowFilter

```java
public
RowFilter
<? super
M
,​? super
I
> getRowFilter()
```

Returns the filter that determines which rows, if any, should
be hidden from view.

**Returns:** the filter

---

#### getRowFilter

public

RowFilter

<? super

M

,​? super

I

> getRowFilter()

Returns the filter that determines which rows, if any, should
be hidden from view.

toggleSortOrder

```java
public void toggleSortOrder​(int column)
```

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order. If
the specified column is not sortable, this method has no
effect.

**Specified by:** toggleSortOrder

in class

RowSorter

<

M

>
**Parameters:** column

- index of the column to make the primary sorted column,
in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if column is outside the range of
the underlying model
**See Also:** setSortable(int,boolean)

,

setMaxSortKeys(int)

---

#### toggleSortOrder

public void toggleSortOrder​(int column)

Reverses the sort order from ascending to descending (or
descending to ascending) if the specified column is already the
primary sorted column; otherwise, makes the specified column
the primary sorted column, with an ascending sort order. If
the specified column is not sortable, this method has no
effect.

convertRowIndexToView

```java
public int convertRowIndexToView​(int index)
```

Returns the location of

index

in terms of the
view. That is, for the row

index

in the
coordinates of the underlying model this returns the row index
in terms of the view.

**Specified by:** convertRowIndexToView

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying model
**Returns:** row index in terms of the view, or -1 if index has been
filtered out of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside
the range of the model

---

#### convertRowIndexToView

public int convertRowIndexToView​(int index)

Returns the location of

index

in terms of the
view. That is, for the row

index

in the
coordinates of the underlying model this returns the row index
in terms of the view.

convertRowIndexToModel

```java
public int convertRowIndexToModel​(int index)
```

Returns the location of

index

in terms of the
underlying model. That is, for the row

index

in
the coordinates of the view this returns the row index in terms
of the underlying model.

**Specified by:** convertRowIndexToModel

in class

RowSorter

<

M

>
**Parameters:** index

- the row index in terms of the underlying view
**Returns:** row index in terms of the view
**Throws:** IndexOutOfBoundsException

- if

index

is outside the
range of the view

---

#### convertRowIndexToModel

public int convertRowIndexToModel​(int index)

Returns the location of

index

in terms of the
underlying model. That is, for the row

index

in
the coordinates of the view this returns the row index in terms
of the underlying model.

sort

```java
public void sort()
```

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter. An empty

sortKeys

list
indicates that the view should unsorted, the same as the model.

**See Also:** setRowFilter(javax.swing.RowFilter<? super M, ? super I>)

,

setSortKeys(java.util.List<? extends javax.swing.RowSorter.SortKey>)

---

#### sort

public void sort()

Sorts and filters the rows in the view based on the sort keys
of the columns currently being sorted and the filter, if any,
associated with this sorter. An empty

sortKeys

list
indicates that the view should unsorted, the same as the model.

useToString

```java
protected boolean useToString​(int column)
```

Returns whether or not to convert the value to a string before
doing comparisons when sorting. If true

ModelWrapper.getStringValueAt

will be used, otherwise

ModelWrapper.getValueAt

will be used. It is up to
subclasses, such as

TableRowSorter

, to honor this value
in their

ModelWrapper

implementation.

**Parameters:** column

- the index of the column to test, in terms of the
underlying model
**Returns:** true if values are to be converted to strings before doing
comparisons when sorting
**Throws:** IndexOutOfBoundsException

- if

column

is not valid

---

#### useToString

protected boolean useToString​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting. If true

ModelWrapper.getStringValueAt

will be used, otherwise

ModelWrapper.getValueAt

will be used. It is up to
subclasses, such as

TableRowSorter

, to honor this value
in their

ModelWrapper

implementation.

setComparator

```java
public void setComparator​(int column,

Comparator
<?> comparator)
```

Sets the

Comparator

to use when sorting the specified
column. This does not trigger a sort. If you want to sort after
setting the comparator you need to explicitly invoke

sort

.

**Parameters:** column

- the index of the column the

Comparator

is
to be used for, in terms of the underlying model
**Parameters:** comparator

- the

Comparator

to use
**Throws:** IndexOutOfBoundsException

- if

column

is outside
the range of the underlying model

---

#### setComparator

public void setComparator​(int column,

Comparator

<?> comparator)

Sets the

Comparator

to use when sorting the specified
column. This does not trigger a sort. If you want to sort after
setting the comparator you need to explicitly invoke

sort

.

getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. This will return

null

if a

Comparator

has not been specified for the column.

**Parameters:** column

- the column to fetch the

Comparator

for, in
terms of the underlying model
**Returns:** the

Comparator

for the specified column
**Throws:** IndexOutOfBoundsException

- if column is outside
the range of the underlying model

---

#### getComparator

public

Comparator

<?> getComparator​(int column)

Returns the

Comparator

for the specified
column. This will return

null

if a

Comparator

has not been specified for the column.

rowsInserted

```java
public void rowsInserted​(int firstRow,
int endRow)
```

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsInserted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is invalid, or

firstRow

>

endRow

---

#### rowsInserted

public void rowsInserted​(int firstRow,
int endRow)

Invoked when rows have been inserted into the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

The arguments give the indices of the effected range.
The first argument is in terms of the model before the change, and
must be less than or equal to the size of the model before the change.
The second argument is in terms of the model after the change and must
be less than the size of the model after the change. For example,
if you have a 5-row model and add 3 items to the end of the model
the indices are 5, 7.

You normally do not call this method. This method is public
to allow view classes to call it.

You normally do not call this method. This method is public
to allow view classes to call it.

rowsDeleted

```java
public void rowsDeleted​(int firstRow,
int endRow)
```

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsDeleted

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row
**Parameters:** endRow

- the last row
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the model before the change, or

firstRow

>

endRow

---

#### rowsDeleted

public void rowsDeleted​(int firstRow,
int endRow)

Invoked when rows have been deleted from the underlying model
in the specified range (inclusive).

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

The arguments give the indices of the effected range and
are in terms of the model

before

the change.
For example, if you have a 5-row model and delete 3 items from the end
of the model the indices are 2, 4.

You normally do not call this method. This method is public
to allow view classes to call it.

You normally do not call this method. This method is public
to allow view classes to call it.

rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow)
```

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model, or

firstRow

>

endRow

---

#### rowsUpdated

public void rowsUpdated​(int firstRow,
int endRow)

Invoked when rows have been changed in the underlying model
between the specified range (inclusive).

You normally do not call this method. This method is public
to allow view classes to call it.

You normally do not call this method. This method is public
to allow view classes to call it.

rowsUpdated

```java
public void rowsUpdated​(int firstRow,
int endRow,
int column)
```

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

You normally do not call this method. This method is public
to allow view classes to call it.

**Specified by:** rowsUpdated

in class

RowSorter

<

M

>
**Parameters:** firstRow

- the first row, in terms of the underlying model
**Parameters:** endRow

- the last row, in terms of the underlying model
**Parameters:** column

- the column that has changed, in terms of the underlying
model
**Throws:** IndexOutOfBoundsException

- if either argument is outside
the range of the underlying model after the change,

firstRow

>

endRow

, or

column

is outside the range of the underlying
model

---

#### rowsUpdated

public void rowsUpdated​(int firstRow,
int endRow,
int column)

Invoked when the column in the rows have been updated in
the underlying model between the specified range.

You normally do not call this method. This method is public
to allow view classes to call it.

You normally do not call this method. This method is public
to allow view classes to call it.

---

