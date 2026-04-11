# Class TableRowSorter<M extends TableModel >

**Source:** `java.desktop\javax\swing\table\TableRowSorter.html`

### Class Description

```java
public class
TableRowSorter<M extends
TableModel
>

extends
DefaultRowSorter
<M,​
Integer
>
```

An implementation of

RowSorter

that provides sorting
and filtering using a

TableModel

.
The following example shows adding sorting to a

JTable

:

```java
TableModel myModel = createMyTableModel();
JTable table = new JTable(myModel);
table.setRowSorter(new TableRowSorter(myModel));
```

This will do all the wiring such that when the user does the appropriate
gesture, such as clicking on the column header, the table will
visually sort.

JTable

's row-based methods and

JTable

's
selection model refer to the view and not the underlying
model. Therefore, it is necessary to convert between the two. For
example, to get the selection in terms of

myModel

you need to convert the indices:

```java
int[] selection = table.getSelectedRows();
for (int i = 0; i < selection.length; i++) {
selection[i] = table.convertRowIndexToModel(selection[i]);
}
```

Similarly to select a row in

JTable

based on
a coordinate from the underlying model do the inverse:

```java
table.setRowSelectionInterval(table.convertRowIndexToView(row),
table.convertRowIndexToView(row));
```

The previous example assumes you have not enabled filtering. If you
have enabled filtering

convertRowIndexToView

will return
-1 for locations that are not visible in the view.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

**Type Parameters:** M

- the type of the model, which must be an implementation of

TableModel

---

### Field Details

*No entries found.*

### Constructor Details

#### public TableRowSorter()

Creates a

TableRowSorter

with an empty model.

---

#### public TableRowSorter​(
M
model)

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

**Parameters:**
- model

- the underlying

TableModel

to use,

null

is treated as an empty model

---

### Method Details

#### public void setModel​(
M
model)

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

. A value of

null

can be used to set an empty model.

**Parameters:**
- model

- the underlying model to use, or

null

---

#### public void setStringConverter​(
TableStringConverter
stringConverter)

Sets the object responsible for converting values from the
model to strings. If non-

null

this
is used to convert any object values, that do not have a
registered

Comparator

, to strings.

**Parameters:**
- stringConverter

- the object responsible for converting values
from the model to strings

---

#### public
TableStringConverter
getStringConverter()

Returns the object responsible for converting values from the
model to strings.

**Returns:**
- object responsible for converting values to strings.

---

#### public
Comparator
<?> getComparator​(int column)

Returns the

Comparator

for the specified
column. If a

Comparator

has not been specified using
the

setComparator

method a

Comparator

will be returned based on the column class
(

TableModel.getColumnClass

) of the specified column.
If the column class is

String

,

Collator.getInstance

is returned. If the
column class implements

Comparable

a private

Comparator

is returned that invokes the

compareTo

method. Otherwise

Collator.getInstance

is returned.

**Overrides:**
- getComparator

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>

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

**Overrides:**
- useToString

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>

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

### Additional Sections

#### Class TableRowSorter<M extends TableModel >

java.lang.Object

- javax.swing.RowSorter

<M>
- - javax.swing.DefaultRowSorter

<M,​

Integer

>
- - javax.swing.table.TableRowSorter<M>

javax.swing.RowSorter

<M>

- javax.swing.DefaultRowSorter

<M,​

Integer

>
- - javax.swing.table.TableRowSorter<M>

javax.swing.DefaultRowSorter

<M,​

Integer

>

- javax.swing.table.TableRowSorter<M>

javax.swing.table.TableRowSorter<M>

**Type Parameters:** M

- the type of the model, which must be an implementation of

TableModel

```java
public class
TableRowSorter<M extends
TableModel
>

extends
DefaultRowSorter
<M,​
Integer
>
```

An implementation of

RowSorter

that provides sorting
and filtering using a

TableModel

.
The following example shows adding sorting to a

JTable

:

```java
TableModel myModel = createMyTableModel();
JTable table = new JTable(myModel);
table.setRowSorter(new TableRowSorter(myModel));
```

This will do all the wiring such that when the user does the appropriate
gesture, such as clicking on the column header, the table will
visually sort.

JTable

's row-based methods and

JTable

's
selection model refer to the view and not the underlying
model. Therefore, it is necessary to convert between the two. For
example, to get the selection in terms of

myModel

you need to convert the indices:

```java
int[] selection = table.getSelectedRows();
for (int i = 0; i < selection.length; i++) {
selection[i] = table.convertRowIndexToModel(selection[i]);
}
```

Similarly to select a row in

JTable

based on
a coordinate from the underlying model do the inverse:

```java
table.setRowSelectionInterval(table.convertRowIndexToView(row),
table.convertRowIndexToView(row));
```

