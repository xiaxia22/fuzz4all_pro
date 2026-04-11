# Class EnumControl

**Source:** `java.desktop\javax\sound\sampled\EnumControl.html`

### Class Description

```java
public abstract class
EnumControl

extends
Control
```

An

EnumControl

provides control over a set of discrete possible
values, each represented by an object. In a graphical user interface, such a
control might be represented by a set of buttons, each of which chooses one
value or setting. For example, a reverb control might provide several preset
reverberation settings, instead of providing continuously adjustable
parameters of the sort that would be represented by

FloatControl

objects.

Controls that provide a choice between only two settings can often be
implemented instead as a

BooleanControl

, and controls that provide a
set of values along some quantifiable dimension might be implemented instead
as a

FloatControl

with a coarse resolution. However, a key feature of

EnumControl

is that the returned values are arbitrary objects, rather
than numerical or boolean values. This means that each returned object can
provide further information. As an example, the settings of a

REVERB

control are instances of

ReverbType

that can be queried for the parameter values used for each
setting.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### protected EnumControl​(
EnumControl.Type
type,

Object
[] values,

Object
value)

Constructs a new enumerated control object with the given parameters.

**Parameters:**
- type

- the type of control represented this enumerated control
object
- values

- the set of possible values for the control
- value

- the initial control value

---

### Method Details

#### public void setValue​(
Object
value)

Sets the current value for the control. The default implementation simply
sets the value as indicated. If the value indicated is not supported, an

IllegalArgumentException

is thrown. Some controls require that
their line be open before they can be affected by setting a value.

**Parameters:**
- value

- the desired new value

**Throws:**
- IllegalArgumentException

- if the value indicated does not fall
within the allowable range

---

#### public
Object
getValue()

Obtains this control's current value.

**Returns:**
- the current value

---

#### public
Object
[] getValues()

Returns the set of possible values for this control.

**Returns:**
- the set of possible values

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

#### Class EnumControl

java.lang.Object

- javax.sound.sampled.Control
- - javax.sound.sampled.EnumControl

javax.sound.sampled.Control

- javax.sound.sampled.EnumControl

javax.sound.sampled.EnumControl

```java
public abstract class
EnumControl

extends
Control
```

An

EnumControl

provides control over a set of discrete possible
values, each represented by an object. In a graphical user interface, such a
control might be represented by a set of buttons, each of which chooses one
value or setting. For example, a reverb control might provide several preset
reverberation settings, instead of providing continuously adjustable
parameters of the sort that would be represented by

FloatControl

objects.

Controls that provide a choice between only two settings can often be
implemented instead as a

BooleanControl

, and controls that provide a
set of values along some quantifiable dimension might be implemented instead
as a

FloatControl

with a coarse resolution. However, a key feature of

EnumControl

is that the returned values are arbitrary objects, rather
than numerical or boolean values. This means that each returned object can
provide further information. As an example, the settings of a

REVERB

control are instances of

ReverbType

that can be queried for the parameter values used for each
setting.

**Since:** 1.3

public abstract class

EnumControl

extends

Control

An

EnumControl

provides control over a set of discrete possible
values, each represented by an object. In a graphical user interface, such a
control might be represented by a set of buttons, each of which chooses one
value or setting. For example, a reverb control might provide several preset
reverberation settings, instead of providing continuously adjustable
parameters of the sort that would be represented by

FloatControl

objects.

Controls that provide a choice between only two settings can often be
implemented instead as a

BooleanControl

, and controls that provide a
set of values along some quantifiable dimension might be implemented instead
as a

FloatControl

with a coarse resolution. However, a key feature of

EnumControl

is that the returned values are arbitrary objects, rather
than numerical or boolean values. This means that each returned object can
provide further information. As an example, the settings of a

REVERB

control are instances of

ReverbType

that can be queried for the parameter values used for each
setting.

Controls that provide a choice between only two settings can often be
implemented instead as a

BooleanControl

, and controls that provide a
set of values along some quantifiable dimension might be implemented instead
as a

FloatControl

with a coarse resolution. However, a key feature of

EnumControl

is that the returned values are arbitrary objects, rather
than numerical or boolean values. This means that each returned object can
provide further information. As an example, the settings of a

REVERB

control are instances of

ReverbType

that can be queried for the parameter values used for each
setting.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

