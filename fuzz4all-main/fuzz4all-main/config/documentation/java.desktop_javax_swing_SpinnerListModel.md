# Class SpinnerListModel

**Source:** `java.desktop\javax\swing\SpinnerListModel.html`

### Class Description

```java
public class
SpinnerListModel

extends
AbstractSpinnerModel

implements
Serializable
```

A simple implementation of

SpinnerModel

whose
values are defined by an array or a

List

.
For example to create a model defined by
an array of the names of the days of the week:

```java
String[] days = new DateFormatSymbols().getWeekdays();
SpinnerModel model = new SpinnerListModel(Arrays.asList(days).subList(1, 8));
```

This class only stores a reference to the array or

List

so if an element of the underlying sequence changes, it's up
to the application to notify the

ChangeListeners

by calling

fireStateChanged

.

This model inherits a

ChangeListener

.
The

ChangeListener

s are notified whenever the
model's

value

or

list

properties changes.

**All Implemented Interfaces:** Serializable

,

SpinnerModel

---

### Field Details

*No entries found.*

### Constructor Details

#### public SpinnerListModel​(
List
<?> values)

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.
The initial value (

current element

)
of the model will be

values.get(0)

.
If

values

is

null

or has zero
size, an

IllegalArugmentException

is thrown.

**Parameters:**
- values

- the sequence this model represents

**Throws:**
- IllegalArgumentException

- if

values

is

null

or zero size

---

#### public SpinnerListModel​(
Object
[] values)

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array. The initial value of the model
will be

values[0]

. If

values

is

null

or has zero length, an

IllegalArgumentException

is thrown.

**Parameters:**
- values

- the sequence this model represents

**Throws:**
- IllegalArgumentException

- if

values

is

null

or zero length

---

#### public SpinnerListModel()

Constructs an effectively empty

SpinnerListModel

.
The model's list will contain a single

"empty"

string element.

---

### Method Details

#### public
List
<?> getList()

Returns the

List

that defines the sequence for this model.

**Returns:**
- the value of the

list

property

**See Also:**
- setList(java.util.List<?>)

---

#### public void setList​(
List
<?> list)

Changes the list that defines this sequence and resets the index
of the models

value

to zero. Note that

list

is not copied, the model just stores a reference to it.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

**Parameters:**
- list

- the sequence that this model represents

**Throws:**
- IllegalArgumentException

- if

list

is

null

or zero length

**See Also:**
- getList()

---

#### public
Object
getValue()

Returns the current element of the sequence.

**Specified by:**
- getValue

in interface

SpinnerModel

**Returns:**
- the

value

property

**See Also:**
- SpinnerModel.getValue()

,

setValue(java.lang.Object)

---

#### public void setValue​(
Object
elt)

Changes the current element of the sequence and notifies

ChangeListeners

. If the specified
value is not equal to an element of the underlying sequence
then an

IllegalArgumentException

is thrown.
In the following example the

setValue

call
would cause an exception to be thrown:

```java
String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");
```

**Specified by:**
- setValue

in interface

SpinnerModel

**Parameters:**
- elt

- the sequence element that will be model's current value

**Throws:**
- IllegalArgumentException

- if the specified value isn't allowed

**See Also:**
- SpinnerModel.setValue(java.lang.Object)

,

getValue()

---

#### public
Object
getNextValue()

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

**Specified by:**
- getNextValue

in interface

SpinnerModel

**Returns:**
- the next legal value of the underlying sequence or

null

if value is already the last element

**See Also:**
- SpinnerModel.getNextValue()

,

getPreviousValue()

---

#### public
Object
getPreviousValue()

Returns the previous element of the underlying sequence or

null

if value is already the first element.

**Specified by:**
- getPreviousValue

in interface

SpinnerModel

**Returns:**
- the previous element of the underlying sequence or

null

if value is already the first element

**See Also:**
- SpinnerModel.getPreviousValue()

,

getNextValue()

---

### Additional Sections

#### Class SpinnerListModel

java.lang.Object

- javax.swing.AbstractSpinnerModel
- - javax.swing.SpinnerListModel

javax.swing.AbstractSpinnerModel

- javax.swing.SpinnerListModel

