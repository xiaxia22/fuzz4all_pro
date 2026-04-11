# Class Control

**Source:** `java.desktop\javax\sound\sampled\Control.html`

### Class Description

```java
public abstract class
Control

extends
Object
```

Lines

often have a set of controls, such as gain and pan, that
affect the audio signal passing through the line. Java Sound's

Line

objects let you obtain a particular control object by passing its class as
the argument to a

getControl

method.

Because the various types of controls have different purposes and features,
all of their functionality is accessed from the subclasses that define each
kind of control.

**Direct Known Subclasses:** BooleanControl

,

CompoundControl

,

EnumControl

,

FloatControl

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Control​(
Control.Type
type)

Constructs a control with the specified type.

**Parameters:**
- type

- the kind of control desired

---

### Method Details

#### public
Control.Type
getType()

Obtains the control's type.

**Returns:**
- the control's type

---

#### public
String
toString()

Obtains a string describing the control type and its current state.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the control

---

### Additional Sections

#### Class Control

java.lang.Object

- javax.sound.sampled.Control

javax.sound.sampled.Control

**Direct Known Subclasses:** BooleanControl

,

CompoundControl

,

EnumControl

,

FloatControl

```java
public abstract class
Control

extends
Object
```

Lines

often have a set of controls, such as gain and pan, that
affect the audio signal passing through the line. Java Sound's

Line

objects let you obtain a particular control object by passing its class as
the argument to a

getControl

method.

Because the various types of controls have different purposes and features,
all of their functionality is accessed from the subclasses that define each
kind of control.

**Since:** 1.3
**See Also:** Line.getControls()

,

Line.isControlSupported(javax.sound.sampled.Control.Type)

public abstract class

Control

extends

Object

Lines

often have a set of controls, such as gain and pan, that
affect the audio signal passing through the line. Java Sound's

Line

objects let you obtain a particular control object by passing its class as
the argument to a

getControl

method.

Because the various types of controls have different purposes and features,
all of their functionality is accessed from the subclasses that define each
kind of control.

Because the various types of controls have different purposes and features,
all of their functionality is accessed from the subclasses that define each
kind of control.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Control.Type

An instance of the

Type

class represents the type of the control.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Control

​(

Control.Type

type)

Constructs a control with the specified type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Control.Type

getType

()

Obtains the control's type.

String

toString

()

Obtains a string describing the control type and its current state.

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

Control.Type

An instance of the

Type

class represents the type of the control.

---

#### Nested Class Summary

An instance of the

Type

class represents the type of the control.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Control

​(

Control.Type

type)

Constructs a control with the specified type.

---

#### Constructor Summary

Constructs a control with the specified type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Control.Type

getType

()

Obtains the control's type.

String

toString

()

Obtains a string describing the control type and its current state.

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

Obtains the control's type.

Obtains a string describing the control type and its current state.

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

- Control

```java
protected Control​(
Control.Type
type)
```

Constructs a control with the specified type.

**Parameters:** type

- the kind of control desired

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public
Control.Type
getType()
```

Obtains the control's type.

**Returns:** the control's type

- toString

```java
public
String
toString()
```

Obtains a string describing the control type and its current state.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the control

Constructor Detail

- Control

```java
protected Control​(
Control.Type
type)
```

Constructs a control with the specified type.

**Parameters:** type

- the kind of control desired

---

#### Constructor Detail

Control

```java
protected Control​(
Control.Type
type)
```

Constructs a control with the specified type.

**Parameters:** type

- the kind of control desired

---

#### Control

protected Control​(

Control.Type

type)

Constructs a control with the specified type.

Method Detail

- getType

```java
public
Control.Type
getType()
```

Obtains the control's type.

**Returns:** the control's type

- toString

```java
public
String
toString()
```

Obtains a string describing the control type and its current state.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the control

---

#### Method Detail

getType

```java
public
Control.Type
getType()
```

Obtains the control's type.

**Returns:** the control's type

---

#### getType

public

Control.Type

getType()

Obtains the control's type.

toString

```java
public
String
toString()
```

Obtains a string describing the control type and its current state.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the control

---

#### toString

public

String

toString()

Obtains a string describing the control type and its current state.

---

