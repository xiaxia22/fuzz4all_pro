# Enum StackWalker.Option

**Source:** `java.base\java\lang\StackWalker.Option.html`

### Class Description

```java
public static enum
StackWalker.Option

extends
Enum
<
StackWalker.Option
>
```

Stack walker option to configure the

stack frame

information obtained by a

StackWalker

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

StackWalker.Option

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
StackWalker.Option
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
StackWalker.Option
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum StackWalker.Option

java.lang.Object

- java.lang.Enum

<

StackWalker.Option

>
- - java.lang.StackWalker.Option

java.lang.Enum

<

StackWalker.Option

>

- java.lang.StackWalker.Option

java.lang.StackWalker.Option

**All Implemented Interfaces:** Serializable

,

Comparable

<

StackWalker.Option

>

**Enclosing class:** StackWalker

```java
public static enum
StackWalker.Option

extends
Enum
<
StackWalker.Option
>
```

Stack walker option to configure the

stack frame

information obtained by a

StackWalker

.

**Since:** 9

public static enum

StackWalker.Option

extends

Enum

<

StackWalker.Option

>

Stack walker option to configure the

stack frame

information obtained by a

StackWalker

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

RETAIN_CLASS_REFERENCE

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

SHOW_HIDDEN_FRAMES

Shows all hidden frames.

SHOW_REFLECT_FRAMES

Shows all reflection frames.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StackWalker.Option

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StackWalker.Option

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

RETAIN_CLASS_REFERENCE

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

SHOW_HIDDEN_FRAMES

Shows all hidden frames.

SHOW_REFLECT_FRAMES

Shows all reflection frames.

---

#### Enum Constant Summary

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

Shows all hidden frames.

Shows all reflection frames.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

StackWalker.Option

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

StackWalker.Option

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- RETAIN_CLASS_REFERENCE

```java
public static final
StackWalker.Option
RETAIN_CLASS_REFERENCE
```

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

A

StackWalker

configured with this option will support

StackWalker.getCallerClass()

and

StackFrame.getDeclaringClass()

.

- SHOW_REFLECT_FRAMES

```java
public static final
StackWalker.Option
SHOW_REFLECT_FRAMES
```

Shows all reflection frames.

By default, reflection frames are hidden. A

StackWalker

configured with this

SHOW_REFLECT_FRAMES

option
will show all reflection frames that
include

Method.invoke(java.lang.Object, java.lang.Object...)

and

Constructor.newInstance(Object...)

and their reflection implementation classes.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

**API Note:** This option includes the stack frames representing the invocation of

Method

and

Constructor

. Any utility methods that
are equivalent to calling

Method.invoke

or

Constructor.newInstance

such as

Class.newInstance

are not filtered or controlled by any stack walking option.

- SHOW_HIDDEN_FRAMES

```java
public static final
StackWalker.Option
SHOW_HIDDEN_FRAMES
```

Shows all hidden frames.

A Java Virtual Machine implementation may hide implementation
specific frames in addition to

reflection frames

. A

StackWalker

with this

SHOW_HIDDEN_FRAMES

option will show all hidden frames (including reflection frames).

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
StackWalker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StackWalker.Option
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- RETAIN_CLASS_REFERENCE

```java
public static final
StackWalker.Option
RETAIN_CLASS_REFERENCE
```

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

A

StackWalker

configured with this option will support

StackWalker.getCallerClass()

and

StackFrame.getDeclaringClass()

.

- SHOW_REFLECT_FRAMES

```java
public static final
StackWalker.Option
SHOW_REFLECT_FRAMES
```

Shows all reflection frames.

By default, reflection frames are hidden. A

StackWalker

configured with this

SHOW_REFLECT_FRAMES

option
will show all reflection frames that
include

Method.invoke(java.lang.Object, java.lang.Object...)

and

Constructor.newInstance(Object...)

and their reflection implementation classes.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

**API Note:** This option includes the stack frames representing the invocation of

Method

and

Constructor

. Any utility methods that
are equivalent to calling

Method.invoke

or

Constructor.newInstance

