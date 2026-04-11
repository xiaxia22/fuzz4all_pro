# Interface SpinnerModel

**Source:** `java.desktop\javax\swing\SpinnerModel.html`

### Class Description

```java
public interface
SpinnerModel
```

A model for a potentially unbounded sequence of object values. This model
is similar to

ListModel

however there are some important differences:

- The number of sequence elements isn't necessarily bounded.

The model doesn't support indexed random access to sequence elements.
Only three sequence values are accessible at a time: current, next and
previous.

The current sequence element, can be set.

A

SpinnerModel

has three properties, only the first is read/write.

When the

value

property changes,

ChangeListeners

are notified.

SpinnerModel

may
choose to notify the

ChangeListeners

under other circumstances.

**All Known Implementing Classes:** AbstractSpinnerModel

,

SpinnerDateModel

,

SpinnerListModel

,

SpinnerNumberModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getValue()

The

current element

of the sequence. This element is usually
displayed by the

editor

part of a

JSpinner

.

**Returns:**
- the current spinner value.

**See Also:**
- setValue(java.lang.Object)

---

#### void setValue​(
Object
value)

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.
If the

SpinnerModel

implementation doesn't support
the specified value then an

IllegalArgumentException

is thrown. For example a

SpinnerModel

for numbers might
only support values that are integer multiples of ten. In
that case,

model.setValue(new Number(11))

would throw an exception.

**Parameters:**
- value

- new value for the spinner

**Throws:**
- IllegalArgumentException

- if

value

isn't allowed

**See Also:**
- getValue()

---

#### Object
getNextValue()

Return the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return null. Calling this method does not effect

value

.

**Returns:**
- the next legal value or null if one doesn't exist

**See Also:**
- getValue()

,

getPreviousValue()

---

#### Object
getPreviousValue()

Return the object in the sequence that comes before the object returned
by

getValue()

. If the end of the sequence has been reached then
return null. Calling this method does not effect

value

.

**Returns:**
- the previous legal value or null if one doesn't exist

**See Also:**
- getValue()

,

getNextValue()

---

#### void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to the model's listener list. The

ChangeListeners

must be notified when models

value

changes.

**Parameters:**
- l

- the ChangeListener to add

**See Also:**
- removeChangeListener(javax.swing.event.ChangeListener)

---

#### void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from the model's listener list.

**Parameters:**
- l

- the ChangeListener to remove

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

---

### Additional Sections

#### Interface SpinnerModel

**All Known Implementing Classes:** AbstractSpinnerModel

,

SpinnerDateModel

,

SpinnerListModel

,

SpinnerNumberModel

```java
public interface
SpinnerModel
```

A model for a potentially unbounded sequence of object values. This model
is similar to

ListModel

however there are some important differences:

- The number of sequence elements isn't necessarily bounded.

The model doesn't support indexed random access to sequence elements.
Only three sequence values are accessible at a time: current, next and
previous.

The current sequence element, can be set.

A

SpinnerModel

has three properties, only the first is read/write.

When the

value

property changes,

ChangeListeners

are notified.

SpinnerModel

may
choose to notify the

ChangeListeners

under other circumstances.

**Since:** 1.4
**See Also:** JSpinner

,

AbstractSpinnerModel

,

SpinnerListModel

,

SpinnerNumberModel

,

SpinnerDateModel

public interface

SpinnerModel

A model for a potentially unbounded sequence of object values. This model
is similar to

ListModel

however there are some important differences:

- The number of sequence elements isn't necessarily bounded.

The model doesn't support indexed random access to sequence elements.
Only three sequence values are accessible at a time: current, next and
previous.

The current sequence element, can be set.

A

SpinnerModel

has three properties, only the first is read/write.

When the

value

property changes,

ChangeListeners

are notified.

SpinnerModel

may
choose to notify the

ChangeListeners

under other circumstances.

The number of sequence elements isn't necessarily bounded.

The model doesn't support indexed random access to sequence elements.
Only three sequence values are accessible at a time: current, next and
previous.

The current sequence element, can be set.

A

SpinnerModel

has three properties, only the first is read/write.

When the

value

property changes,

ChangeListeners

are notified.

SpinnerModel

may
choose to notify the

ChangeListeners

under other circumstances.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the model's listener list.

Object

getNextValue

()

Return the object in the sequence that comes after the object returned
by

getValue()

.

Object

getPreviousValue

()

Return the object in the sequence that comes before the object returned
by

getValue()

.

Object

getValue

()

The

current element

of the sequence.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model's listener list.

void

setValue

​(

Object

value)

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the model's listener list.

Object

getNextValue

()

Return the object in the sequence that comes after the object returned
by

getValue()

.

Object

getPreviousValue

()

Return the object in the sequence that comes before the object returned
by

getValue()

.

Object

getValue

()