EnumControl.Type

An instance of the

EnumControl.Type

inner class identifies one
kind of enumerated control.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

EnumControl

​(

EnumControl.Type

type,

Object

[] values,

Object

value)

Constructs a new enumerated control object with the given parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getValue

()

Obtains this control's current value.

Object

[]

getValues

()

Returns the set of possible values for this control.

void

setValue

​(

Object

value)

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

EnumControl.Type

An instance of the

EnumControl.Type

inner class identifies one
kind of enumerated control.

---

#### Nested Class Summary

An instance of the

EnumControl.Type

inner class identifies one
kind of enumerated control.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

EnumControl

​(

EnumControl.Type

type,

Object

[] values,

Object

value)

Constructs a new enumerated control object with the given parameters.

---

#### Constructor Summary

Constructs a new enumerated control object with the given parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getValue

()

Obtains this control's current value.

Object

[]

getValues

()

Returns the set of possible values for this control.

void

setValue

​(

Object

value)

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

Obtains this control's current value.

Returns the set of possible values for this control.

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

- EnumControl

```java
protected EnumControl​(
EnumControl.Type
type,

Object
[] values,

Object
value)
```

Constructs a new enumerated control object with the given parameters.

**Parameters:** type

- the type of control represented this enumerated control
object
**Parameters:** values

- the set of possible values for the control
**Parameters:** value

- the initial control value

============ METHOD DETAIL ==========

- Method Detail

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. If the value indicated is not supported, an

IllegalArgumentException

is thrown. Some controls require that
their line be open before they can be affected by setting a value.

**Parameters:** value

- the desired new value
**Throws:** IllegalArgumentException

- if the value indicated does not fall
within the allowable range

- getValue

```java
public
Object
getValue()
```

Obtains this control's current value.

**Returns:** the current value

- getValues

```java
public
Object
[] getValues()
```

Returns the set of possible values for this control.

**Returns:** the set of possible values

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

- EnumControl

```java
protected EnumControl​(
EnumControl.Type
type,

Object
[] values,

Object
value)
```

Constructs a new enumerated control object with the given parameters.

**Parameters:** type

- the type of control represented this enumerated control
object
**Parameters:** values

- the set of possible values for the control
**Parameters:** value

- the initial control value

---

#### Constructor Detail

EnumControl

```java
protected EnumControl​(
EnumControl.Type
type,

Object
[] values,

Object
value)
```

Constructs a new enumerated control object with the given parameters.

**Parameters:** type

- the type of control represented this enumerated control
object
**Parameters:** values

- the set of possible values for the control
**Parameters:** value

- the initial control value

---

#### EnumControl

protected EnumControl​(

EnumControl.Type

type,

Object

[] values,

Object

value)

Constructs a new enumerated control object with the given parameters.

Method Detail

- setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. If the value indicated is not supported, an

IllegalArgumentException

is thrown. Some controls require that
their line be open before they can be affected by setting a value.

**Parameters:** value

- the desired new value
**Throws:** IllegalArgumentException

- if the value indicated does not fall
within the allowable range

- getValue

```java
public
Object
getValue()
```

Obtains this control's current value.

**Returns:** the current value

- getValues

```java
public
Object
[] getValues()
```

Returns the set of possible values for this control.

**Returns:** the set of possible values

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

setValue

```java
public void setValue​(
Object
value)
```

Sets the current value for the control. The default implementation simply
sets the value as indicated. If the value indicated is not supported, an

IllegalArgumentException

is thrown. Some controls require that
their line be open before they can be affected by setting a value.

**Parameters:** value

- the desired new value
**Throws:** IllegalArgumentException

- if the value indicated does not fall
within the allowable range

---

#### setValue

public void setValue​(

Object

value)

Sets the current value for the control. The default implementation simply
sets the value as indicated. If the value indicated is not supported, an

IllegalArgumentException

is thrown. Some controls require that
their line be open before they can be affected by setting a value.

getValue

```java
public
Object
getValue()
```

Obtains this control's current value.

**Returns:** the current value

---

#### getValue

public

Object

getValue()

Obtains this control's current value.

getValues

```java
public
Object
[] getValues()
```

Returns the set of possible values for this control.

**Returns:** the set of possible values

---

#### getValues

public

Object

[] getValues()

Returns the set of possible values for this control.

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

