# Class CompoundControl

**Source:** `java.desktop\javax\sound\sampled\CompoundControl.html`

### Class Description

```java
public abstract class
CompoundControl

extends
Control
```

A

CompoundControl

, such as a graphic equalizer, provides control over
two or more related properties, each of which is itself represented as a

Control

.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CompoundControl​(
CompoundControl.Type
type,

Control
[] memberControls)

Constructs a new compound control object with the given parameters.

**Parameters:**
- type

- the type of control represented this compound control object
- memberControls

- the set of member controls

---

### Method Details

#### public
Control
[] getMemberControls()

Returns the set of member controls that comprise the compound control.

**Returns:**
- the set of member controls

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
- a string description

---

### Additional Sections

#### Class CompoundControl

java.lang.Object

- javax.sound.sampled.Control
- - javax.sound.sampled.CompoundControl

javax.sound.sampled.Control

- javax.sound.sampled.CompoundControl

javax.sound.sampled.CompoundControl

```java
public abstract class
CompoundControl

extends
Control
```

A

CompoundControl

, such as a graphic equalizer, provides control over
two or more related properties, each of which is itself represented as a

Control

.

**Since:** 1.3

public abstract class

CompoundControl

extends

Control

A

CompoundControl

, such as a graphic equalizer, provides control over
two or more related properties, each of which is itself represented as a

Control

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CompoundControl.Type

An instance of the

CompoundControl.Type

inner class identifies
one kind of compound control.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CompoundControl

​(

CompoundControl.Type

type,

Control

[] memberControls)

Constructs a new compound control object with the given parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Control

[]

getMemberControls

()

Returns the set of member controls that comprise the compound control.

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

CompoundControl.Type

An instance of the

CompoundControl.Type

inner class identifies
one kind of compound control.

---

#### Nested Class Summary

An instance of the

CompoundControl.Type

inner class identifies
one kind of compound control.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CompoundControl

​(

CompoundControl.Type

type,

Control

[] memberControls)

Constructs a new compound control object with the given parameters.

---

#### Constructor Summary

Constructs a new compound control object with the given parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Control

[]

getMemberControls

()

Returns the set of member controls that comprise the compound control.

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

Returns the set of member controls that comprise the compound control.

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

- CompoundControl

```java
protected CompoundControl​(
CompoundControl.Type
type,

Control
[] memberControls)
```

Constructs a new compound control object with the given parameters.

**Parameters:** type

- the type of control represented this compound control object
**Parameters:** memberControls

- the set of member controls

============ METHOD DETAIL ==========

- Method Detail

- getMemberControls

```java
public
Control
[] getMemberControls()
```

Returns the set of member controls that comprise the compound control.

**Returns:** the set of member controls

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
**Returns:** a string description

Constructor Detail

- CompoundControl

```java
protected CompoundControl​(
CompoundControl.Type
type,

Control
[] memberControls)
```

Constructs a new compound control object with the given parameters.

**Parameters:** type

- the type of control represented this compound control object
**Parameters:** memberControls

- the set of member controls

---

#### Constructor Detail

CompoundControl

```java
protected CompoundControl​(
CompoundControl.Type
type,

Control
[] memberControls)
```

Constructs a new compound control object with the given parameters.

**Parameters:** type

- the type of control represented this compound control object
**Parameters:** memberControls

- the set of member controls

---

#### CompoundControl

protected CompoundControl​(

CompoundControl.Type

type,

Control

[] memberControls)

Constructs a new compound control object with the given parameters.

Method Detail

- getMemberControls

```java
public
Control
[] getMemberControls()
```

Returns the set of member controls that comprise the compound control.

**Returns:** the set of member controls

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
**Returns:** a string description

---

#### Method Detail

getMemberControls

```java
public
Control
[] getMemberControls()
```

Returns the set of member controls that comprise the compound control.

**Returns:** the set of member controls

---

#### getMemberControls

public

Control

[] getMemberControls()

Returns the set of member controls that comprise the compound control.

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
**Returns:** a string description

---

#### toString

public

String

toString()

Provides a string representation of the control.

---

