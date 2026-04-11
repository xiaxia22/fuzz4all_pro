# Class UIDefaults.LazyInputMap

**Source:** `java.desktop\javax\swing\UIDefaults.LazyInputMap.html`

### Class Description

```java
public static class
UIDefaults.LazyInputMap

extends
Object

implements
UIDefaults.LazyValue
```

LazyInputMap

will create a

InputMap

in its

createValue

method. The bindings are passed in the constructor.
The bindings are an array with
the even number entries being string

KeyStrokes

(eg "alt SPACE") and
the odd number entries being the value to use in the

InputMap

(and the key in the

ActionMap

).

**All Implemented Interfaces:** UIDefaults.LazyValue

---

### Field Details

*No entries found.*

### Constructor Details

#### public LazyInputMap​(
Object
[] bindings)

Constructs a

LazyInputMap

.

**Parameters:**
- bindings

- the bindings

---

### Method Details

#### public
Object
createValue​(
UIDefaults
table)

Creates an

InputMap

with the bindings that are
passed in.

**Specified by:**
- createValue

in interface

UIDefaults.LazyValue

**Parameters:**
- table

- a

UIDefaults

table

**Returns:**
- the

InputMap

---

### Additional Sections

#### Class UIDefaults.LazyInputMap

java.lang.Object

- javax.swing.UIDefaults.LazyInputMap

javax.swing.UIDefaults.LazyInputMap

**All Implemented Interfaces:** UIDefaults.LazyValue

**Enclosing class:** UIDefaults

```java
public static class
UIDefaults.LazyInputMap

extends
Object

implements
UIDefaults.LazyValue
```

LazyInputMap

will create a

InputMap

in its

createValue

method. The bindings are passed in the constructor.
The bindings are an array with
the even number entries being string

KeyStrokes

(eg "alt SPACE") and
the odd number entries being the value to use in the

InputMap

(and the key in the

ActionMap

).

**Since:** 1.3

public static class

UIDefaults.LazyInputMap

extends

Object

implements

UIDefaults.LazyValue

LazyInputMap

will create a

InputMap

in its

createValue

method. The bindings are passed in the constructor.
The bindings are an array with
the even number entries being string

KeyStrokes

(eg "alt SPACE") and
the odd number entries being the value to use in the

InputMap

(and the key in the

ActionMap

).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LazyInputMap

​(

Object

[] bindings)

Constructs a

LazyInputMap

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates an

InputMap

with the bindings that are
passed in.

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

Constructor Summary

Constructors

Constructor

Description

LazyInputMap

​(

Object

[] bindings)

Constructs a

LazyInputMap

.

---

#### Constructor Summary

Constructs a

LazyInputMap

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

createValue

​(

UIDefaults

table)

Creates an

InputMap

with the bindings that are
passed in.

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

Creates an

InputMap

with the bindings that are
passed in.

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

- LazyInputMap

```java
public LazyInputMap​(
Object
[] bindings)
```

Constructs a

LazyInputMap

.

**Parameters:** bindings

- the bindings

============ METHOD DETAIL ==========

- Method Detail

- createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates an

InputMap

with the bindings that are
passed in.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the

InputMap

Constructor Detail

- LazyInputMap

```java
public LazyInputMap​(
Object
[] bindings)
```

Constructs a

LazyInputMap

.

**Parameters:** bindings

- the bindings

---

#### Constructor Detail

LazyInputMap

```java
public LazyInputMap​(
Object
[] bindings)
```

Constructs a

LazyInputMap

.

**Parameters:** bindings

- the bindings

---

#### LazyInputMap

public LazyInputMap​(

Object

[] bindings)

Constructs a

LazyInputMap

.

Method Detail

- createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates an

InputMap

with the bindings that are
passed in.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the

InputMap

---

#### Method Detail

createValue

```java
public
Object
createValue​(
UIDefaults
table)
```

Creates an

InputMap

with the bindings that are
passed in.

**Specified by:** createValue

in interface

UIDefaults.LazyValue
**Parameters:** table

- a

UIDefaults

table
**Returns:** the

InputMap

---

#### createValue

public

Object

createValue​(

UIDefaults

table)

Creates an

InputMap

with the bindings that are
passed in.

---

