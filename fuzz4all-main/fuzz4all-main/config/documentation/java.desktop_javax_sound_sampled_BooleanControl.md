# Class BooleanControl

**Source:** `java.desktop\javax\sound\sampled\BooleanControl.html`

### Class Description

```java
public abstract class
BooleanControl

extends
Control
```

A

BooleanControl

provides the ability to switch between two possible
settings that affect a line's audio. The settings are boolean values
(

true

and

false

). A graphical user interface might represent
the control by a two-state button, an on/off switch, two mutually exclusive
buttons, or a checkbox (among other possibilities). For example, depressing a
button might activate a

MUTE

control to
silence the line's audio.

As with other

Control

subclasses, a method is provided that returns
string labels for the values, suitable for display in the user interface.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue,

String
trueStateLabel,

String
falseStateLabel)

Constructs a new boolean control object with the given parameters.

**Parameters:**
- type

- the type of control represented this float control object
- initialValue

- the initial control value
- trueStateLabel

- the label for the state represented by

true

, such as "true" or "on"
- falseStateLabel

- the label for the state represented by

false

, such as "false" or "off"

---

#### protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue)

Constructs a new boolean control object with the given parameters. The
labels for the

true

and

false

states default to "true"
and "false".

**Parameters:**
- type

- the type of control represented by this float control object
- initialValue

- the initial control value

---

### Method Details

#### public void setValue​(boolean value)

Sets the current value for the control. The default implementation simply
sets the value as indicated. Some controls require that their line be
open before they can be affected by setting a value.

**Parameters:**
- value

- desired new value

---

#### public boolean getValue()

Obtains this control's current value.

**Returns:**
- current value

---

#### public
String
getStateLabel​(boolean state)

Obtains the label for the specified state.

**Parameters:**
- state

- the state whose label will be returned

**Returns:**
- the label for the specified state, such as "true" or "on" for

true

, or "false" or "off" for

false

---

#### public
String
toString()

Provides a string representation of the control.

**Overrides:**
- toString

in class

Control

**Returns:**
- a string representation of the control

---

### Additional Sections

#### Class BooleanControl

java.lang.Object

- javax.sound.sampled.Control
- - javax.sound.sampled.BooleanControl

javax.sound.sampled.Control

- javax.sound.sampled.BooleanControl

javax.sound.sampled.BooleanControl

```java
public abstract class
BooleanControl

extends
Control
```

A

BooleanControl

provides the ability to switch between two possible
settings that affect a line's audio. The settings are boolean values
(

true

and

false

). A graphical user interface might represent
the control by a two-state button, an on/off switch, two mutually exclusive
buttons, or a checkbox (among other possibilities). For example, depressing a
button might activate a

MUTE

control to
silence the line's audio.

As with other

Control

subclasses, a method is provided that returns
string labels for the values, suitable for display in the user interface.

**Since:** 1.3

public abstract class

BooleanControl

extends

Control

A

BooleanControl

provides the ability to switch between two possible
settings that affect a line's audio. The settings are boolean values
(

true

and

false

). A graphical user interface might represent
the control by a two-state button, an on/off switch, two mutually exclusive
buttons, or a checkbox (among other possibilities). For example, depressing a
button might activate a

MUTE

control to
silence the line's audio.

As with other

Control

subclasses, a method is provided that returns
string labels for the values, suitable for display in the user interface.

As with other

Control

subclasses, a method is provided that returns
string labels for the values, suitable for display in the user interface.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

BooleanControl.Type

An instance of the

BooleanControl.Type

class identifies one kind
of boolean control.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BooleanControl

​(

BooleanControl.Type

type,
boolean initialValue)

Constructs a new boolean control object with the given parameters.

protected

BooleanControl

​(

BooleanControl.Type

type,
boolean initialValue,

String

trueStateLabel,

String

falseStateLabel)

Constructs a new boolean control object with the given parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getStateLabel

​(boolean state)

Obtains the label for the specified state.

boolean

getValue

()

Obtains this control's current value.

void

setValue

​(boolean value)

Sets the current value for the control.

String

toString

()

Provides a string representation of the control.

- Methods declared in class javax.sound.sampled.

Control

getType

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

static class

BooleanControl.Type

An instance of the

BooleanControl.Type

class identifies one kind
of boolean control.

---

#### Nested Class Summary

An instance of the

BooleanControl.Type

class identifies one kind
of boolean control.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BooleanControl

​(

BooleanControl.Type

type,
boolean initialValue)

Constructs a new boolean control object with the given parameters.

protected

BooleanControl

​(

BooleanControl.Type

type,
boolean initialValue,

String

trueStateLabel,

String

falseStateLabel)

Constructs a new boolean control object with the given parameters.

---

#### Constructor Summary

Constructs a new boolean control object with the given parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getStateLabel

​(boolean state)

Obtains the label for the specified state.

boolean

getValue

()

Obtains this control's current value.

void

setValue

​(boolean value)

Sets the current value for the control.

String

toString

()

Provides a string representation of the control.

- Methods declared in class javax.sound.sampled.

Control

getType

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

wait

,

wait

,

wait

---

#### Method Summary

Obtains the label for the specified state.

Obtains this control's current value.

