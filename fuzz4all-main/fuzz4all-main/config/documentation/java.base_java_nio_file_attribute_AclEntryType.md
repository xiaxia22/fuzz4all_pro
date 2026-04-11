# Enum AclEntryType

**Source:** `java.base\java\nio\file\attribute\AclEntryType.html`

### Class Description

```java
public enum
AclEntryType

extends
Enum
<
AclEntryType
>
```

A typesafe enumeration of the access control entry types.

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AclEntryType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryType c : AclEntryType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
AclEntryType
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

#### Enum AclEntryType

java.lang.Object

- java.lang.Enum

<

AclEntryType

>
- - java.nio.file.attribute.AclEntryType

java.lang.Enum

<

AclEntryType

>

- java.nio.file.attribute.AclEntryType

java.nio.file.attribute.AclEntryType

**All Implemented Interfaces:** Serializable

,

Comparable

<

AclEntryType

>

```java
public enum
AclEntryType

extends
Enum
<
AclEntryType
>
```

A typesafe enumeration of the access control entry types.

**Since:** 1.7

public enum

AclEntryType

extends

Enum

<

AclEntryType

>

A typesafe enumeration of the access control entry types.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALARM

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

ALLOW

Explicitly grants access to a file or directory.

AUDIT

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

DENY

Explicitly denies access to a file or directory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryType

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

ALARM

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

ALLOW

Explicitly grants access to a file or directory.

AUDIT

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

DENY

Explicitly denies access to a file or directory.

---

#### Enum Constant Summary

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

Explicitly grants access to a file or directory.

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

Explicitly denies access to a file or directory.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AclEntryType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AclEntryType

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

- ALLOW

```java
public static final
AclEntryType
ALLOW
```

Explicitly grants access to a file or directory.

- DENY

```java
public static final
AclEntryType
DENY
```

Explicitly denies access to a file or directory.

- AUDIT

```java
public static final
AclEntryType
AUDIT
```

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

- ALARM

```java
public static final
AclEntryType
ALARM
```

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
AclEntryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryType c : AclEntryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryType
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

- ALLOW

```java
public static final
AclEntryType
ALLOW
```

Explicitly grants access to a file or directory.

- DENY

```java
public static final
AclEntryType
DENY
```

Explicitly denies access to a file or directory.

- AUDIT

```java
public static final
AclEntryType
AUDIT
```

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

- ALARM

```java
public static final
AclEntryType
ALARM
```

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

---

#### Enum Constant Detail

ALLOW

```java
public static final
AclEntryType
ALLOW
```

Explicitly grants access to a file or directory.

---

#### ALLOW

public static final

AclEntryType

ALLOW

Explicitly grants access to a file or directory.

DENY

```java
public static final
AclEntryType
DENY
```

Explicitly denies access to a file or directory.

---

#### DENY

public static final

AclEntryType

DENY

Explicitly denies access to a file or directory.

AUDIT

```java
public static final
AclEntryType
AUDIT
```

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

---

#### AUDIT

public static final

AclEntryType

AUDIT

Log, in a system dependent way, the access specified in the
permissions component of the ACL entry.

ALARM

```java
public static final
AclEntryType
ALARM
```

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

---

#### ALARM

public static final

AclEntryType

ALARM

Generate an alarm, in a system dependent way, the access specified in the
permissions component of the ACL entry.

Method Detail

- values

```java
public static
AclEntryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryType c : AclEntryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AclEntryType
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
AclEntryType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryType c : AclEntryType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

AclEntryType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AclEntryType c : AclEntryType.values())
System.out.println(c);
```

for (AclEntryType c : AclEntryType.values())
System.out.println(c);

valueOf

```java
public static
AclEntryType
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

AclEntryType

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