javax.swing.SpinnerListModel

**All Implemented Interfaces:** Serializable

,

SpinnerModel

```java
public class
SpinnerListModel

extends
AbstractSpinnerModel

implements
Serializable
```

A simple implementation of

SpinnerModel

whose
values are defined by an array or a

List

.
For example to create a model defined by
an array of the names of the days of the week:

```java
String[] days = new DateFormatSymbols().getWeekdays();
SpinnerModel model = new SpinnerListModel(Arrays.asList(days).subList(1, 8));
```

This class only stores a reference to the array or

List

so if an element of the underlying sequence changes, it's up
to the application to notify the

ChangeListeners

by calling

fireStateChanged

.

This model inherits a

ChangeListener

.
The

ChangeListener

s are notified whenever the
model's

value

or

list

properties changes.

**Since:** 1.4
**See Also:** JSpinner

,

SpinnerModel

,

AbstractSpinnerModel

,

SpinnerNumberModel

,

SpinnerDateModel

,

Serialized Form

public class

SpinnerListModel

extends

AbstractSpinnerModel

implements

Serializable

A simple implementation of

SpinnerModel

whose
values are defined by an array or a

List

.
For example to create a model defined by
an array of the names of the days of the week:

```java
String[] days = new DateFormatSymbols().getWeekdays();
SpinnerModel model = new SpinnerListModel(Arrays.asList(days).subList(1, 8));
```

This class only stores a reference to the array or

List

so if an element of the underlying sequence changes, it's up
to the application to notify the

ChangeListeners

by calling

fireStateChanged

.

This model inherits a

ChangeListener

.
The

ChangeListener

s are notified whenever the
model's

value

or

list

properties changes.

String[] days = new DateFormatSymbols().getWeekdays();
SpinnerModel model = new SpinnerListModel(Arrays.asList(days).subList(1, 8));

This model inherits a

ChangeListener

.
The

ChangeListener

s are notified whenever the
model's

value

or

list

properties changes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SpinnerListModel

()

Constructs an effectively empty

SpinnerListModel

.

SpinnerListModel

​(

Object

[] values)

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array.

SpinnerListModel

​(

List

<?> values)

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<?>

getList

()

Returns the

List

that defines the sequence for this model.

Object

getNextValue

()

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

Object

getPreviousValue

()

Returns the previous element of the underlying sequence or

null

if value is already the first element.

Object

getValue

()

Returns the current element of the sequence.

void

setList

​(

List

<?> list)

Changes the list that defines this sequence and resets the index
of the models

value

to zero.

void

setValue

​(

Object

elt)

Changes the current element of the sequence and notifies

ChangeListeners

.

- Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

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

Field Summary

- Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

---

#### Field Summary

Fields declared in class javax.swing.

AbstractSpinnerModel

listenerList

---

#### Fields declared in class javax.swing. AbstractSpinnerModel

Constructor Summary

Constructors

Constructor

Description

SpinnerListModel

()

Constructs an effectively empty

SpinnerListModel

.

SpinnerListModel

​(

Object

[] values)

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array.

SpinnerListModel

​(

List

<?> values)

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.

---

#### Constructor Summary

Constructs an effectively empty

SpinnerListModel

.

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array.

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<?>

getList

()

Returns the

List

that defines the sequence for this model.

Object

getNextValue

()

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

Object

getPreviousValue

()

Returns the previous element of the underlying sequence or

null

if value is already the first element.

Object

getValue

()

Returns the current element of the sequence.

void

setList

​(

List

<?> list)

Changes the list that defines this sequence and resets the index
of the models

value

to zero.

void

setValue

​(

Object

elt)

Changes the current element of the sequence and notifies

ChangeListeners

.

- Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

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

List

that defines the sequence for this model.

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

Returns the previous element of the underlying sequence or

null

if value is already the first element.

Returns the current element of the sequence.

Changes the list that defines this sequence and resets the index
of the models

value

to zero.

Changes the current element of the sequence and notifies

ChangeListeners

.

Methods declared in class javax.swing.

AbstractSpinnerModel

addChangeListener

,

fireStateChanged

,

getChangeListeners

,

getListeners

,

