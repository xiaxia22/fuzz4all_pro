# Enum AssociationChangeNotification.AssocChangeEvent

**Source:** `jdk.sctp\com\sun\nio\sctp\AssociationChangeNotification.AssocChangeEvent.html`

### Class Description

```java
public static enum
AssociationChangeNotification.AssocChangeEvent

extends
Enum
<
AssociationChangeNotification.AssocChangeEvent
>
```

Defines the type of change event that happened to the association.

**All Implemented Interfaces:** Serializable

,

Comparable

<

AssociationChangeNotification.AssocChangeEvent

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AssociationChangeNotification.AssocChangeEvent
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
AssociationChangeNotification.AssocChangeEvent
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

#### Enum AssociationChangeNotification.AssocChangeEvent

java.lang.Object

- java.lang.Enum

<

AssociationChangeNotification.AssocChangeEvent

>
- - com.sun.nio.sctp.AssociationChangeNotification.AssocChangeEvent

java.lang.Enum

<

AssociationChangeNotification.AssocChangeEvent

>

- com.sun.nio.sctp.AssociationChangeNotification.AssocChangeEvent

com.sun.nio.sctp.AssociationChangeNotification.AssocChangeEvent

**All Implemented Interfaces:** Serializable

,

Comparable

<

AssociationChangeNotification.AssocChangeEvent

>

**Enclosing class:** AssociationChangeNotification

```java
public static enum
AssociationChangeNotification.AssocChangeEvent

extends
Enum
<
AssociationChangeNotification.AssocChangeEvent
>
```

Defines the type of change event that happened to the association.

**Since:** 1.7

public static enum

AssociationChangeNotification.AssocChangeEvent

extends

Enum

<

AssociationChangeNotification.AssocChangeEvent

>

Defines the type of change event that happened to the association.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CANT_START

The association failed to setup.

COMM_LOST

The association has failed.

COMM_UP

A new association is now ready and data may be exchanged with this peer.

RESTART

SCTP has detected that the peer has restarted.

SHUTDOWN

The association has gracefully closed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AssociationChangeNotification.AssocChangeEvent

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AssociationChangeNotification.AssocChangeEvent

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

CANT_START

The association failed to setup.

COMM_LOST

The association has failed.

COMM_UP

A new association is now ready and data may be exchanged with this peer.

RESTART

SCTP has detected that the peer has restarted.

SHUTDOWN

The association has gracefully closed.

---

#### Enum Constant Summary

The association failed to setup.

The association has failed.

A new association is now ready and data may be exchanged with this peer.

SCTP has detected that the peer has restarted.

The association has gracefully closed.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

AssociationChangeNotification.AssocChangeEvent

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

AssociationChangeNotification.AssocChangeEvent

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

- COMM_UP

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_UP
```

A new association is now ready and data may be exchanged with this peer.

- COMM_LOST

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_LOST
```

The association has failed. A series of SCTP send failed notifications
will follow this notification, one for each outstanding message.

- RESTART

```java
public static final
AssociationChangeNotification.AssocChangeEvent
RESTART
```

SCTP has detected that the peer has restarted.

- SHUTDOWN

```java
public static final
AssociationChangeNotification.AssocChangeEvent
SHUTDOWN
```

The association has gracefully closed.

- CANT_START

```java
public static final
AssociationChangeNotification.AssocChangeEvent
CANT_START
```

The association failed to setup. If a message was sent on a

SctpMultiChannel

in non-blocking mode, an
SCTP send failed notification will follow this notification for the
outstanding message.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
AssociationChangeNotification.AssocChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AssociationChangeNotification.AssocChangeEvent
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

- COMM_UP

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_UP
```

A new association is now ready and data may be exchanged with this peer.

- COMM_LOST

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_LOST
```

The association has failed. A series of SCTP send failed notifications
will follow this notification, one for each outstanding message.

- RESTART

```java
public static final
AssociationChangeNotification.AssocChangeEvent
RESTART
```

SCTP has detected that the peer has restarted.

- SHUTDOWN

```java
public static final
AssociationChangeNotification.AssocChangeEvent
SHUTDOWN
```

The association has gracefully closed.

- CANT_START

```java
public static final
AssociationChangeNotification.AssocChangeEvent
CANT_START
```

The association failed to setup. If a message was sent on a

SctpMultiChannel

in non-blocking mode, an
SCTP send failed notification will follow this notification for the
outstanding message.

---

#### Enum Constant Detail

COMM_UP

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_UP
```

A new association is now ready and data may be exchanged with this peer.

---

#### COMM_UP

public static final

AssociationChangeNotification.AssocChangeEvent

COMM_UP

A new association is now ready and data may be exchanged with this peer.

COMM_LOST

```java
public static final
AssociationChangeNotification.AssocChangeEvent
COMM_LOST
```

The association has failed. A series of SCTP send failed notifications
will follow this notification, one for each outstanding message.

---

#### COMM_LOST

public static final

AssociationChangeNotification.AssocChangeEvent

COMM_LOST

The association has failed. A series of SCTP send failed notifications
will follow this notification, one for each outstanding message.

RESTART

```java
public static final
AssociationChangeNotification.AssocChangeEvent
RESTART
```

SCTP has detected that the peer has restarted.

---

#### RESTART

public static final

AssociationChangeNotification.AssocChangeEvent

RESTART

SCTP has detected that the peer has restarted.

SHUTDOWN

```java
public static final
AssociationChangeNotification.AssocChangeEvent
SHUTDOWN
```

The association has gracefully closed.

---

#### SHUTDOWN

public static final

AssociationChangeNotification.AssocChangeEvent

SHUTDOWN

The association has gracefully closed.

CANT_START

```java
public static final
AssociationChangeNotification.AssocChangeEvent
CANT_START
```

The association failed to setup. If a message was sent on a

SctpMultiChannel

in non-blocking mode, an
SCTP send failed notification will follow this notification for the
outstanding message.

---

#### CANT_START

public static final

AssociationChangeNotification.AssocChangeEvent

CANT_START

The association failed to setup. If a message was sent on a

SctpMultiChannel

in non-blocking mode, an
SCTP send failed notification will follow this notification for the
outstanding message.

Method Detail

- values

```java
public static
AssociationChangeNotification.AssocChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
AssociationChangeNotification.AssocChangeEvent
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
AssociationChangeNotification.AssocChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

AssociationChangeNotification.AssocChangeEvent

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);
```

for (AssociationChangeNotification.AssocChangeEvent c : AssociationChangeNotification.AssocChangeEvent.values())
System.out.println(c);

valueOf

```java
public static
AssociationChangeNotification.AssocChangeEvent
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

AssociationChangeNotification.AssocChangeEvent

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

