# Class DefaultButtonModel

**Source:** `java.desktop\javax\swing\DefaultButtonModel.html`

### Class Description

```java
public class
DefaultButtonModel

extends
Object

implements
ButtonModel
,
Serializable
```

The default implementation of a

Button

component's data model.

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

**All Implemented Interfaces:** ItemSelectable

,

Serializable

,

ButtonModel

---

### Field Details

#### protected int stateMask

The bitmask used to store the state of the button.

---

#### protected
String
actionCommand

The action command string fired by the button.

---

#### protected
ButtonGroup
group

The button group that the button belongs to.

---

#### protected int mnemonic

The button's mnemonic.

---

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.
The source of events generated is always "this".

---

#### protected
EventListenerList
listenerList

Stores the listeners on this model.

---

#### public static final int ARMED

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

**See Also:**
- Constant Field Values

---

#### public static final int SELECTED

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected. Only needed for
certain types of buttons - such as radio button or check box.

**See Also:**
- Constant Field Values

---

#### public static final int PRESSED

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

**See Also:**
- Constant Field Values

---

#### public static final int ENABLED

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

**See Also:**
- Constant Field Values

---

#### public static final int ROLLOVER

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DefaultButtonModel()

Constructs a

DefaultButtonModel

.

---

### Method Details

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

**Returns:**
- all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered

**See Also:**
- ButtonModel.addChangeListener(javax.swing.event.ChangeListener)

,

ButtonModel.removeChangeListener(javax.swing.event.ChangeListener)

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:**
- EventListenerList

---

#### public
ActionListener
[] getActionListeners()

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

**Returns:**
- all of this model's

ActionListener

s
or an empty
array if no action listeners are currently registered

**See Also:**
- ButtonModel.addActionListener(java.awt.event.ActionListener)

,

ButtonModel.removeActionListener(java.awt.event.ActionListener)

**Since:**
- 1.4

---

#### protected void fireActionPerformed​(
ActionEvent
e)

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:**
- e

- the

ActionEvent

to deliver to listeners

**See Also:**
- EventListenerList

---

#### public
ItemListener
[] getItemListeners()

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

**Returns:**
- all of this model's

ItemListener

s
or an empty
array if no item listeners are currently registered

**See Also:**
- ButtonModel.addItemListener(java.awt.event.ItemListener)

,

ButtonModel.removeItemListener(java.awt.event.ItemListener)

**Since:**
- 1.4

---

#### protected void fireItemStateChanged​(
ItemEvent
e)

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:**
- e

- the

ItemEvent

to deliver to listeners

**See Also:**
- EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener

**See Also:**
- getActionListeners()

,

getChangeListeners()

,

getItemListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of requested listeners

---

#### public
Object
[] getSelectedObjects()

Overridden to return

null

.

**Specified by:**
- getSelectedObjects

in interface

ItemSelectable

**Returns:**
- the list of selected objects, or

null

---

#### public
ButtonGroup
getGroup()

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Specified by:**
- getGroup

in interface

ButtonModel

**Returns:**
- the

ButtonGroup

that the button belongs to

**Since:**
- 1.3

---

### Additional Sections

#### Class DefaultButtonModel

java.lang.Object

- javax.swing.DefaultButtonModel

javax.swing.DefaultButtonModel

**All Implemented Interfaces:** ItemSelectable

,

Serializable

,

ButtonModel

**Direct Known Subclasses:** JToggleButton.ToggleButtonModel

```java
public class
DefaultButtonModel

extends
Object

implements
ButtonModel
,
Serializable
```

The default implementation of a

Button

component's data model.

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

DefaultButtonModel

extends

Object

implements

ButtonModel

,

Serializable

The default implementation of a

Button

component's data model.

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

String

actionCommand

The action command string fired by the button.

static int

ARMED

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.

static int

ENABLED

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

protected

ButtonGroup

group

The button group that the button belongs to.

protected

EventListenerList

listenerList

Stores the listeners on this model.

protected int

mnemonic

The button's mnemonic.

static int

PRESSED

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

static int

ROLLOVER

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

static int

SELECTED

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected.

protected int

stateMask

The bitmask used to store the state of the button.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultButtonModel

()

Constructs a

DefaultButtonModel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

fireActionPerformed

