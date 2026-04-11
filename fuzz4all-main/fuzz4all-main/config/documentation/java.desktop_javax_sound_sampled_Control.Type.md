# Class Control.Type

**Source:** `java.desktop\javax\sound\sampled\Control.Type.html`

### Class Description

```java
public static class
Control.Type

extends
Object
```

An instance of the

Type

class represents the type of the control.

**Direct Known Subclasses:** BooleanControl.Type

,

CompoundControl.Type

,

EnumControl.Type

,

FloatControl.Type

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Type​(
String
name)

Constructs a new control type with the name specified. The name
should be a descriptive string appropriate for labelling the control
in an application, such as "Gain" or "Balance".

**Parameters:**
- name

- the name of the new control type

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this control
type;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this control type.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this control type

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
toString()

Provides the

String

representation of the control type. This

String

is the same name that was passed to the constructor.

**Overrides:**
- toString

in class

Object

**Returns:**
- the control type name

---

### Additional Sections

#### Class Control.Type

java.lang.Object

- javax.sound.sampled.Control.Type

javax.sound.sampled.Control.Type

**Direct Known Subclasses:** BooleanControl.Type

,

CompoundControl.Type

,

EnumControl.Type

,

FloatControl.Type

**Enclosing class:** Control

```java
public static class
Control.Type

extends
Object
```

An instance of the

Type

class represents the type of the control.

public static class

Control.Type

extends

Object

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

Type

​(

String

name)

Constructs a new control type with the name specified.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

int

hashCode

()

Returns a hash code value for this control type.

String

toString

()

Provides the

String

representation of the control type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Type

​(

String

name)

Constructs a new control type with the name specified.

---

#### Constructor Summary

Constructs a new control type with the name specified.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

int

hashCode

()

Returns a hash code value for this control type.

String

toString

()

Provides the

String

representation of the control type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

Returns a hash code value for this control type.

Provides the

String

representation of the control type.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Type

```java
protected Type​(
String
name)
```

Constructs a new control type with the name specified. The name
should be a descriptive string appropriate for labelling the control
in an application, such as "Gain" or "Balance".

**Parameters:** name

- the name of the new control type

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this control
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this control type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this control type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the

String

representation of the control type. This

String

is the same name that was passed to the constructor.

**Overrides:** toString

in class

Object
**Returns:** the control type name

Constructor Detail

- Type

```java
protected Type​(
String
name)
```

Constructs a new control type with the name specified. The name
should be a descriptive string appropriate for labelling the control
in an application, such as "Gain" or "Balance".

**Parameters:** name

- the name of the new control type

---

#### Constructor Detail

Type

```java
protected Type​(
String
name)
```

Constructs a new control type with the name specified. The name
should be a descriptive string appropriate for labelling the control
in an application, such as "Gain" or "Balance".

**Parameters:** name

- the name of the new control type

---

#### Type

protected Type​(

String

name)

Constructs a new control type with the name specified. The name
should be a descriptive string appropriate for labelling the control
in an application, such as "Gain" or "Balance".

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this control
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this control type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this control type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the

String

representation of the control type. This

String

is the same name that was passed to the constructor.

**Overrides:** toString

in class

Object
**Returns:** the control type name

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this control
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this control type,
returning

true

if the objects are the same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this control type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this control type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this control type.

toString

```java
public final
String
toString()
```

Provides the

String

representation of the control type. This

String

is the same name that was passed to the constructor.

**Overrides:** toString

in class

Object
**Returns:** the control type name

---

#### toString

public final

String

toString()

Provides the

String

representation of the control type. This

String

is the same name that was passed to the constructor.

---