Sets the current value for the control.

Provides a string representation of the control.

Methods declared in class javax.sound.sampled.

Control

getType

---

#### Methods declared in class javax.sound.sampled. Control

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue,

String
trueStateLabel,

String
falseStateLabel)
```

Constructs a new boolean control object with the given parameters.

**Parameters:** type

- the type of control represented this float control object
**Parameters:** initialValue

- the initial control value
**Parameters:** trueStateLabel

- the label for the state represented by

true

, such as "true" or "on"
**Parameters:** falseStateLabel

- the label for the state represented by

false

, such as "false" or "off"

- BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue)
```

Constructs a new boolean control object with the given parameters. The
labels for the

true

and

false

states default to "true"
and "false".

**Parameters:** type

- the type of control represented by this float control object
**Parameters:** initialValue

- the initial control value

============ METHOD DETAIL ==========

- Method Detail

- setValue

```java
public void setValue​(boolean value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. Some controls require that their line be
open before they can be affected by setting a value.

**Parameters:** value

- desired new value

- getValue

```java
public boolean getValue()
```

Obtains this control's current value.

**Returns:** current value

- getStateLabel

```java
public
String
getStateLabel​(boolean state)
```

Obtains the label for the specified state.

**Parameters:** state

- the state whose label will be returned
**Returns:** the label for the specified state, such as "true" or "on" for

true

, or "false" or "off" for

false

- toString

```java
public
String
toString()
```

Provides a string representation of the control.

**Overrides:** toString

in class

Control
**Returns:** a string representation of the control

Constructor Detail

- BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue,

String
trueStateLabel,

String
falseStateLabel)
```

Constructs a new boolean control object with the given parameters.

**Parameters:** type

- the type of control represented this float control object
**Parameters:** initialValue

- the initial control value
**Parameters:** trueStateLabel

- the label for the state represented by

true

, such as "true" or "on"
**Parameters:** falseStateLabel

- the label for the state represented by

false

, such as "false" or "off"

- BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue)
```

Constructs a new boolean control object with the given parameters. The
labels for the

true

and

false

states default to "true"
and "false".

**Parameters:** type

- the type of control represented by this float control object
**Parameters:** initialValue

- the initial control value

---

#### Constructor Detail

BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue,

String
trueStateLabel,

String
falseStateLabel)
```

Constructs a new boolean control object with the given parameters.

**Parameters:** type

- the type of control represented this float control object
**Parameters:** initialValue

- the initial control value
**Parameters:** trueStateLabel

- the label for the state represented by

true

, such as "true" or "on"
**Parameters:** falseStateLabel

- the label for the state represented by

false

, such as "false" or "off"

---

#### BooleanControl

protected BooleanControl​(

BooleanControl.Type

type,
boolean initialValue,

String

trueStateLabel,

String

falseStateLabel)

Constructs a new boolean control object with the given parameters.

BooleanControl

```java
protected BooleanControl​(
BooleanControl.Type
type,
boolean initialValue)
```

Constructs a new boolean control object with the given parameters. The
labels for the

true

and

false

states default to "true"
and "false".

**Parameters:** type

- the type of control represented by this float control object
**Parameters:** initialValue

- the initial control value

---

#### BooleanControl

protected BooleanControl​(

BooleanControl.Type

type,
boolean initialValue)

Constructs a new boolean control object with the given parameters. The
labels for the

true

and

false

states default to "true"
and "false".

Method Detail

- setValue

```java
public void setValue​(boolean value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. Some controls require that their line be
open before they can be affected by setting a value.

**Parameters:** value

- desired new value

- getValue

```java
public boolean getValue()
```

Obtains this control's current value.

**Returns:** current value

- getStateLabel

```java
public
String
getStateLabel​(boolean state)
```

Obtains the label for the specified state.

**Parameters:** state

- the state whose label will be returned
**Returns:** the label for the specified state, such as "true" or "on" for

true

, or "false" or "off" for

false

- toString

```java
public
String
toString()
```

Provides a string representation of the control.

**Overrides:** toString

in class

Control
**Returns:** a string representation of the control

---

#### Method Detail

setValue

```java
public void setValue​(boolean value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. Some controls require that their line be
open before they can be affected by setting a value.

**Parameters:** value

- desired new value

---

#### setValue

public void setValue​(boolean value)

Sets the current value for the control. The default implementation simply
sets the value as indicated. Some controls require that their line be
open before they can be affected by setting a value.

getValue

```java
public boolean getValue()
```

Obtains this control's current value.

**Returns:** current value

---

#### getValue

public boolean getValue()

Obtains this control's current value.

getStateLabel

```java
public
String
getStateLabel​(boolean state)
```

Obtains the label for the specified state.

**Parameters:** state

- the state whose label will be returned
**Returns:** the label for the specified state, such as "true" or "on" for

true

, or "false" or "off" for

false

---

#### getStateLabel

public

String

getStateLabel​(boolean state)

Obtains the label for the specified state.

toString

```java
public
String
toString()
```

Provides a string representation of the control.

**Overrides:** toString

in class

Control
**Returns:** a string representation of the control

---

#### toString

public

String

toString()

Provides a string representation of the control.

---