The

current element

of the sequence.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model's listener list.

void

setValue

​(

Object

value)

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.

---

#### Method Summary

Adds a

ChangeListener

to the model's listener list.

Return the object in the sequence that comes after the object returned
by

getValue()

.

Return the object in the sequence that comes before the object returned
by

getValue()

.

The

current element

of the sequence.

Removes a

ChangeListener

from the model's listener list.

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
Object
getValue()
```

The

current element

of the sequence. This element is usually
displayed by the

editor

part of a

JSpinner

.

**Returns:** the current spinner value.
**See Also:** setValue(java.lang.Object)

- setValue

```java
void setValue​(
Object
value)
```

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.
If the

SpinnerModel

implementation doesn't support
the specified value then an

IllegalArgumentException

is thrown. For example a

SpinnerModel

for numbers might
only support values that are integer multiples of ten. In
that case,

model.setValue(new Number(11))

would throw an exception.

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

- getNextValue

```java
Object
getNextValue()
```

Return the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return null. Calling this method does not effect

value

.

**Returns:** the next legal value or null if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

- getPreviousValue

```java
Object
getPreviousValue()
```

Return the object in the sequence that comes before the object returned
by

getValue()

. If the end of the sequence has been reached then
return null. Calling this method does not effect

value

.

**Returns:** the previous legal value or null if one doesn't exist
**See Also:** getValue()

,

getNextValue()

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model's listener list. The

ChangeListeners

must be notified when models

value

changes.

**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model's listener list.

**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

Method Detail

- getValue

```java
Object
getValue()
```

The

current element

of the sequence. This element is usually
displayed by the

editor

part of a

JSpinner

.

**Returns:** the current spinner value.
**See Also:** setValue(java.lang.Object)

- setValue

```java
void setValue​(
Object
value)
```

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.
If the

SpinnerModel

implementation doesn't support
the specified value then an

IllegalArgumentException

is thrown. For example a

SpinnerModel

for numbers might
only support values that are integer multiples of ten. In
that case,

model.setValue(new Number(11))

would throw an exception.

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

- getNextValue

```java
Object
getNextValue()
```

Return the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return null. Calling this method does not effect

value

.

**Returns:** the next legal value or null if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

- getPreviousValue

```java
Object
getPreviousValue()
```

Return the object in the sequence that comes before the object returned
by

getValue()

. If the end of the sequence has been reached then
return null. Calling this method does not effect

value

.

**Returns:** the previous legal value or null if one doesn't exist
**See Also:** getValue()

,

getNextValue()

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model's listener list. The

ChangeListeners

must be notified when models

value

changes.

**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model's listener list.

**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

---

#### Method Detail

getValue

```java
Object
getValue()
```

The

current element

of the sequence. This element is usually
displayed by the

editor

part of a

JSpinner

.

**Returns:** the current spinner value.
**See Also:** setValue(java.lang.Object)

---

#### getValue

Object

getValue()

The

current element

of the sequence. This element is usually
displayed by the

editor

part of a

JSpinner

.

setValue

```java
void setValue​(
Object
value)
```

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.
If the

SpinnerModel

implementation doesn't support
the specified value then an

IllegalArgumentException

is thrown. For example a

SpinnerModel

for numbers might
only support values that are integer multiples of ten. In
that case,

model.setValue(new Number(11))

would throw an exception.

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

---

#### setValue

void setValue​(

Object

value)

Changes current value of the model, typically this value is displayed
by the

editor

part of a

JSpinner

.
If the

SpinnerModel

implementation doesn't support
the specified value then an

IllegalArgumentException

is thrown. For example a

SpinnerModel

for numbers might
only support values that are integer multiples of ten. In
that case,

model.setValue(new Number(11))

would throw an exception.

getNextValue

```java
Object
getNextValue()
```

Return the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return null. Calling this method does not effect

value

.

**Returns:** the next legal value or null if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

---

#### getNextValue

Object

getNextValue()

Return the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return null. Calling this method does not effect

value

.

getPreviousValue

```java
Object
getPreviousValue()
```

Return the object in the sequence that comes before the object returned
by

getValue()

. If the end of the sequence has been reached then
return null. Calling this method does not effect

value

.

**Returns:** the previous legal value or null if one doesn't exist
**See Also:** getValue()

,

getNextValue()

---

#### getPreviousValue

Object

getPreviousValue()

Return the object in the sequence that comes before the object returned
by

getValue()

. If the end of the sequence has been reached then
return null. Calling this method does not effect

value

.

addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model's listener list. The

ChangeListeners

must be notified when models

value

changes.

**Parameters:** l

- the ChangeListener to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to the model's listener list. The

ChangeListeners

must be notified when models

value

changes.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model's listener list.

**Parameters:** l

- the ChangeListener to remove
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from the model's listener list.

---