removeChangeListener

---

#### Methods declared in class javax.swing. AbstractSpinnerModel

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

- SpinnerListModel

```java
public SpinnerListModel​(
List
<?> values)
```

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.
The initial value (

current element

)
of the model will be

values.get(0)

.
If

values

is

null

or has zero
size, an

IllegalArugmentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero size

- SpinnerListModel

```java
public SpinnerListModel​(
Object
[] values)
```

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array. The initial value of the model
will be

values[0]

. If

values

is

null

or has zero length, an

IllegalArgumentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero length

- SpinnerListModel

```java
public SpinnerListModel()
```

Constructs an effectively empty

SpinnerListModel

.
The model's list will contain a single

"empty"

string element.

============ METHOD DETAIL ==========

- Method Detail

- getList

```java
public
List
<?> getList()
```

Returns the

List

that defines the sequence for this model.

**Returns:** the value of the

list

property
**See Also:** setList(java.util.List<?>)

- setList

```java
public void setList​(
List
<?> list)
```

Changes the list that defines this sequence and resets the index
of the models

value

to zero. Note that

list

is not copied, the model just stores a reference to it.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

**Parameters:** list

- the sequence that this model represents
**Throws:** IllegalArgumentException

- if

list

is

null

or zero length
**See Also:** getList()

- getValue

```java
public
Object
getValue()
```

Returns the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** SpinnerModel.getValue()

,

setValue(java.lang.Object)

- setValue

```java
public void setValue​(
Object
elt)
```

Changes the current element of the sequence and notifies

ChangeListeners

. If the specified
value is not equal to an element of the underlying sequence
then an

IllegalArgumentException

is thrown.
In the following example the

setValue

call
would cause an exception to be thrown:

```java
String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");
```

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** elt

- the sequence element that will be model's current value
**Throws:** IllegalArgumentException

- if the specified value isn't allowed
**See Also:** SpinnerModel.setValue(java.lang.Object)

,

getValue()

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next legal value of the underlying sequence or

null

if value is already the last element
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous element of the underlying sequence or

null

if value is already the first element.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous element of the underlying sequence or

null

if value is already the first element
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

Constructor Detail

- SpinnerListModel

```java
public SpinnerListModel​(
List
<?> values)
```

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.
The initial value (

current element

)
of the model will be

values.get(0)

.
If

values

is

null

or has zero
size, an

IllegalArugmentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero size

- SpinnerListModel

```java
public SpinnerListModel​(
Object
[] values)
```

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array. The initial value of the model
will be

values[0]

. If

values

is

null

or has zero length, an

IllegalArgumentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero length

- SpinnerListModel

```java
public SpinnerListModel()
```

Constructs an effectively empty

SpinnerListModel

.
The model's list will contain a single

"empty"

string element.

---

#### Constructor Detail

SpinnerListModel

```java
public SpinnerListModel​(
List
<?> values)
```

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.
The initial value (

current element

)
of the model will be

values.get(0)

.
If

values

is

null

or has zero
size, an

IllegalArugmentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero size

---

#### SpinnerListModel

public SpinnerListModel​(

List

<?> values)

Constructs a

SpinnerModel

whose sequence of
values is defined by the specified

List

.
The initial value (

current element

)
of the model will be

values.get(0)

.
If

values

is

null

or has zero
size, an

IllegalArugmentException

is thrown.

SpinnerListModel

```java
public SpinnerListModel​(
Object
[] values)
```

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array. The initial value of the model
will be

values[0]

. If

values

is

null

or has zero length, an

IllegalArgumentException

is thrown.

**Parameters:** values

- the sequence this model represents
**Throws:** IllegalArgumentException

- if

values

is

null

or zero length

---

#### SpinnerListModel

public SpinnerListModel​(

Object

[] values)

Constructs a

SpinnerModel

whose sequence of values
is defined by the specified array. The initial value of the model
will be

values[0]

. If

values

is

null

or has zero length, an

IllegalArgumentException

is thrown.

SpinnerListModel

```java
public SpinnerListModel()
```

Constructs an effectively empty

SpinnerListModel

.
The model's list will contain a single

"empty"

string element.

---

#### SpinnerListModel