​(

ActionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

ButtonGroup

getGroup

()

Returns the group that the button belongs to.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Object

[]

getSelectedObjects

()

Overridden to return

null

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

- Methods declared in interface javax.swing.

ButtonModel

addActionListener

,

addChangeListener

,

addItemListener

,

getActionCommand

,

getMnemonic

,

isArmed

,

isEnabled

,

isPressed

,

isRollover

,

isSelected

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setActionCommand

,

setArmed

,

setEnabled

,

setGroup

,

setMnemonic

,

setPressed

,

setRollover

,

setSelected

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

actionCommand

The action command string fired by the button.

static int

ARMED

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.

static int

ENABLED

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

protected

ButtonGroup

group

The button group that the button belongs to.

protected

EventListenerList

listenerList

Stores the listeners on this model.

protected int

mnemonic

The button's mnemonic.

static int

PRESSED

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

static int

ROLLOVER

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

static int

SELECTED

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected.

protected int

stateMask

The bitmask used to store the state of the button.

---

#### Field Summary

The action command string fired by the button.

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

The button group that the button belongs to.

Stores the listeners on this model.

The button's mnemonic.

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected.

The bitmask used to store the state of the button.

Constructor Summary

Constructors

Constructor

Description

DefaultButtonModel

()

Constructs a

DefaultButtonModel

.

---

#### Constructor Summary

Constructs a

DefaultButtonModel

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

fireActionPerformed

​(

ActionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

ButtonGroup

getGroup

()

Returns the group that the button belongs to.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Object

[]

getSelectedObjects

()

Overridden to return

null

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

- Methods declared in interface javax.swing.

ButtonModel

addActionListener

,

addChangeListener

,

addItemListener

,

getActionCommand

,

getMnemonic

,

isArmed

,

isEnabled

,

isPressed

,

isRollover

,

isSelected

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setActionCommand

,

setArmed

,

setEnabled

,

setGroup

,

setMnemonic

,

setPressed

,

setRollover

,

setSelected

---

#### Method Summary

Notifies all listeners that have registered interest for
notification on this event type.

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

Returns the group that the button belongs to.

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Overridden to return

null

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

Methods declared in interface javax.swing.

ButtonModel

addActionListener

,

addChangeListener

,

addItemListener

,

getActionCommand

,

getMnemonic

,

isArmed

,

isEnabled

,

isPressed

,

isRollover

,

isSelected

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setActionCommand

,

setArmed

,

setEnabled

,

setGroup

,

setMnemonic

,

setPressed

,

setRollover

,

setSelected

---

#### Methods declared in interface javax.swing. ButtonModel

============ FIELD DETAIL ===========

- Field Detail

- stateMask

```java
protected int stateMask
```

The bitmask used to store the state of the button.

- actionCommand

```java
protected
String
actionCommand
```

The action command string fired by the button.

- group

```java
protected
ButtonGroup
group
```

The button group that the button belongs to.

- mnemonic

```java
protected int mnemonic
```

The button's mnemonic.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.
The source of events generated is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

Stores the listeners on this model.

- ARMED

```java
public static final int ARMED
```

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

**See Also:** Constant Field Values

- SELECTED

```java
public static final int SELECTED
```

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected. Only needed for
certain types of buttons - such as radio button or check box.

**See Also:** Constant Field Values

- PRESSED

```java
public static final int PRESSED
```

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

**See Also:** Constant Field Values

- ENABLED

```java
public static final int ENABLED
```

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

**See Also:** Constant Field Values

- ROLLOVER

```java
public static final int ROLLOVER
```

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultButtonModel

```java
public DefaultButtonModel()
```

Constructs a

DefaultButtonModel

.

============ METHOD DETAIL ==========

- Method Detail

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addChangeListener(javax.swing.event.ChangeListener)

,

ButtonModel.removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ActionListener

s
or an empty
array if no action listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addActionListener(java.awt.event.ActionListener)

,

ButtonModel.removeActionListener(java.awt.event.ActionListener)

- fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ActionEvent

to deliver to listeners
**See Also:** EventListenerList

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ItemListener

s
or an empty
array if no item listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addItemListener(java.awt.event.ItemListener)

,

ButtonModel.removeItemListener(java.awt.event.ItemListener)

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ItemEvent

to deliver to listeners
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getActionListeners()

,

getChangeListeners()

,

getItemListeners()

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Overridden to return

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null

- getGroup

```java
public
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Specified by:** getGroup

in interface

ButtonModel
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 1.3

Field Detail

- stateMask

```java
protected int stateMask
```

The bitmask used to store the state of the button.

- actionCommand

```java
protected
String
actionCommand
```

The action command string fired by the button.

- group

```java
protected
ButtonGroup
group
```

The button group that the button belongs to.

- mnemonic

```java
protected int mnemonic
```

The button's mnemonic.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.
The source of events generated is always "this".

- listenerList

```java
protected
EventListenerList
listenerList
```

Stores the listeners on this model.

- ARMED

```java
public static final int ARMED
```

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

**See Also:** Constant Field Values

- SELECTED

```java
public static final int SELECTED
```

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected. Only needed for
certain types of buttons - such as radio button or check box.

**See Also:** Constant Field Values

- PRESSED

```java
public static final int PRESSED
```

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

**See Also:** Constant Field Values

- ENABLED

```java
public static final int ENABLED
```

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

**See Also:** Constant Field Values

- ROLLOVER

```java
public static final int ROLLOVER
```

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

**See Also:** Constant Field Values

---

#### Field Detail

stateMask

```java
protected int stateMask
```

The bitmask used to store the state of the button.

---

#### stateMask

protected int stateMask

The bitmask used to store the state of the button.

actionCommand

```java
protected
String
actionCommand
```

The action command string fired by the button.

---

#### actionCommand

protected

String

actionCommand

The action command string fired by the button.

group

```java
protected
ButtonGroup
group
```

The button group that the button belongs to.

---

#### group

protected

ButtonGroup

group

The button group that the button belongs to.

mnemonic

```java
protected int mnemonic
```

The button's mnemonic.

---

#### mnemonic

protected int mnemonic

The button's mnemonic.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.
The source of events generated is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button model
instance since the event's only state is the source property.
The source of events generated is always "this".

listenerList

```java
protected
EventListenerList
listenerList
```

Stores the listeners on this model.

---

#### listenerList

protected

EventListenerList

listenerList

Stores the listeners on this model.

ARMED

```java
public static final int ARMED
```

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

**See Also:** Constant Field Values

---

#### ARMED

public static final int ARMED

Identifies the "armed" bit in the bitmask, which
indicates partial commitment towards choosing/triggering
the button.

SELECTED

```java
public static final int SELECTED
```

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected. Only needed for
certain types of buttons - such as radio button or check box.

**See Also:** Constant Field Values

---

#### SELECTED

public static final int SELECTED

Identifies the "selected" bit in the bitmask, which
indicates that the button has been selected. Only needed for
certain types of buttons - such as radio button or check box.

PRESSED

```java
public static final int PRESSED
```

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

**See Also:** Constant Field Values

---

#### PRESSED

public static final int PRESSED

Identifies the "pressed" bit in the bitmask, which
indicates that the button is pressed.

ENABLED

```java
public static final int ENABLED
```

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

**See Also:** Constant Field Values

---

#### ENABLED

public static final int ENABLED

Identifies the "enabled" bit in the bitmask, which
indicates that the button can be selected by
an input device (such as a mouse pointer).

ROLLOVER

```java
public static final int ROLLOVER
```

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

**See Also:** Constant Field Values

---

#### ROLLOVER

public static final int ROLLOVER

Identifies the "rollover" bit in the bitmask, which
indicates that the mouse is over the button.

Constructor Detail

- DefaultButtonModel

```java
public DefaultButtonModel()
```

Constructs a

DefaultButtonModel

.

---

#### Constructor Detail

DefaultButtonModel

```java
public DefaultButtonModel()
```

Constructs a

DefaultButtonModel

.

---

#### DefaultButtonModel

public DefaultButtonModel()

Constructs a

DefaultButtonModel

.

Method Detail

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addChangeListener(javax.swing.event.ChangeListener)

,

ButtonModel.removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ActionListener

s
or an empty
array if no action listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addActionListener(java.awt.event.ActionListener)

,

ButtonModel.removeActionListener(java.awt.event.ActionListener)

- fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ActionEvent

to deliver to listeners
**See Also:** EventListenerList

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ItemListener

s
or an empty
array if no item listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addItemListener(java.awt.event.ItemListener)

,

ButtonModel.removeItemListener(java.awt.event.ItemListener)

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ItemEvent

to deliver to listeners
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getActionListeners()

,

getChangeListeners()

,

getItemListeners()

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Overridden to return

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null

- getGroup

```java
public
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Specified by:** getGroup

in interface

ButtonModel
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 1.3

---

#### Method Detail

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addChangeListener(javax.swing.event.ChangeListener)

,

ButtonModel.removeChangeListener(javax.swing.event.ChangeListener)

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the change listeners
registered on this

DefaultButtonModel

.

fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is created lazily.

getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ActionListener

s
or an empty
array if no action listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addActionListener(java.awt.event.ActionListener)

,

ButtonModel.removeActionListener(java.awt.event.ActionListener)

---

#### getActionListeners

public

ActionListener

[] getActionListeners()

Returns an array of all the action listeners
registered on this

DefaultButtonModel

.

fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ActionEvent

to deliver to listeners
**See Also:** EventListenerList

---

#### fireActionPerformed

protected void fireActionPerformed​(

ActionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

**Returns:** all of this model's

ItemListener

s
or an empty
array if no item listeners are currently registered
**Since:** 1.4
**See Also:** ButtonModel.addItemListener(java.awt.event.ItemListener)

,

ButtonModel.removeItemListener(java.awt.event.ItemListener)

---

#### getItemListeners

public

ItemListener

[] getItemListeners()

Returns an array of all the item listeners
registered on this

DefaultButtonModel

.

fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

ItemEvent

to deliver to listeners
**See Also:** EventListenerList

---

#### fireItemStateChanged

protected void fireItemStateChanged​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of requested listeners
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getActionListeners()

,

getChangeListeners()

,

getItemListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultButtonModel

instance

m

for its action listeners
with the following code:

```java
ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));
```

If no such listeners exist,
this method returns an empty array.

ActionListener[] als = (ActionListener[])(m.getListeners(ActionListener.class));

getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Overridden to return

null

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** the list of selected objects, or

null

---

#### getSelectedObjects

public

Object

[] getSelectedObjects()

Overridden to return

null

.

getGroup

```java
public
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Specified by:** getGroup

in interface

ButtonModel
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 1.3

---

#### getGroup

public

ButtonGroup

getGroup()

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

---

