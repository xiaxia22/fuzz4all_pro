# Enum PeerAddressChangeNotification.AddressChangeEvent

**Source:** `jdk.sctp\com\sun\nio\sctp\PeerAddressChangeNotification.AddressChangeEvent.html`

### Class Description

```java
public static enum
PeerAddressChangeNotification.AddressChangeEvent

extends
Enum
<
PeerAddressChangeNotification.AddressChangeEvent
>
```

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

Some of these events types are only generated when the association
supports dynamic address reconfiguration, e.g.

SCTP_ADDR_ADDED

,

SCTP_ADDR_REMOVED

, etc.

**All Implemented Interfaces:** Serializable

,

Comparable

<

PeerAddressChangeNotification.AddressChangeEvent

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PeerAddressChangeNotification.AddressChangeEvent
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
PeerAddressChangeNotification.AddressChangeEvent
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

#### Enum PeerAddressChangeNotification.AddressChangeEvent

java.lang.Object

- java.lang.Enum

<

PeerAddressChangeNotification.AddressChangeEvent

>
- - com.sun.nio.sctp.PeerAddressChangeNotification.AddressChangeEvent

java.lang.Enum

<

PeerAddressChangeNotification.AddressChangeEvent

>

- com.sun.nio.sctp.PeerAddressChangeNotification.AddressChangeEvent

com.sun.nio.sctp.PeerAddressChangeNotification.AddressChangeEvent

**All Implemented Interfaces:** Serializable

,

Comparable

<

PeerAddressChangeNotification.AddressChangeEvent

>

**Enclosing class:** PeerAddressChangeNotification

```java
public static enum
PeerAddressChangeNotification.AddressChangeEvent

extends
Enum
<
PeerAddressChangeNotification.AddressChangeEvent
>
```

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

Some of these events types are only generated when the association
supports dynamic address reconfiguration, e.g.

SCTP_ADDR_ADDED

,

SCTP_ADDR_REMOVED

, etc.

**Since:** 1.7

public static enum

PeerAddressChangeNotification.AddressChangeEvent

extends

Enum

<

PeerAddressChangeNotification.AddressChangeEvent

>

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

Some of these events types are only generated when the association
supports dynamic address reconfiguration, e.g.

SCTP_ADDR_ADDED

,

SCTP_ADDR_REMOVED

, etc.

Some of these events types are only generated when the association
supports dynamic address reconfiguration, e.g.

SCTP_ADDR_ADDED

,

SCTP_ADDR_REMOVED

, etc.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ADDR_ADDED

The address is now part of the association.

ADDR_AVAILABLE

This address is now reachable.

ADDR_CONFIRMED

This address has now been confirmed as a valid address.

ADDR_MADE_PRIMARY

This address has now been made to be the primary destination address.

ADDR_REMOVED

The address is no longer part of the association.

ADDR_UNREACHABLE

The address specified can no longer be reached.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PeerAddressChangeNotification.AddressChangeEvent

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PeerAddressChangeNotification.AddressChangeEvent

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

ADDR_ADDED

The address is now part of the association.

ADDR_AVAILABLE

This address is now reachable.

ADDR_CONFIRMED

This address has now been confirmed as a valid address.

ADDR_MADE_PRIMARY

This address has now been made to be the primary destination address.

ADDR_REMOVED

The address is no longer part of the association.

ADDR_UNREACHABLE

The address specified can no longer be reached.

---

#### Enum Constant Summary

The address is now part of the association.

This address is now reachable.

This address has now been confirmed as a valid address.

This address has now been made to be the primary destination address.

The address is no longer part of the association.

The address specified can no longer be reached.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PeerAddressChangeNotification.AddressChangeEvent

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

PeerAddressChangeNotification.AddressChangeEvent

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

- ADDR_AVAILABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_AVAILABLE
```

This address is now reachable.

- ADDR_UNREACHABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_UNREACHABLE
```

The address specified can no longer be reached. Any data sent to this
address is rerouted to an alternate until this address becomes reachable.

- ADDR_REMOVED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_REMOVED
```

The address is no longer part of the association.

- ADDR_ADDED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_ADDED
```

The address is now part of the association.

- ADDR_MADE_PRIMARY

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_MADE_PRIMARY
```

This address has now been made to be the primary destination address.

- ADDR_CONFIRMED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_CONFIRMED
```

This address has now been confirmed as a valid address.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
PeerAddressChangeNotification.AddressChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PeerAddressChangeNotification.AddressChangeEvent
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

- ADDR_AVAILABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_AVAILABLE
```

This address is now reachable.

- ADDR_UNREACHABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_UNREACHABLE
```

The address specified can no longer be reached. Any data sent to this
address is rerouted to an alternate until this address becomes reachable.

- ADDR_REMOVED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_REMOVED
```

The address is no longer part of the association.

- ADDR_ADDED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_ADDED
```

The address is now part of the association.

- ADDR_MADE_PRIMARY

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_MADE_PRIMARY
```

This address has now been made to be the primary destination address.

- ADDR_CONFIRMED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_CONFIRMED
```

This address has now been confirmed as a valid address.

---

#### Enum Constant Detail

ADDR_AVAILABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_AVAILABLE
```

This address is now reachable.

---

#### ADDR_AVAILABLE

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_AVAILABLE

This address is now reachable.

ADDR_UNREACHABLE

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_UNREACHABLE
```

The address specified can no longer be reached. Any data sent to this
address is rerouted to an alternate until this address becomes reachable.

---

#### ADDR_UNREACHABLE

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_UNREACHABLE

The address specified can no longer be reached. Any data sent to this
address is rerouted to an alternate until this address becomes reachable.

ADDR_REMOVED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_REMOVED
```

The address is no longer part of the association.

---

#### ADDR_REMOVED

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_REMOVED

The address is no longer part of the association.

ADDR_ADDED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_ADDED
```

The address is now part of the association.

---

#### ADDR_ADDED

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_ADDED

The address is now part of the association.

ADDR_MADE_PRIMARY

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_MADE_PRIMARY
```

This address has now been made to be the primary destination address.

---

#### ADDR_MADE_PRIMARY

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_MADE_PRIMARY

This address has now been made to be the primary destination address.

ADDR_CONFIRMED

```java
public static final
PeerAddressChangeNotification.AddressChangeEvent
ADDR_CONFIRMED
```

This address has now been confirmed as a valid address.

---

#### ADDR_CONFIRMED

public static final

PeerAddressChangeNotification.AddressChangeEvent

ADDR_CONFIRMED

This address has now been confirmed as a valid address.

Method Detail

- values

```java
public static
PeerAddressChangeNotification.AddressChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
PeerAddressChangeNotification.AddressChangeEvent
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
PeerAddressChangeNotification.AddressChangeEvent
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

PeerAddressChangeNotification.AddressChangeEvent

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);
```

for (PeerAddressChangeNotification.AddressChangeEvent c : PeerAddressChangeNotification.AddressChangeEvent.values())
System.out.println(c);

valueOf

```java
public static
PeerAddressChangeNotification.AddressChangeEvent
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

PeerAddressChangeNotification.AddressChangeEvent

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

