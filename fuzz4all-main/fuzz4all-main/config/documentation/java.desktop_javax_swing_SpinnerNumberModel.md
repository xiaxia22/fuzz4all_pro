# Class SpinnerNumberModel

**Source:** `java.desktop\javax\swing\SpinnerNumberModel.html`

### Class Description

```java
public class
SpinnerNumberModel

extends
AbstractSpinnerModel

implements
Serializable
```

A

SpinnerModel

for sequences of numbers.
The upper and lower bounds of the sequence are defined
by properties called

minimum

and

maximum

. The size of the increase or decrease
computed by the

nextValue

and

previousValue

methods is defined by a property called

stepSize

. The

minimum

and

maximum

properties can be

null

to indicate that the sequence has no lower or upper limit.
All of the properties in this class are defined in terms of two
generic types:

Number

and

Comparable

, so that all Java numeric types
may be accommodated. Internally, there's only support for
values whose type is one of the primitive

Number

types:

Double

,

Float

,

Long

,

Integer

,

Short

, or

Byte

.

To create a

SpinnerNumberModel

for the integer
range zero to one hundred, with
fifty as the initial value, one could write:

```java
Integer value = Integer.valueOf(50);
Integer min = Integer.valueOf(0);
Integer max = Integer.valueOf(100);
Integer step = Integer.valueOf(1);
SpinnerNumberModel model = new SpinnerNumberModel(value, min, max, step);
int fifty = model.getNumber().intValue();
```

Spinners for integers and doubles are common, so special constructors
for these cases are provided. For example to create the model in
the previous example, one could also write:

```java
SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);
```

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

properties changes.

**All Implemented Interfaces:** Serializable

,

SpinnerModel

---

### Field Details

*No entries found.*

### Constructor Details

#### public SpinnerNumberModel​(
Number
value,

Comparable
<?> minimum,

Comparable
<?> maximum,

Number
stepSize)

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

. The

nextValue

and

previousValue

methods
compute elements of the sequence by adding or subtracting

stepSize

respectively. All of the parameters
must be mutually

Comparable

,

value

and

stepSize

must be instances of

Integer

Long

,

Float

, or

Double

.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

**Parameters:**
- value

- the current (non

null

) value of the model
- minimum

- the first number in the sequence or

null
- maximum

- the last number in the sequence or

null
- stepSize

- the difference between elements of the sequence

**Throws:**
- IllegalArgumentException

- if stepSize or value is

null

or if the following expression is false:

minimum <= value <= maximum

---

#### public SpinnerNumberModel​(int value,
int minimum,
int maximum,
int stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:**
- value

- the current value of the model
- minimum

- the first number in the sequence
- maximum

- the last number in the sequence
- stepSize

- the difference between elements of the sequence

**Throws:**
- IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

---

#### public SpinnerNumberModel​(double value,
double minimum,
double maximum,
double stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:**
- value

- the current value of the model
- minimum

- the first number in the sequence
- maximum

- the last number in the sequence
- stepSize

- the difference between elements of the sequence

**Throws:**
- IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

---

#### public SpinnerNumberModel()

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

---

### Method Details

#### public void setMinimum​(
Comparable
<?> minimum)

Changes the lower bound for numbers in this sequence.
If

minimum

is

null

,
then there is no lower bound. No bounds checking is done here;
the new

minimum

value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

getNextValue

,

getPreviousValue

, or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

**Parameters:**
- minimum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value

**See Also:**
- getMinimum()

,

setMaximum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public
Comparable
<?> getMinimum()

Returns the first number in this sequence.

**Returns:**
- the value of the

minimum

property

**See Also:**
- setMinimum(java.lang.Comparable<?>)

---

#### public void setMaximum​(
Comparable
<?> maximum)

Changes the upper bound for numbers in this sequence.
If

maximum

is

null

, then there
is no upper bound. No bounds checking is done here; the new