The previous example assumes you have not enabled filtering. If you
have enabled filtering

convertRowIndexToView

will return
-1 for locations that are not visible in the view.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

**Since:** 1.6
**See Also:** JTable

,

RowFilter

,

DefaultTableModel

,

Collator

,

Comparator

public class

TableRowSorter<M extends

TableModel

>

extends

DefaultRowSorter

<M,​

Integer

>

An implementation of

RowSorter

that provides sorting
and filtering using a

TableModel

.
The following example shows adding sorting to a

JTable

:

```java
TableModel myModel = createMyTableModel();
JTable table = new JTable(myModel);
table.setRowSorter(new TableRowSorter(myModel));
```

This will do all the wiring such that when the user does the appropriate
gesture, such as clicking on the column header, the table will
visually sort.

JTable

's row-based methods and

JTable

's
selection model refer to the view and not the underlying
model. Therefore, it is necessary to convert between the two. For
example, to get the selection in terms of

myModel

you need to convert the indices:

```java
int[] selection = table.getSelectedRows();
for (int i = 0; i < selection.length; i++) {
selection[i] = table.convertRowIndexToModel(selection[i]);
}
```

Similarly to select a row in

JTable

based on
a coordinate from the underlying model do the inverse:

```java
table.setRowSelectionInterval(table.convertRowIndexToView(row),
table.convertRowIndexToView(row));
```

The previous example assumes you have not enabled filtering. If you
have enabled filtering

convertRowIndexToView

will return
-1 for locations that are not visible in the view.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

TableModel myModel = createMyTableModel();
JTable table = new JTable(myModel);
table.setRowSorter(new TableRowSorter(myModel));

JTable

's row-based methods and

JTable

's
selection model refer to the view and not the underlying
model. Therefore, it is necessary to convert between the two. For
example, to get the selection in terms of

myModel

you need to convert the indices:

```java
int[] selection = table.getSelectedRows();
for (int i = 0; i < selection.length; i++) {
selection[i] = table.convertRowIndexToModel(selection[i]);
}
```

Similarly to select a row in

JTable

based on
a coordinate from the underlying model do the inverse:

```java
table.setRowSelectionInterval(table.convertRowIndexToView(row),
table.convertRowIndexToView(row));
```

The previous example assumes you have not enabled filtering. If you
have enabled filtering

convertRowIndexToView

will return
-1 for locations that are not visible in the view.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

int[] selection = table.getSelectedRows();
for (int i = 0; i < selection.length; i++) {
selection[i] = table.convertRowIndexToModel(selection[i]);
}

table.setRowSelectionInterval(table.convertRowIndexToView(row),
table.convertRowIndexToView(row));

The previous example assumes you have not enabled filtering. If you
have enabled filtering

convertRowIndexToView

will return
-1 for locations that are not visible in the view.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

TableRowSorter

uses

Comparator

s for doing
comparisons. The following defines how a

Comparator

is
chosen for a column:

- If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

If a

Comparator

has been specified for the column by the

setComparator

method, use it.

If the column class as returned by

getColumnClass

is

String

, use the

Comparator

returned by

Collator.getInstance()

.

If the column class implements

Comparable

, use a

Comparator

that invokes the

compareTo

method.

If a

TableStringConverter

has been specified, use it
to convert the values to

String

s and then use the

Comparator

returned by

Collator.getInstance()

.

Otherwise use the

Comparator

returned by

Collator.getInstance()

on the results from
calling

toString

on the objects.

In addition to sorting

TableRowSorter

provides the ability
to filter. A filter is specified using the

setFilter

method. The following example will only show rows containing the string
"foo":

```java
TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);
```

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

TableModel myModel = createMyTableModel();
TableRowSorter sorter = new TableRowSorter(myModel);
sorter.setRowFilter(RowFilter.regexFilter(".*foo.*"));
JTable table = new JTable(myModel);
table.setRowSorter(sorter);

If the underlying model structure changes (the

modelStructureChanged

method is invoked) the following
are reset to their default values:

Comparator

s by
column, current sort order, and whether each column is sortable. The default
sort order is natural (the same as the model), and columns are
sortable by default.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

TableRowSorter

has one formal type parameter: the type
of the model. Passing in a type that corresponds exactly to your
model allows you to filter based on your model without casting.
Refer to the documentation of

RowFilter

for an example
of this.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

WARNING:

DefaultTableModel

returns a column
class of

Object

. As such all comparisons will
be done using

toString

. This may be unnecessarily
expensive. If the column only contains one type of value, such as
an

Integer

, you should override

getColumnClass

and
return the appropriate

Class

. This will dramatically
increase the performance of this class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

DefaultRowSorter

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

- Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TableRowSorter

()

Creates a

TableRowSorter

