# Class ButtonGroup

**Source:** `java.desktop\javax\swing\ButtonGroup.html`

### Class Description

```java
public class
ButtonGroup

extends
Object

implements
Serializable
```

This class is used to create a multiple-exclusion scope for
a set of buttons. Creating a set of buttons with the
same

ButtonGroup

object means that
turning "on" one of those buttons
turns off all other buttons in the group.

A

ButtonGroup

can be used with
any set of objects that inherit from

AbstractButton

.
Typically a button group contains instances of

JRadioButton

,

JRadioButtonMenuItem

,
or

JToggleButton

.
It wouldn't make sense to put an instance of

JButton

or

JMenuItem

in a button group
because

JButton

and

JMenuItem

don't implement the selected state.

Initially, all buttons in the group are unselected.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Vector
<
AbstractButton
> buttons

The list of buttons participating in this group.

---

### Constructor Details

#### public ButtonGroup()

Creates a new

ButtonGroup

.

---

### Method Details

#### public void add​(
AbstractButton
b)

Adds the button to the group.

**Parameters:**
- b

- the button to be added

---

#### public void remove​(
AbstractButton
b)

Removes the button from the group.

**Parameters:**
- b

- the button to be removed

---

#### public void clearSelection()

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

**Since:**
- 1.6

---

#### public
Enumeration
<
AbstractButton
> getElements()

Returns all the buttons that are participating in
this group.

**Returns:**
- an

Enumeration

of the buttons in this group

---

#### public
ButtonModel
getSelection()

Returns the model of the selected button.

**Returns:**
- the selected button model

---

#### public void setSelected​(
ButtonModel
m,
boolean b)

Sets the selected value for the

ButtonModel

.
Only one button in the group may be selected at a time.

**Parameters:**
- m

- the

ButtonModel
- b

-

true

if this button is to be
selected, otherwise

false

---

#### public boolean isSelected​(
ButtonModel
m)

Returns whether a

ButtonModel

is selected.

**Parameters:**
- m

- an isntance of

ButtonModel

**Returns:**
- true

if the button is selected,
otherwise returns

false

---

#### public int getButtonCount()

Returns the number of buttons in the group.

**Returns:**
- the button count

**Since:**
- 1.3

---

### Additional Sections

#### Class ButtonGroup

java.lang.Object

- javax.swing.ButtonGroup

javax.swing.ButtonGroup

**All Implemented Interfaces:** Serializable

```java
public class
ButtonGroup

extends
Object

implements
Serializable
```

This class is used to create a multiple-exclusion scope for
a set of buttons. Creating a set of buttons with the
same

ButtonGroup

object means that
turning "on" one of those buttons
turns off all other buttons in the group.

A

ButtonGroup

can be used with
any set of objects that inherit from

AbstractButton

.
Typically a button group contains instances of

JRadioButton

,

JRadioButtonMenuItem

,
or

JToggleButton

.
It wouldn't make sense to put an instance of

JButton

or

JMenuItem

in a button group
because

JButton

and

JMenuItem

don't implement the selected state.

Initially, all buttons in the group are unselected.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** Serialized Form

public class

ButtonGroup

extends

Object

implements

Serializable

This class is used to create a multiple-exclusion scope for
a set of buttons. Creating a set of buttons with the
same

ButtonGroup

object means that
turning "on" one of those buttons
turns off all other buttons in the group.

A

ButtonGroup

can be used with
any set of objects that inherit from

AbstractButton

.
Typically a button group contains instances of

JRadioButton

,

JRadioButtonMenuItem

,
or

JToggleButton

.
It wouldn't make sense to put an instance of

JButton

or

JMenuItem

in a button group
because

JButton

and

JMenuItem

don't implement the selected state.

Initially, all buttons in the group are unselected.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

A

ButtonGroup

can be used with
any set of objects that inherit from

AbstractButton

.
Typically a button group contains instances of

JRadioButton

,

JRadioButtonMenuItem

,
or

JToggleButton

.
It wouldn't make sense to put an instance of

JButton

or

JMenuItem

in a button group
because

JButton

and