maximum

value may invalidate the

(minimum <= value < maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

next

,

previous

,
or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

**Parameters:**
- maximum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value

**See Also:**
- getMaximum()

,

setMinimum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public
Comparable
<?> getMaximum()

Returns the last number in the sequence.

**Returns:**
- the value of the

maximum

property

**See Also:**
- setMaximum(java.lang.Comparable<?>)

---

#### public void setStepSize​(
Number
stepSize)

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods. An

IllegalArgumentException

is thrown if

stepSize

is

null

.

This method fires a

ChangeEvent

if the

stepSize

has changed.

**Parameters:**
- stepSize

- the size of the value change computed by the

getNextValue

and

getPreviousValue

methods

**See Also:**
- getNextValue()

,

getPreviousValue()

,

getStepSize()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### public
Number
getStepSize()

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

**Returns:**
- the value of the

stepSize

property

**See Also:**
- setStepSize(java.lang.Number)

---

#### public
Object
getNextValue()

Returns the next number in the sequence.

**Specified by:**
- getNextValue

in interface

SpinnerModel

**Returns:**
- value + stepSize

or

null

if the sum
exceeds

maximum

.

**See Also:**
- SpinnerModel.getNextValue()

,

getPreviousValue()

,

setStepSize(java.lang.Number)

---

#### public
Object
getPreviousValue()

Returns the previous number in the sequence.

**Specified by:**
- getPreviousValue

in interface

SpinnerModel

**Returns:**
- value - stepSize

, or

null

if the sum is less
than

minimum

.

**See Also:**
- SpinnerModel.getPreviousValue()

,

getNextValue()

,

setStepSize(java.lang.Number)

---

#### public
Number
getNumber()

Returns the value of the current element of the sequence.

**Returns:**
- the value property

**See Also:**
- setValue(java.lang.Object)

---

#### public
Object
getValue()

Returns the value of the current element of the sequence.

**Specified by:**
- getValue

in interface

SpinnerModel

**Returns:**
- the value property

**See Also:**
- setValue(java.lang.Object)

,

getNumber()

---

#### public void setValue​(
Object
value)

Sets the current value for this sequence. If

value

is

null

, or not a

Number

, an

IllegalArgumentException

is thrown. No
bounds checking is done here; the new value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. It's also possible to set
the value to be something that wouldn't naturally occur in the sequence,
i.e. a value that's not modulo the

stepSize

.
This is to simplify updating the model, and to accommodate
spinners that don't want to restrict values that have been
directly entered by the user. Naturally, one should ensure that the

(minimum <= value <= maximum)

invariant is true
before calling the

next

,

previous

, or

setValue

methods.

This method fires a

ChangeEvent

if the value has changed.

**Specified by:**
- setValue

in interface

SpinnerModel

**Parameters:**
- value

- the current (non

null

)

Number

for this sequence

**Throws:**
- IllegalArgumentException

- if

value

is

null

or not a

Number

**See Also:**
- getNumber()

,

getValue()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

### Additional Sections

#### Class SpinnerNumberModel

java.lang.Object

- javax.swing.AbstractSpinnerModel
- - javax.swing.SpinnerNumberModel

javax.swing.AbstractSpinnerModel

- javax.swing.SpinnerNumberModel

javax.swing.SpinnerNumberModel

**All Implemented Interfaces:** Serializable

,

SpinnerModel

```java
public class
SpinnerNumberModel

extends
AbstractSpinnerModel

implements
Serializable
```

A

SpinnerModel

for sequences of numbers.
The upper and lower bounds of the sequence are defined
by properties called

minimum

and

maximum

. The size of the increase or decrease
computed by the

nextValue

and

previousValue

methods is defined by a property called

stepSize

. The

minimum

and

maximum

properties can be

null

to indicate that the sequence has no lower or upper limit.
All of the properties in this class are defined in terms of two
generic types:

Number

