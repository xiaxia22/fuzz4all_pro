# Enum UserSessionEvent.Reason

**Source:** `java.desktop\java\awt\desktop\UserSessionEvent.Reason.html`

### Class Description

```java
public static enum
UserSessionEvent.Reason

extends
Enum
<
UserSessionEvent.Reason
>
```

Kinds of available reasons of user session change.

**All Implemented Interfaces:** Serializable

,

Comparable

<

UserSessionEvent.Reason

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
UserSessionEvent.Reason
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
UserSessionEvent.Reason
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

#### Enum UserSessionEvent.Reason

java.lang.Object

- java.lang.Enum

<

UserSessionEvent.Reason

>
- - java.awt.desktop.UserSessionEvent.Reason

java.lang.Enum

<

UserSessionEvent.Reason

>

- java.awt.desktop.UserSessionEvent.Reason

java.awt.desktop.UserSessionEvent.Reason

**All Implemented Interfaces:** Serializable

,

Comparable

<

UserSessionEvent.Reason

>

**Enclosing class:** UserSessionEvent

```java
public static enum
UserSessionEvent.Reason

extends
Enum
<
UserSessionEvent.Reason
>
```

Kinds of available reasons of user session change.

public static enum

UserSessionEvent.Reason

extends

Enum

<

UserSessionEvent.Reason

>

Kinds of available reasons of user session change.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CONSOLE

The session was connected/disconnected to the console terminal.

LOCK

The session has been locked/unlocked.

REMOTE

The session was connected/disconnected to the remote terminal.

UNSPECIFIED

The system does not provide a reason for a session change.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

UserSessionEvent.Reason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

UserSessionEvent.Reason

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

CONSOLE

The session was connected/disconnected to the console terminal.

LOCK

The session has been locked/unlocked.

REMOTE

The session was connected/disconnected to the remote terminal.

UNSPECIFIED

The system does not provide a reason for a session change.

---

#### Enum Constant Summary

The session was connected/disconnected to the console terminal.

The session has been locked/unlocked.

The session was connected/disconnected to the remote terminal.

The system does not provide a reason for a session change.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

UserSessionEvent.Reason

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

UserSessionEvent.Reason

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

- UNSPECIFIED

```java
public static final
UserSessionEvent.Reason
UNSPECIFIED
```

The system does not provide a reason for a session change.

- CONSOLE

```java
public static final
UserSessionEvent.Reason
CONSOLE
```

The session was connected/disconnected to the console terminal.

- REMOTE

```java
public static final
UserSessionEvent.Reason
REMOTE
```

The session was connected/disconnected to the remote terminal.

- LOCK

```java
public static final
UserSessionEvent.Reason
LOCK
```

The session has been locked/unlocked.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
UserSessionEvent.Reason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
UserSessionEvent.Reason
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

- UNSPECIFIED

```java
public static final
UserSessionEvent.Reason
UNSPECIFIED
```

The system does not provide a reason for a session change.

- CONSOLE

```java
public static final
UserSessionEvent.Reason
CONSOLE
```

The session was connected/disconnected to the console terminal.

- REMOTE

```java
public static final
UserSessionEvent.Reason
REMOTE
```

The session was connected/disconnected to the remote terminal.

- LOCK

```java
public static final
UserSessionEvent.Reason
LOCK
```

The session has been locked/unlocked.

---

#### Enum Constant Detail

UNSPECIFIED

```java
public static final
UserSessionEvent.Reason
UNSPECIFIED
```

The system does not provide a reason for a session change.

---

#### UNSPECIFIED

public static final

UserSessionEvent.Reason

UNSPECIFIED

The system does not provide a reason for a session change.

CONSOLE

```java
public static final
UserSessionEvent.Reason
CONSOLE
```

The session was connected/disconnected to the console terminal.

---

#### CONSOLE

public static final

UserSessionEvent.Reason

CONSOLE

The session was connected/disconnected to the console terminal.

REMOTE

```java
public static final
UserSessionEvent.Reason
REMOTE
```

The session was connected/disconnected to the remote terminal.

---

#### REMOTE

public static final

UserSessionEvent.Reason

REMOTE

The session was connected/disconnected to the remote terminal.

LOCK

```java
public static final
UserSessionEvent.Reason
LOCK
```

The session has been locked/unlocked.

---

#### LOCK

public static final

UserSessionEvent.Reason

LOCK

The session has been locked/unlocked.

Method Detail

- values

```java
public static
UserSessionEvent.Reason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
UserSessionEvent.Reason
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
UserSessionEvent.Reason
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

UserSessionEvent.Reason

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);
```

for (UserSessionEvent.Reason c : UserSessionEvent.Reason.values())
System.out.println(c);

valueOf

```java
public static
UserSessionEvent.Reason
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

UserSessionEvent.Reason

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