JMenuItem

don't implement the selected state.

Initially, all buttons in the group are unselected.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Initially, all buttons in the group are unselected.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

For examples and further information on using button groups see

How to Use Radio Buttons

,
a section in

The Java Tutorial

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

AbstractButton

>

buttons

The list of buttons participating in this group.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ButtonGroup

()

Creates a new

ButtonGroup

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

AbstractButton

b)

Adds the button to the group.

void

clearSelection

()

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

int

getButtonCount

()

Returns the number of buttons in the group.

Enumeration

<

AbstractButton

>

getElements

()

Returns all the buttons that are participating in
this group.

ButtonModel

getSelection

()

Returns the model of the selected button.

boolean

isSelected

​(

ButtonModel

m)

Returns whether a

ButtonModel

is selected.

void

remove

​(

AbstractButton

b)

Removes the button from the group.

void

setSelected

​(

ButtonModel

m,
boolean b)

Sets the selected value for the

ButtonModel

.

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

Fields

Modifier and Type

Field

Description

protected

Vector

<

AbstractButton

>

buttons

The list of buttons participating in this group.

---

#### Field Summary

The list of buttons participating in this group.

Constructor Summary

Constructors

Constructor

Description

ButtonGroup

()

Creates a new

ButtonGroup

.

---

#### Constructor Summary

Creates a new

ButtonGroup

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

AbstractButton

b)

Adds the button to the group.

void

clearSelection

()

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

int

getButtonCount

()

Returns the number of buttons in the group.

Enumeration

<

AbstractButton

>

getElements

()

Returns all the buttons that are participating in
this group.

ButtonModel

getSelection

()

Returns the model of the selected button.

boolean

isSelected

​(

ButtonModel

m)

Returns whether a

ButtonModel

is selected.

void

remove

​(

AbstractButton

b)

Removes the button from the group.

void

setSelected

​(

ButtonModel

m,
boolean b)

Sets the selected value for the

ButtonModel

.

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

Adds the button to the group.

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

Returns the number of buttons in the group.

Returns all the buttons that are participating in
this group.

Returns the model of the selected button.

Returns whether a

ButtonModel

is selected.

Removes the button from the group.

Sets the selected value for the

ButtonModel

.

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

============ FIELD DETAIL ===========

- Field Detail

- buttons

```java
protected
Vector
<
AbstractButton
> buttons
```

The list of buttons participating in this group.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ButtonGroup

```java
public ButtonGroup()
```

Creates a new

ButtonGroup