and

Comparable

, so that all Java numeric types
may be accommodated. Internally, there's only support for
values whose type is one of the primitive

Number

types:

Double

,

Float

,

Long

,

Integer

,

Short

, or

Byte

.

To create a

SpinnerNumberModel

for the integer
range zero to one hundred, with
fifty as the initial value, one could write:

```java
Integer value = Integer.valueOf(50);
Integer min = Integer.valueOf(0);
Integer max = Integer.valueOf(100);
Integer step = Integer.valueOf(1);
SpinnerNumberModel model = new SpinnerNumberModel(value, min, max, step);
int fifty = model.getNumber().intValue();
```

Spinners for integers and doubles are common, so special constructors
for these cases are provided. For example to create the model in
the previous example, one could also write:

```java
SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);
```

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

properties changes.

**Since:** 1.4
**See Also:** JSpinner

,

SpinnerModel

,

AbstractSpinnerModel

,

SpinnerListModel

,

SpinnerDateModel

,

Serialized Form

public class

SpinnerNumberModel

extends

AbstractSpinnerModel

implements

Serializable

A

SpinnerModel

for sequences of numbers.
The upper and lower bounds of the sequence are defined
by properties called

minimum

and

maximum

. The size of the increase or decrease
computed by the

nextValue

and

previousValue

methods is defined by a property called

stepSize

. The

minimum

and

maximum

properties can be

null

to indicate that the sequence has no lower or upper limit.
All of the properties in this class are defined in terms of two
generic types:

Number

and

Comparable

, so that all Java numeric types
may be accommodated. Internally, there's only support for
values whose type is one of the primitive

Number

types:

Double

,

Float

,

Long

,

Integer

,

Short

, or

Byte

.

To create a

SpinnerNumberModel

for the integer
range zero to one hundred, with
fifty as the initial value, one could write:

```java
Integer value = Integer.valueOf(50);
Integer min = Integer.valueOf(0);
Integer max = Integer.valueOf(100);
Integer step = Integer.valueOf(1);
SpinnerNumberModel model = new SpinnerNumberModel(value, min, max, step);
int fifty = model.getNumber().intValue();
```

Spinners for integers and doubles are common, so special constructors
for these cases are provided. For example to create the model in
the previous example, one could also write:

```java
SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);
```

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

properties changes.

To create a

SpinnerNumberModel

for the integer
range zero to one hundred, with
fifty as the initial value, one could write:

```java
Integer value = Integer.valueOf(50);
Integer min = Integer.valueOf(0);
Integer max = Integer.valueOf(100);
Integer step = Integer.valueOf(1);
SpinnerNumberModel model = new SpinnerNumberModel(value, min, max, step);
int fifty = model.getNumber().intValue();
```

Spinners for integers and doubles are common, so special constructors
for these cases are provided. For example to create the model in
the previous example, one could also write:

```java
SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);
```

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

properties changes.

Integer value = Integer.valueOf(50);
Integer min = Integer.valueOf(0);
Integer max = Integer.valueOf(100);
Integer step = Integer.valueOf(1);
SpinnerNumberModel model = new SpinnerNumberModel(value, min, max, step);
int fifty = model.getNumber().intValue();

Spinners for integers and doubles are common, so special constructors
for these cases are provided. For example to create the model in
the previous example, one could also write:

```java
SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);
```

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

properties changes.

SpinnerNumberModel model = new SpinnerNumberModel(50, 0, 100, 1);

This model inherits a

ChangeListener

.
The

ChangeListeners

are notified
whenever the model's

value

,

stepSize

,

minimum

, or

maximum

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

SpinnerNumberModel

()

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

SpinnerNumberModel