public SpinnerListModel()

Constructs an effectively empty

SpinnerListModel

.
The model's list will contain a single

"empty"

string element.

Method Detail

- getList

```java
public
List
<?> getList()
```

Returns the

List

that defines the sequence for this model.

**Returns:** the value of the

list

property
**See Also:** setList(java.util.List<?>)

- setList

```java
public void setList​(
List
<?> list)
```

Changes the list that defines this sequence and resets the index
of the models

value

to zero. Note that

list

is not copied, the model just stores a reference to it.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

**Parameters:** list

- the sequence that this model represents
**Throws:** IllegalArgumentException

- if

list

is

null

or zero length
**See Also:** getList()

- getValue

```java
public
Object
getValue()
```

Returns the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** SpinnerModel.getValue()

,

setValue(java.lang.Object)

- setValue

```java
public void setValue​(
Object
elt)
```

Changes the current element of the sequence and notifies

ChangeListeners

. If the specified
value is not equal to an element of the underlying sequence
then an

IllegalArgumentException

is thrown.
In the following example the

setValue

call
would cause an exception to be thrown:

```java
String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");
```

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** elt

- the sequence element that will be model's current value
**Throws:** IllegalArgumentException

- if the specified value isn't allowed
**See Also:** SpinnerModel.setValue(java.lang.Object)

,

getValue()

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next legal value of the underlying sequence or

null

if value is already the last element
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous element of the underlying sequence or

null

if value is already the first element.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous element of the underlying sequence or

null

if value is already the first element
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

---

#### Method Detail

getList

```java
public
List
<?> getList()
```

Returns the

List

that defines the sequence for this model.

**Returns:** the value of the

list

property
**See Also:** setList(java.util.List<?>)

---

#### getList

public

List

<?> getList()

Returns the

List

that defines the sequence for this model.

setList

```java
public void setList​(
List
<?> list)
```

Changes the list that defines this sequence and resets the index
of the models

value

to zero. Note that

list

is not copied, the model just stores a reference to it.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

**Parameters:** list

- the sequence that this model represents
**Throws:** IllegalArgumentException

- if

list

is

null

or zero length
**See Also:** getList()

---

#### setList

public void setList​(

List

<?> list)

Changes the list that defines this sequence and resets the index
of the models

value

to zero. Note that

list

is not copied, the model just stores a reference to it.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

This method fires a

ChangeEvent

if

list

is
not equal to the current list.

getValue

```java
public
Object
getValue()
```

Returns the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the

value

property
**See Also:** SpinnerModel.getValue()

,

setValue(java.lang.Object)

---

#### getValue

public

Object

getValue()

Returns the current element of the sequence.

setValue

```java
public void setValue​(
Object
elt)
```

Changes the current element of the sequence and notifies

ChangeListeners

. If the specified
value is not equal to an element of the underlying sequence
then an

IllegalArgumentException

is thrown.
In the following example the

setValue

call
would cause an exception to be thrown:

```java
String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");
```

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** elt

- the sequence element that will be model's current value
**Throws:** IllegalArgumentException

- if the specified value isn't allowed
**See Also:** SpinnerModel.setValue(java.lang.Object)

,

getValue()

---

#### setValue

public void setValue​(

Object

elt)

Changes the current element of the sequence and notifies

ChangeListeners

. If the specified
value is not equal to an element of the underlying sequence
then an

IllegalArgumentException

is thrown.
In the following example the

setValue

call
would cause an exception to be thrown:

```java
String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");
```

String[] values = {"one", "two", "free", "four"};
SpinnerModel model = new SpinnerListModel(values);
model.setValue("TWO");

getNextValue

```java
public
Object
getNextValue()
```

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** the next legal value of the underlying sequence or

null

if value is already the last element
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

---

#### getNextValue

public

Object

getNextValue()

Returns the next legal value of the underlying sequence or

null

if value is already the last element.

getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous element of the underlying sequence or

null

if value is already the first element.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** the previous element of the underlying sequence or

null

if value is already the first element
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

---

#### getPreviousValue

public

Object

getPreviousValue()

Returns the previous element of the underlying sequence or

null

if value is already the first element.

---