.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public void add​(
AbstractButton
b)
```

Adds the button to the group.

**Parameters:** b

- the button to be added

- remove

```java
public void remove​(
AbstractButton
b)
```

Removes the button from the group.

**Parameters:** b

- the button to be removed

- clearSelection

```java
public void clearSelection()
```

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

**Since:** 1.6

- getElements

```java
public
Enumeration
<
AbstractButton
> getElements()
```

Returns all the buttons that are participating in
this group.

**Returns:** an

Enumeration

of the buttons in this group

- getSelection

```java
public
ButtonModel
getSelection()
```

Returns the model of the selected button.

**Returns:** the selected button model

- setSelected

```java
public void setSelected​(
ButtonModel
m,
boolean b)
```

Sets the selected value for the

ButtonModel

.
Only one button in the group may be selected at a time.

**Parameters:** m

- the

ButtonModel
**Parameters:** b

-

true

if this button is to be
selected, otherwise

false

- isSelected

```java
public boolean isSelected​(
ButtonModel
m)
```

Returns whether a

ButtonModel

is selected.

**Parameters:** m

- an isntance of

ButtonModel
**Returns:** true

if the button is selected,
otherwise returns

false

- getButtonCount

```java
public int getButtonCount()
```

Returns the number of buttons in the group.

**Returns:** the button count
**Since:** 1.3

Field Detail

- buttons

```java
protected
Vector
<
AbstractButton
> buttons
```

The list of buttons participating in this group.

---

#### Field Detail

buttons

```java
protected
Vector
<
AbstractButton
> buttons
```

The list of buttons participating in this group.

---

#### buttons

protected

Vector

<

AbstractButton

> buttons

The list of buttons participating in this group.

Constructor Detail

- ButtonGroup

```java
public ButtonGroup()
```

Creates a new

ButtonGroup

.

---

#### Constructor Detail

ButtonGroup

```java
public ButtonGroup()
```

Creates a new

ButtonGroup

.

---

#### ButtonGroup

public ButtonGroup()

Creates a new

ButtonGroup

.

Method Detail

- add

```java
public void add​(
AbstractButton
b)
```

Adds the button to the group.

**Parameters:** b

- the button to be added

- remove

```java
public void remove​(
AbstractButton
b)
```

Removes the button from the group.

**Parameters:** b

- the button to be removed

- clearSelection

```java
public void clearSelection()
```

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

**Since:** 1.6

- getElements

```java
public
Enumeration
<
AbstractButton
> getElements()
```

Returns all the buttons that are participating in
this group.

**Returns:** an

Enumeration

of the buttons in this group

- getSelection

```java
public
ButtonModel
getSelection()
```

Returns the model of the selected button.

**Returns:** the selected button model

- setSelected

```java
public void setSelected​(
ButtonModel
m,
boolean b)
```

Sets the selected value for the

ButtonModel

.
Only one button in the group may be selected at a time.

**Parameters:** m

- the

ButtonModel
**Parameters:** b

-

true

if this button is to be
selected, otherwise

false

- isSelected

```java
public boolean isSelected​(
ButtonModel
m)
```

Returns whether a

ButtonModel

is selected.

**Parameters:** m

- an isntance of

ButtonModel
**Returns:** true

if the button is selected,
otherwise returns

false

- getButtonCount

```java
public int getButtonCount()
```

Returns the number of buttons in the group.

**Returns:** the button count
**Since:** 1.3

---

#### Method Detail

add

```java
public void add​(
AbstractButton
b)
```

Adds the button to the group.

**Parameters:** b

- the button to be added

---

#### add

public void add​(

AbstractButton

b)

Adds the button to the group.

remove

```java
public void remove​(
AbstractButton
b)
```

Removes the button from the group.

**Parameters:** b

- the button to be removed

---

#### remove

public void remove​(

AbstractButton

b)

Removes the button from the group.

clearSelection

```java
public void clearSelection()
```

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

**Since:** 1.6

---

#### clearSelection

public void clearSelection()

Clears the selection such that none of the buttons
in the

ButtonGroup

are selected.

getElements

```java
public
Enumeration
<
AbstractButton
> getElements()
```

Returns all the buttons that are participating in
this group.

**Returns:** an

Enumeration

of the buttons in this group

---

#### getElements

public

Enumeration

<

AbstractButton

> getElements()

Returns all the buttons that are participating in
this group.

getSelection

```java
public
ButtonModel
getSelection()
```

Returns the model of the selected button.

**Returns:** the selected button model

---

#### getSelection

public

ButtonModel

getSelection()

Returns the model of the selected button.

setSelected

```java
public void setSelected​(
ButtonModel
m,
boolean b)
```

Sets the selected value for the

ButtonModel

.
Only one button in the group may be selected at a time.

**Parameters:** m

- the

ButtonModel
**Parameters:** b

-

true

if this button is to be
selected, otherwise

false

---

#### setSelected

public void setSelected​(

ButtonModel

m,
boolean b)

Sets the selected value for the

ButtonModel

.
Only one button in the group may be selected at a time.

isSelected

```java
public boolean isSelected​(
ButtonModel
m)
```

Returns whether a

ButtonModel

is selected.

**Parameters:** m

- an isntance of

ButtonModel
**Returns:** true

if the button is selected,
otherwise returns

false

---

#### isSelected

public boolean isSelected​(

ButtonModel

m)

Returns whether a

ButtonModel

is selected.

getButtonCount

```java
public int getButtonCount()
```

Returns the number of buttons in the group.

**Returns:** the button count
**Since:** 1.3

---

#### getButtonCount

public int getButtonCount()

Returns the number of buttons in the group.

---