​(double value,
double minimum,
double maximum,
double stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

​(int value,
int minimum,
int maximum,
int stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

​(

Number

value,

Comparable

<?> minimum,

Comparable

<?> maximum,

Number

stepSize)

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Comparable

<?>

getMaximum

()

Returns the last number in the sequence.

Comparable

<?>

getMinimum

()

Returns the first number in this sequence.

Object

getNextValue

()

Returns the next number in the sequence.

Number

getNumber

()

Returns the value of the current element of the sequence.

Object

getPreviousValue

()

Returns the previous number in the sequence.

Number

getStepSize

()

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

Object

getValue

()

Returns the value of the current element of the sequence.

void

setMaximum

​(

Comparable

<?> maximum)

Changes the upper bound for numbers in this sequence.

void

setMinimum

​(

Comparable

<?> minimum)

Changes the lower bound for numbers in this sequence.

void

setStepSize

​(

Number

stepSize)

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

void

setValue

​(

Object

value)

Sets the current value for this sequence.

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

SpinnerNumberModel

()

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

SpinnerNumberModel

​(double value,
double minimum,
double maximum,
double stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

​(int value,
int minimum,
int maximum,
int stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

​(

Number

value,

Comparable

<?> minimum,

Comparable

<?> maximum,

Number

stepSize)

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

.

---

#### Constructor Summary

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Comparable

<?>

getMaximum

()

Returns the last number in the sequence.

Comparable

<?>

getMinimum

()

Returns the first number in this sequence.

Object

getNextValue

()

Returns the next number in the sequence.

Number

getNumber

()

Returns the value of the current element of the sequence.

Object

getPreviousValue

()

Returns the previous number in the sequence.

Number

getStepSize

()

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

Object

getValue

()

Returns the value of the current element of the sequence.

void

setMaximum

​(

Comparable

<?> maximum)

Changes the upper bound for numbers in this sequence.

void

setMinimum

​(

Comparable

<?> minimum)

Changes the lower bound for numbers in this sequence.

void

setStepSize

​(

Number

stepSize)

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

void

setValue

​(

Object

value)

Sets the current value for this sequence.

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

Returns the last number in the sequence.

Returns the first number in this sequence.

Returns the next number in the sequence.

Returns the value of the current element of the sequence.

Returns the previous number in the sequence.

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

Changes the upper bound for numbers in this sequence.

Changes the lower bound for numbers in this sequence.

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

Sets the current value for this sequence.

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

- SpinnerNumberModel

```java
public SpinnerNumberModel​(
Number
value,

Comparable
<?> minimum,

Comparable
<?> maximum,

Number
stepSize)
```

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

. The

nextValue

and

previousValue

methods
compute elements of the sequence by adding or subtracting

stepSize

respectively. All of the parameters
must be mutually

Comparable

,

value

and

stepSize

must be instances of

Integer

Long

,

Float

, or

Double

.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** minimum

- the first number in the sequence or

null
**Parameters:** maximum

- the last number in the sequence or

null
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if stepSize or value is

null

or if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel​(int value,
int minimum,
int maximum,
int stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel​(double value,
double minimum,
double maximum,
double stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel()
```

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

============ METHOD DETAIL ==========

- Method Detail

- setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Changes the lower bound for numbers in this sequence.
If

minimum

is

null

,
then there is no lower bound. No bounds checking is done here;
the new

minimum

value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

getNextValue

,

getPreviousValue

, or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

**Parameters:** minimum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMinimum()

,

setMaximum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the first number in this sequence.

**Returns:** the value of the

minimum

property
**See Also:** setMinimum(java.lang.Comparable<?>)

- setMaximum

```java
public void setMaximum​(
Comparable
<?> maximum)
```

Changes the upper bound for numbers in this sequence.
If

maximum

is

null

, then there
is no upper bound. No bounds checking is done here; the new

maximum

value may invalidate the

(minimum <= value < maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

next

,

previous

,
or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

**Parameters:** maximum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMaximum()

,

setMinimum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the last number in the sequence.

**Returns:** the value of the

maximum

property
**See Also:** setMaximum(java.lang.Comparable<?>)

- setStepSize

```java
public void setStepSize​(
Number
stepSize)
```

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods. An

IllegalArgumentException

is thrown if

stepSize

is

null

.

This method fires a

ChangeEvent

if the

stepSize

has changed.

**Parameters:** stepSize

- the size of the value change computed by the

getNextValue

and

getPreviousValue

methods
**See Also:** getNextValue()

,

getPreviousValue()

,

getStepSize()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getStepSize

```java
public
Number
getStepSize()
```

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

**Returns:** the value of the

stepSize

property
**See Also:** setStepSize(java.lang.Number)

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next number in the sequence.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** value + stepSize

or

null

if the sum
exceeds

maximum

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setStepSize(java.lang.Number)

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous number in the sequence.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** value - stepSize

, or

null

if the sum is less
than

minimum

.
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setStepSize(java.lang.Number)

- getNumber

```java
public
Number
getNumber()
```

Returns the value of the current element of the sequence.

**Returns:** the value property
**See Also:** setValue(java.lang.Object)

- getValue

```java
public
Object
getValue()
```

Returns the value of the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the value property
**See Also:** setValue(java.lang.Object)

,

getNumber()

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for this sequence. If

value

is

null

, or not a

Number

, an

IllegalArgumentException

is thrown. No
bounds checking is done here; the new value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. It's also possible to set
the value to be something that wouldn't naturally occur in the sequence,
i.e. a value that's not modulo the

stepSize

.
This is to simplify updating the model, and to accommodate
spinners that don't want to restrict values that have been
directly entered by the user. Naturally, one should ensure that the

(minimum <= value <= maximum)

invariant is true
before calling the

next

,

previous

, or

setValue

methods.

This method fires a

ChangeEvent

if the value has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Number

for this sequence
**Throws:** IllegalArgumentException

- if

value

is

null

or not a

Number
**See Also:** getNumber()

,

getValue()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

Constructor Detail

- SpinnerNumberModel

```java
public SpinnerNumberModel​(
Number
value,

Comparable
<?> minimum,

Comparable
<?> maximum,

Number
stepSize)
```

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

. The

nextValue

and

previousValue

methods
compute elements of the sequence by adding or subtracting

stepSize

respectively. All of the parameters
must be mutually

Comparable

,

value

and

stepSize

must be instances of

Integer

Long

,

Float

, or

Double

.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** minimum

- the first number in the sequence or

null
**Parameters:** maximum

- the last number in the sequence or

null
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if stepSize or value is

null

or if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel​(int value,
int minimum,
int maximum,
int stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel​(double value,
double minimum,
double maximum,
double stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

- SpinnerNumberModel

```java
public SpinnerNumberModel()
```

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

---

#### Constructor Detail

SpinnerNumberModel

```java
public SpinnerNumberModel​(
Number
value,

Comparable
<?> minimum,

Comparable
<?> maximum,

Number
stepSize)
```

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

. The

nextValue

and

previousValue

methods
compute elements of the sequence by adding or subtracting

stepSize

respectively. All of the parameters
must be mutually

Comparable

,

value

and

stepSize

must be instances of

Integer

Long

,

Float

, or

Double

.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

**Parameters:** value

- the current (non

null

) value of the model
**Parameters:** minimum

- the first number in the sequence or

null
**Parameters:** maximum

- the last number in the sequence or

null
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if stepSize or value is

null

or if the following expression is false:

minimum <= value <= maximum

---

#### SpinnerNumberModel

public SpinnerNumberModel​(

Number

value,

Comparable

<?> minimum,

Comparable

<?> maximum,

Number

stepSize)

Constructs a

SpinnerModel

that represents
a closed sequence of
numbers from

minimum

to

maximum

. The

nextValue

and

previousValue

methods
compute elements of the sequence by adding or subtracting

stepSize

respectively. All of the parameters
must be mutually

Comparable

,

value

and

stepSize

must be instances of

Integer

Long

,

Float

, or

Double

.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

The

minimum

and

maximum

parameters
can be

null

to indicate that the range doesn't
have an upper or lower bound.
If

value

or

stepSize

is

null

,
or if both

minimum

and

maximum

are specified and

minimum > maximum

then an

IllegalArgumentException

is thrown.
Similarly if

(minimum <= value <= maximum

) is false,
an

IllegalArgumentException

is thrown.

SpinnerNumberModel

```java
public SpinnerNumberModel​(int value,
int minimum,
int maximum,
int stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

---

#### SpinnerNumberModel

public SpinnerNumberModel​(int value,
int minimum,
int maximum,
int stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

```java
public SpinnerNumberModel​(double value,
double minimum,
double maximum,
double stepSize)
```

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

**Parameters:** value

- the current value of the model
**Parameters:** minimum

- the first number in the sequence
**Parameters:** maximum

- the last number in the sequence
**Parameters:** stepSize

- the difference between elements of the sequence
**Throws:** IllegalArgumentException

- if the following expression is false:

minimum <= value <= maximum

---

#### SpinnerNumberModel

public SpinnerNumberModel​(double value,
double minimum,
double maximum,
double stepSize)

Constructs a

SpinnerNumberModel

with the specified

value

,

minimum

/

maximum

bounds,
and

stepSize

.

SpinnerNumberModel

```java
public SpinnerNumberModel()
```

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

---

#### SpinnerNumberModel

public SpinnerNumberModel()

Constructs a

SpinnerNumberModel

with no

minimum

or

maximum

value,

stepSize

equal to one, and an initial value of zero.

Method Detail

- setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Changes the lower bound for numbers in this sequence.
If

minimum

is

null

,
then there is no lower bound. No bounds checking is done here;
the new

minimum

value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

getNextValue

,

getPreviousValue

, or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

**Parameters:** minimum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMinimum()

,

setMaximum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the first number in this sequence.

**Returns:** the value of the

minimum

property
**See Also:** setMinimum(java.lang.Comparable<?>)

- setMaximum

```java
public void setMaximum​(
Comparable
<?> maximum)
```

Changes the upper bound for numbers in this sequence.
If

maximum

is

null

, then there
is no upper bound. No bounds checking is done here; the new

maximum

value may invalidate the

(minimum <= value < maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

next

,

previous

,
or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

**Parameters:** maximum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMaximum()

,

setMinimum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the last number in the sequence.

**Returns:** the value of the

maximum

property
**See Also:** setMaximum(java.lang.Comparable<?>)

- setStepSize

```java
public void setStepSize​(
Number
stepSize)
```

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods. An

IllegalArgumentException

is thrown if

stepSize

is

null

.

This method fires a

ChangeEvent

if the

stepSize

has changed.

**Parameters:** stepSize

- the size of the value change computed by the

getNextValue

and

getPreviousValue

methods
**See Also:** getNextValue()

,

getPreviousValue()

,

getStepSize()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

- getStepSize

```java
public
Number
getStepSize()
```

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

**Returns:** the value of the

stepSize

property
**See Also:** setStepSize(java.lang.Number)

- getNextValue

```java
public
Object
getNextValue()
```

Returns the next number in the sequence.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** value + stepSize

or

null

if the sum
exceeds

maximum

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setStepSize(java.lang.Number)

- getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous number in the sequence.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** value - stepSize

, or

null

if the sum is less
than

minimum

.
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setStepSize(java.lang.Number)

- getNumber

```java
public
Number
getNumber()
```

Returns the value of the current element of the sequence.

**Returns:** the value property
**See Also:** setValue(java.lang.Object)

- getValue

```java
public
Object
getValue()
```

Returns the value of the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the value property
**See Also:** setValue(java.lang.Object)

,

getNumber()

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for this sequence. If

value

is

null

, or not a

Number

, an

IllegalArgumentException

is thrown. No
bounds checking is done here; the new value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. It's also possible to set
the value to be something that wouldn't naturally occur in the sequence,
i.e. a value that's not modulo the

stepSize

.
This is to simplify updating the model, and to accommodate
spinners that don't want to restrict values that have been
directly entered by the user. Naturally, one should ensure that the

(minimum <= value <= maximum)

invariant is true
before calling the

next

,

previous

, or

setValue

methods.

This method fires a

ChangeEvent

if the value has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Number

for this sequence
**Throws:** IllegalArgumentException

- if

value

is

null

or not a

Number
**See Also:** getNumber()

,

getValue()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### Method Detail

setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Changes the lower bound for numbers in this sequence.
If

minimum

is

null

,
then there is no lower bound. No bounds checking is done here;
the new

minimum

value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

getNextValue

,

getPreviousValue

, or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

**Parameters:** minimum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMinimum()

,

setMaximum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setMinimum

public void setMinimum​(

Comparable

<?> minimum)

Changes the lower bound for numbers in this sequence.
If

minimum

is

null

,
then there is no lower bound. No bounds checking is done here;
the new

minimum

value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

getNextValue

,

getPreviousValue

, or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
For example if value was a

Long

,

minimum

might be a Date subclass defined like this:

```java
MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}
```

This method fires a

ChangeEvent

if the

minimum

has changed.

MyDate extends Date { // Date already implements Comparable
public int compareTo(Long o) {
long t = getTime();
return (t < o.longValue() ? -1 : (t == o.longValue() ? 0 : 1));
}
}

This method fires a

ChangeEvent

if the

minimum

has changed.

getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the first number in this sequence.

**Returns:** the value of the

minimum

property
**See Also:** setMinimum(java.lang.Comparable<?>)

---

#### getMinimum

public

Comparable

<?> getMinimum()

Returns the first number in this sequence.

setMaximum

```java
public void setMaximum​(
Comparable
<?> maximum)
```

Changes the upper bound for numbers in this sequence.
If

maximum

is

null

, then there
is no upper bound. No bounds checking is done here; the new

maximum

value may invalidate the

(minimum <= value < maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

next

,

previous

,
or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

**Parameters:** maximum

- a

Comparable

that has a

compareTo

method for

Number

s with
the same type as

value
**See Also:** getMaximum()

,

setMinimum(java.lang.Comparable<?>)

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setMaximum

public void setMaximum​(

Comparable

<?> maximum)

Changes the upper bound for numbers in this sequence.
If

maximum

is

null

, then there
is no upper bound. No bounds checking is done here; the new

maximum

value may invalidate the

(minimum <= value < maximum)

invariant enforced by the constructors. This is to simplify updating
the model, naturally one should ensure that the invariant is true
before calling the

next

,

previous

,
or

setValue

methods.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

Typically this property is a

Number

of the same type
as the

value

however it's possible to use any

Comparable

with a

compareTo

method for a

Number

with the same type as the value.
See

setMinimum(Comparable)

for an example.

This method fires a

ChangeEvent

if the

maximum

has changed.

This method fires a

ChangeEvent

if the

maximum

has changed.

getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the last number in the sequence.

**Returns:** the value of the

maximum

property
**See Also:** setMaximum(java.lang.Comparable<?>)

---

#### getMaximum

public

Comparable

<?> getMaximum()

Returns the last number in the sequence.

setStepSize

```java
public void setStepSize​(
Number
stepSize)
```

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods. An

IllegalArgumentException

is thrown if

stepSize

is

null

.

This method fires a

ChangeEvent

if the

stepSize

has changed.

**Parameters:** stepSize

- the size of the value change computed by the

getNextValue

and

getPreviousValue

methods
**See Also:** getNextValue()

,

getPreviousValue()

,

getStepSize()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setStepSize

public void setStepSize​(

Number

stepSize)

Changes the size of the value change computed by the

getNextValue

and

getPreviousValue

methods. An

IllegalArgumentException

is thrown if

stepSize

is

null

.

This method fires a

ChangeEvent

if the

stepSize

has changed.

This method fires a

ChangeEvent

if the

stepSize

has changed.

getStepSize

```java
public
Number
getStepSize()
```

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

**Returns:** the value of the

stepSize

property
**See Also:** setStepSize(java.lang.Number)

---

#### getStepSize

public

Number

getStepSize()

Returns the size of the value change computed by the

getNextValue

and

getPreviousValue

methods.

getNextValue

```java
public
Object
getNextValue()
```

Returns the next number in the sequence.

**Specified by:** getNextValue

in interface

SpinnerModel
**Returns:** value + stepSize

or

null

if the sum
exceeds

maximum

.
**See Also:** SpinnerModel.getNextValue()

,

getPreviousValue()

,

setStepSize(java.lang.Number)

---

#### getNextValue

public

Object

getNextValue()

Returns the next number in the sequence.

getPreviousValue

```java
public
Object
getPreviousValue()
```

Returns the previous number in the sequence.

**Specified by:** getPreviousValue

in interface

SpinnerModel
**Returns:** value - stepSize

, or

null

if the sum is less
than

minimum

.
**See Also:** SpinnerModel.getPreviousValue()

,

getNextValue()

,

setStepSize(java.lang.Number)

---

#### getPreviousValue

public

Object

getPreviousValue()

Returns the previous number in the sequence.

getNumber

```java
public
Number
getNumber()
```

Returns the value of the current element of the sequence.

**Returns:** the value property
**See Also:** setValue(java.lang.Object)

---

#### getNumber

public

Number

getNumber()

Returns the value of the current element of the sequence.

getValue

```java
public
Object
getValue()
```

Returns the value of the current element of the sequence.

**Specified by:** getValue

in interface

SpinnerModel
**Returns:** the value property
**See Also:** setValue(java.lang.Object)

,

getNumber()

---

#### getValue

public

Object

getValue()

Returns the value of the current element of the sequence.

setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for this sequence. If

value

is

null

, or not a

Number

, an

IllegalArgumentException

is thrown. No
bounds checking is done here; the new value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. It's also possible to set
the value to be something that wouldn't naturally occur in the sequence,
i.e. a value that's not modulo the

stepSize

.
This is to simplify updating the model, and to accommodate
spinners that don't want to restrict values that have been
directly entered by the user. Naturally, one should ensure that the

(minimum <= value <= maximum)

invariant is true
before calling the

next

,

previous

, or

setValue

methods.

This method fires a

ChangeEvent

if the value has changed.

**Specified by:** setValue

in interface

SpinnerModel
**Parameters:** value

- the current (non

null

)

Number

for this sequence
**Throws:** IllegalArgumentException

- if

value

is

null

or not a

Number
**See Also:** getNumber()

,

getValue()

,

SpinnerModel.addChangeListener(javax.swing.event.ChangeListener)

---

#### setValue

public void setValue​(

Object

value)

Sets the current value for this sequence. If

value

is

null

, or not a

Number

, an

IllegalArgumentException

is thrown. No
bounds checking is done here; the new value may invalidate the

(minimum <= value <= maximum)

invariant enforced by the constructors. It's also possible to set
the value to be something that wouldn't naturally occur in the sequence,
i.e. a value that's not modulo the

stepSize

.
This is to simplify updating the model, and to accommodate
spinners that don't want to restrict values that have been
directly entered by the user. Naturally, one should ensure that the

(minimum <= value <= maximum)

invariant is true
before calling the

next

,

previous

, or

setValue

methods.

This method fires a

ChangeEvent

if the value has changed.

This method fires a

ChangeEvent

if the value has changed.

---