with an empty model.

TableRowSorter

​(

M

model)

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Comparator

<?>

getComparator

​(int column)

Returns the

Comparator

for the specified
column.

TableStringConverter

getStringConverter

()

Returns the object responsible for converting values from the
model to strings.

void

setModel

​(

M

model)

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

.

void

setStringConverter

​(

TableStringConverter

stringConverter)

Sets the object responsible for converting values from the
model to strings.

protected boolean

useToString

​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

- Methods declared in class javax.swing.

DefaultRowSorter

convertRowIndexToModel

,

convertRowIndexToView

,

getMaxSortKeys

,

getModel

,

getModelWrapper

,

getRowFilter

,

getSortKeys

,

getSortsOnUpdates

,

isSortable

,

rowsDeleted

,

rowsInserted

,

rowsUpdated

,

rowsUpdated

,

setComparator

,

setMaxSortKeys

,

setModelWrapper

,

setRowFilter

,

setSortable

,

setSortKeys

,

setSortsOnUpdates

,

sort

,

toggleSortOrder

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

- Nested classes/interfaces declared in class javax.swing.

DefaultRowSorter

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

- Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.

DefaultRowSorter

DefaultRowSorter.ModelWrapper

<

M

,​

I

>

---

#### Nested classes/interfaces declared in class javax.swing. DefaultRowSorter

Nested classes/interfaces declared in class javax.swing.

RowSorter

RowSorter.SortKey

---

#### Nested classes/interfaces declared in class javax.swing. RowSorter

Constructor Summary

Constructors

Constructor

Description

TableRowSorter

()

Creates a

TableRowSorter

with an empty model.

TableRowSorter

​(

M

model)

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

---

#### Constructor Summary

Creates a

TableRowSorter

with an empty model.

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Comparator

<?>

getComparator

​(int column)

Returns the

Comparator

for the specified
column.

TableStringConverter

getStringConverter

()

Returns the object responsible for converting values from the
model to strings.

void

setModel

​(

M

model)

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

.

void

setStringConverter

​(

TableStringConverter

stringConverter)

Sets the object responsible for converting values from the
model to strings.

protected boolean

useToString

​(int column)

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

- Methods declared in class javax.swing.

DefaultRowSorter

convertRowIndexToModel

,

convertRowIndexToView

,

getMaxSortKeys

,

getModel

,

getModelWrapper

,

getRowFilter

,

getSortKeys

,

getSortsOnUpdates

,

isSortable

,

rowsDeleted

,

rowsInserted

,

rowsUpdated

,

rowsUpdated

,

setComparator

,

setMaxSortKeys

,

setModelWrapper

,

setRowFilter

,

setSortable

,

setSortKeys

,

setSortsOnUpdates

,

sort

,

toggleSortOrder

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

Returns the

Comparator

for the specified
column.

Returns the object responsible for converting values from the
model to strings.

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

.

Sets the object responsible for converting values from the
model to strings.

Returns whether or not to convert the value to a string before
doing comparisons when sorting.

Methods declared in class javax.swing.

DefaultRowSorter

convertRowIndexToModel

,

convertRowIndexToView

,

getMaxSortKeys

,

getModel

,

getModelWrapper

,

getRowFilter

,

getSortKeys

,

getSortsOnUpdates

,

isSortable

,

rowsDeleted

,

rowsInserted

,

rowsUpdated

,

rowsUpdated

,

setComparator

,

setMaxSortKeys

,

setModelWrapper

,

setRowFilter

,

setSortable

,

setSortKeys

,

setSortsOnUpdates

,

sort

,

toggleSortOrder

---

#### Methods declared in class javax.swing. DefaultRowSorter

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

- TableRowSorter

```java
public TableRowSorter()
```

Creates a

TableRowSorter

with an empty model.

- TableRowSorter

```java
public TableRowSorter​(
M
model)
```

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

**Parameters:** model

- the underlying

TableModel

to use,

null

is treated as an empty model

============ METHOD DETAIL ==========

- Method Detail

- setModel

```java
public void setModel​(
M
model)
```

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

. A value of

null

can be used to set an empty model.

**Parameters:** model

- the underlying model to use, or

null

- setStringConverter

```java
public void setStringConverter​(
TableStringConverter
stringConverter)
```

Sets the object responsible for converting values from the
model to strings. If non-

null

this
is used to convert any object values, that do not have a
registered

Comparator

, to strings.

**Parameters:** stringConverter

- the object responsible for converting values
from the model to strings

- getStringConverter

```java
public
TableStringConverter
getStringConverter()
```

Returns the object responsible for converting values from the
model to strings.

**Returns:** object responsible for converting values to strings.

- getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. If a

Comparator

has not been specified using
the

setComparator

method a

Comparator