such as

Class.newInstance

are not filtered or controlled by any stack walking option.

- SHOW_HIDDEN_FRAMES

```java
public static final
StackWalker.Option
SHOW_HIDDEN_FRAMES
```

Shows all hidden frames.

A Java Virtual Machine implementation may hide implementation
specific frames in addition to

reflection frames

. A

StackWalker

with this

SHOW_HIDDEN_FRAMES

option will show all hidden frames (including reflection frames).

---

#### Enum Constant Detail

RETAIN_CLASS_REFERENCE

```java
public static final
StackWalker.Option
RETAIN_CLASS_REFERENCE
```

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

A

StackWalker

configured with this option will support

StackWalker.getCallerClass()

and

StackFrame.getDeclaringClass()

.

---

#### RETAIN_CLASS_REFERENCE

public static final

StackWalker.Option

RETAIN_CLASS_REFERENCE

Retains

Class

object in

StackFrame

s
walked by this

StackWalker

.

A

StackWalker

configured with this option will support

StackWalker.getCallerClass()

and

StackFrame.getDeclaringClass()

.

A

StackWalker

configured with this option will support

StackWalker.getCallerClass()

and

StackFrame.getDeclaringClass()

.

SHOW_REFLECT_FRAMES

```java
public static final
StackWalker.Option
SHOW_REFLECT_FRAMES
```

Shows all reflection frames.

By default, reflection frames are hidden. A

StackWalker

configured with this

SHOW_REFLECT_FRAMES

option
will show all reflection frames that
include

Method.invoke(java.lang.Object, java.lang.Object...)

and

Constructor.newInstance(Object...)

and their reflection implementation classes.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

**API Note:** This option includes the stack frames representing the invocation of

Method

and

Constructor

. Any utility methods that
are equivalent to calling

Method.invoke

or

Constructor.newInstance

such as

Class.newInstance

are not filtered or controlled by any stack walking option.

---

#### SHOW_REFLECT_FRAMES

public static final

StackWalker.Option

SHOW_REFLECT_FRAMES

Shows all reflection frames.

By default, reflection frames are hidden. A

StackWalker

configured with this

SHOW_REFLECT_FRAMES

option
will show all reflection frames that
include

Method.invoke(java.lang.Object, java.lang.Object...)

and

Constructor.newInstance(Object...)

and their reflection implementation classes.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

By default, reflection frames are hidden. A

StackWalker

configured with this

SHOW_REFLECT_FRAMES

option
will show all reflection frames that
include

Method.invoke(java.lang.Object, java.lang.Object...)

and

Constructor.newInstance(Object...)

and their reflection implementation classes.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

The

SHOW_HIDDEN_FRAMES

option can also be used to show all
reflection frames and it will also show other hidden frames that
are implementation-specific.

SHOW_HIDDEN_FRAMES

```java
public static final
StackWalker.Option
SHOW_HIDDEN_FRAMES
```

Shows all hidden frames.

A Java Virtual Machine implementation may hide implementation
specific frames in addition to

reflection frames

. A

StackWalker

with this

SHOW_HIDDEN_FRAMES

option will show all hidden frames (including reflection frames).

---

#### SHOW_HIDDEN_FRAMES

public static final

StackWalker.Option

SHOW_HIDDEN_FRAMES

Shows all hidden frames.

A Java Virtual Machine implementation may hide implementation
specific frames in addition to

reflection frames

. A

StackWalker

with this

SHOW_HIDDEN_FRAMES

option will show all hidden frames (including reflection frames).

A Java Virtual Machine implementation may hide implementation
specific frames in addition to

reflection frames

. A

StackWalker

with this

SHOW_HIDDEN_FRAMES

option will show all hidden frames (including reflection frames).

Method Detail

- values

```java
public static
StackWalker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
StackWalker.Option
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
StackWalker.Option
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

StackWalker.Option

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);
```

for (StackWalker.Option c : StackWalker.Option.values())
System.out.println(c);

valueOf

```java
public static
StackWalker.Option
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

StackWalker.Option

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

