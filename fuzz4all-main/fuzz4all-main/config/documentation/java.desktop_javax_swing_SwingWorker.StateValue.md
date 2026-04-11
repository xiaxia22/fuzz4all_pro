# Enum SwingWorker.StateValue

**Source:** `java.desktop\javax\swing\SwingWorker.StateValue.html`

### Class Description

```java
public static enum
SwingWorker.StateValue

extends
Enum
<
SwingWorker.StateValue
>
```

Values for the

state

bound property.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SwingWorker.StateValue

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SwingWorker.StateValue
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SwingWorker.StateValue
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

#### Enum SwingWorker.StateValue

java.lang.Object

- java.lang.Enum

<

SwingWorker.StateValue

>
- - javax.swing.SwingWorker.StateValue

java.lang.Enum

<

SwingWorker.StateValue

>

- javax.swing.SwingWorker.StateValue

javax.swing.SwingWorker.StateValue

**All Implemented Interfaces:** Serializable

,

Comparable

<

SwingWorker.StateValue

>

**Enclosing class:** SwingWorker

<

T

,​

V

>

```java
public static enum
SwingWorker.StateValue

extends
Enum
<
SwingWorker.StateValue
>
```

Values for the

state

bound property.

**Since:** 1.6

public static enum

SwingWorker.StateValue

extends

Enum

<

SwingWorker.StateValue

>

Values for the

state

bound property.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DONE

SwingWorker

is

DONE

after

doInBackground

method
is finished.

PENDING

Initial

SwingWorker

state.

STARTED

SwingWorker

is

STARTED

before invoking

doInBackground

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SwingWorker.StateValue

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SwingWorker.StateValue

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

DONE

SwingWorker

is

DONE

after

doInBackground

method
is finished.

PENDING

Initial

SwingWorker

state.

STARTED

SwingWorker

is

STARTED

before invoking

doInBackground

.

---

#### Enum Constant Summary

SwingWorker

is

DONE

after

doInBackground

method
is finished.

Initial

SwingWorker

state.

SwingWorker

is

STARTED

before invoking

doInBackground

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SwingWorker.StateValue

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SwingWorker.StateValue

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

- PENDING

```java
public static final
SwingWorker.StateValue
PENDING
```

Initial

SwingWorker

state.

- STARTED

```java
public static final
SwingWorker.StateValue
STARTED
```

SwingWorker

is

STARTED

before invoking

doInBackground

.

- DONE

```java
public static final
SwingWorker.StateValue
DONE
```

SwingWorker

is

DONE

after

doInBackground

method
is finished.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SwingWorker.StateValue
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SwingWorker.StateValue
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

- PENDING

```java
public static final
SwingWorker.StateValue
PENDING
```

Initial

SwingWorker

state.

- STARTED

```java
public static final
SwingWorker.StateValue
STARTED
```

SwingWorker

is

STARTED

before invoking

doInBackground

.

- DONE

```java
public static final
SwingWorker.StateValue
DONE
```

SwingWorker

is

DONE

after

doInBackground

method
is finished.

---

#### Enum Constant Detail

PENDING

```java
public static final
SwingWorker.StateValue
PENDING
```

Initial

SwingWorker

state.

---

#### PENDING

public static final

SwingWorker.StateValue

PENDING

Initial

SwingWorker

state.

STARTED

```java
public static final
SwingWorker.StateValue
STARTED
```

SwingWorker

is

STARTED

before invoking

doInBackground

.

---

#### STARTED

public static final

SwingWorker.StateValue

STARTED

SwingWorker

is

STARTED

before invoking

doInBackground

.

DONE

```java
public static final
SwingWorker.StateValue
DONE
```

SwingWorker

is

DONE

after

doInBackground

method
is finished.

---

#### DONE

public static final

SwingWorker.StateValue

DONE

SwingWorker

is

DONE

after

doInBackground

method
is finished.

Method Detail

- values

```java
public static
SwingWorker.StateValue
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SwingWorker.StateValue
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
SwingWorker.StateValue
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SwingWorker.StateValue

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);
```

for (SwingWorker.StateValue c : SwingWorker.StateValue.values())
System.out.println(c);

valueOf

```java
public static
SwingWorker.StateValue
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

SwingWorker.StateValue

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