will be returned based on the column class
(

TableModel.getColumnClass

) of the specified column.
If the column class is

String

,

Collator.getInstance

is returned. If the
column class implements

Comparable

a private

Comparator

is returned that invokes the

compareTo

method. Otherwise

Collator.getInstance

is returned.

**Overrides:** getComparator

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
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

**Overrides:** useToString

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
**Parameters:** column

- the index of the column to test, in terms of the
underlying model
**Returns:** true if values are to be converted to strings before doing
comparisons when sorting
**Throws:** IndexOutOfBoundsException

- if

column

is not valid

Constructor Detail

- TableRowSorter

```java
public TableRowSorter()
```

Creates a

TableRowSorter

with an empty model.

- TableRowSorter

```java
public TableRowSorter​(
M
model)
```

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

**Parameters:** model

- the underlying

TableModel

to use,

null

is treated as an empty model

---

#### Constructor Detail

TableRowSorter

```java
public TableRowSorter()
```

Creates a

TableRowSorter

with an empty model.

---

#### TableRowSorter

public TableRowSorter()

Creates a

TableRowSorter

with an empty model.

TableRowSorter

```java
public TableRowSorter​(
M
model)
```

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

**Parameters:** model

- the underlying

TableModel

to use,

null

is treated as an empty model

---

#### TableRowSorter

public TableRowSorter​(

M

model)

Creates a

TableRowSorter

using

model

as the underlying

TableModel

.

Method Detail

- setModel

```java
public void setModel​(
M
model)
```

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

. A value of

null

can be used to set an empty model.

**Parameters:** model

- the underlying model to use, or

null

- setStringConverter

```java
public void setStringConverter​(
TableStringConverter
stringConverter)
```

Sets the object responsible for converting values from the
model to strings. If non-

null

this
is used to convert any object values, that do not have a
registered

Comparator

, to strings.

**Parameters:** stringConverter

- the object responsible for converting values
from the model to strings

- getStringConverter

```java
public
TableStringConverter
getStringConverter()
```

Returns the object responsible for converting values from the
model to strings.

**Returns:** object responsible for converting values to strings.

- getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. If a

Comparator

has not been specified using
the

setComparator

method a

Comparator

will be returned based on the column class
(

TableModel.getColumnClass

) of the specified column.
If the column class is

String

,

Collator.getInstance

is returned. If the
column class implements

Comparable

a private

Comparator

is returned that invokes the

compareTo

method. Otherwise

Collator.getInstance

is returned.

**Overrides:** getComparator

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
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

**Overrides:** useToString

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
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

#### Method Detail

setModel

```java
public void setModel​(
M
model)
```

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

. A value of

null

can be used to set an empty model.

**Parameters:** model

- the underlying model to use, or

null

---

#### setModel

public void setModel​(

M

model)

Sets the

TableModel

to use as the underlying model
for this

TableRowSorter

. A value of

null

can be used to set an empty model.

setStringConverter

```java
public void setStringConverter​(
TableStringConverter
stringConverter)
```

Sets the object responsible for converting values from the
model to strings. If non-

null

this
is used to convert any object values, that do not have a
registered

Comparator

, to strings.

**Parameters:** stringConverter

- the object responsible for converting values
from the model to strings

---

#### setStringConverter

public void setStringConverter​(

TableStringConverter

stringConverter)

Sets the object responsible for converting values from the
model to strings. If non-

null

this
is used to convert any object values, that do not have a
registered

Comparator

, to strings.

getStringConverter

```java
public
TableStringConverter
getStringConverter()
```

Returns the object responsible for converting values from the
model to strings.

**Returns:** object responsible for converting values to strings.

---

#### getStringConverter

public

TableStringConverter

getStringConverter()

Returns the object responsible for converting values from the
model to strings.

getComparator

```java
public
Comparator
<?> getComparator​(int column)
```

Returns the

Comparator

for the specified
column. If a

Comparator

has not been specified using
the

setComparator

method a

Comparator

will be returned based on the column class
(

TableModel.getColumnClass

) of the specified column.
If the column class is

String

,

Collator.getInstance

is returned. If the
column class implements

Comparable

a private

Comparator

is returned that invokes the

compareTo

method. Otherwise

Collator.getInstance

is returned.

**Overrides:** getComparator

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
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
column. If a

Comparator

has not been specified using
the

setComparator

method a

Comparator

will be returned based on the column class
(

TableModel.getColumnClass

) of the specified column.
If the column class is

String

,

Collator.getInstance

is returned. If the
column class implements

Comparable

a private

Comparator

is returned that invokes the

compareTo

method. Otherwise

Collator.getInstance

is returned.

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

**Overrides:** useToString

in class

DefaultRowSorter

<

M

extends

TableModel

,​

Integer

>
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

---

