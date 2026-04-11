# Enum SocketFlow.Status

**Source:** `jdk.net\jdk\net\SocketFlow.Status.html`

### Class Description

```java
public static enum
SocketFlow.Status

extends
Enum
<
SocketFlow.Status
>
```

Enumeration of the return values from the SO_FLOW_SLA
socket option. Both setting and getting the option return
one of these statuses, which reflect the state of socket's
flow.

**All Implemented Interfaces:** Serializable

,

Comparable

<

SocketFlow.Status

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SocketFlow.Status
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
SocketFlow.Status
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

#### Enum SocketFlow.Status

java.lang.Object

- java.lang.Enum

<

SocketFlow.Status

>
- - jdk.net.SocketFlow.Status

java.lang.Enum

<

SocketFlow.Status

>

- jdk.net.SocketFlow.Status

jdk.net.SocketFlow.Status

**All Implemented Interfaces:** Serializable

,

Comparable

<

SocketFlow.Status

>

**Enclosing class:** SocketFlow

```java
public static enum
SocketFlow.Status

extends
Enum
<
SocketFlow.Status
>
```

Enumeration of the return values from the SO_FLOW_SLA
socket option. Both setting and getting the option return
one of these statuses, which reflect the state of socket's
flow.

**Since:** 1.8

public static enum

SocketFlow.Status

extends

Enum

<

SocketFlow.Status

>

Enumeration of the return values from the SO_FLOW_SLA
socket option. Both setting and getting the option return
one of these statuses, which reflect the state of socket's
flow.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALREADY_CREATED

A flow already exists with identical attributes.

IN_PROGRESS

A flow is being created.

NO_PERMISSION

Caller has no permission to create flow.

NO_STATUS

Set or get socket option has not been called yet.

NOT_CONNECTED

Flow can not be created because socket is not connected.

NOT_SUPPORTED

Flow creation not supported for this socket.

OK

Flow successfully created.

OTHER

Some other unspecified error.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SocketFlow.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SocketFlow.Status

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

ALREADY_CREATED

A flow already exists with identical attributes.

IN_PROGRESS

A flow is being created.

NO_PERMISSION

Caller has no permission to create flow.

NO_STATUS

Set or get socket option has not been called yet.

NOT_CONNECTED

Flow can not be created because socket is not connected.

NOT_SUPPORTED

Flow creation not supported for this socket.

OK

Flow successfully created.

OTHER

Some other unspecified error.

---

#### Enum Constant Summary

A flow already exists with identical attributes.

A flow is being created.

Caller has no permission to create flow.

Set or get socket option has not been called yet.

Flow can not be created because socket is not connected.

Flow creation not supported for this socket.

Flow successfully created.

Some other unspecified error.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SocketFlow.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

SocketFlow.Status

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

- NO_STATUS

```java
public static final
SocketFlow.Status
NO_STATUS
```

Set or get socket option has not been called yet. Status
values can only be retrieved after calling set or get.

- OK

```java
public static final
SocketFlow.Status
OK
```

Flow successfully created.

- NO_PERMISSION

```java
public static final
SocketFlow.Status
NO_PERMISSION
```

Caller has no permission to create flow.

- NOT_CONNECTED

```java
public static final
SocketFlow.Status
NOT_CONNECTED
```

Flow can not be created because socket is not connected.

- NOT_SUPPORTED

```java
public static final
SocketFlow.Status
NOT_SUPPORTED
```

Flow creation not supported for this socket.

- ALREADY_CREATED

```java
public static final
SocketFlow.Status
ALREADY_CREATED
```

A flow already exists with identical attributes.

- IN_PROGRESS

```java
public static final
SocketFlow.Status
IN_PROGRESS
```

A flow is being created.

- OTHER

```java
public static final
SocketFlow.Status
OTHER
```

Some other unspecified error.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
SocketFlow.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SocketFlow.Status
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

- NO_STATUS

```java
public static final
SocketFlow.Status
NO_STATUS
```

Set or get socket option has not been called yet. Status
values can only be retrieved after calling set or get.

- OK

```java
public static final
SocketFlow.Status
OK
```

Flow successfully created.

- NO_PERMISSION

```java
public static final
SocketFlow.Status
NO_PERMISSION
```

Caller has no permission to create flow.

- NOT_CONNECTED

```java
public static final
SocketFlow.Status
NOT_CONNECTED
```

Flow can not be created because socket is not connected.

- NOT_SUPPORTED

```java
public static final
SocketFlow.Status
NOT_SUPPORTED
```

Flow creation not supported for this socket.

- ALREADY_CREATED

```java
public static final
SocketFlow.Status
ALREADY_CREATED
```

A flow already exists with identical attributes.

- IN_PROGRESS

```java
public static final
SocketFlow.Status
IN_PROGRESS
```

A flow is being created.

- OTHER

```java
public static final
SocketFlow.Status
OTHER
```

Some other unspecified error.

---

#### Enum Constant Detail

NO_STATUS

```java
public static final
SocketFlow.Status
NO_STATUS
```

Set or get socket option has not been called yet. Status
values can only be retrieved after calling set or get.

---

#### NO_STATUS

public static final

SocketFlow.Status

NO_STATUS

Set or get socket option has not been called yet. Status
values can only be retrieved after calling set or get.

OK

```java
public static final
SocketFlow.Status
OK
```

Flow successfully created.

---

#### OK

public static final

SocketFlow.Status

OK

Flow successfully created.

NO_PERMISSION

```java
public static final
SocketFlow.Status
NO_PERMISSION
```

Caller has no permission to create flow.

---

#### NO_PERMISSION

public static final

SocketFlow.Status

NO_PERMISSION

Caller has no permission to create flow.

NOT_CONNECTED

```java
public static final
SocketFlow.Status
NOT_CONNECTED
```

Flow can not be created because socket is not connected.

---

#### NOT_CONNECTED

public static final

SocketFlow.Status

NOT_CONNECTED

Flow can not be created because socket is not connected.

NOT_SUPPORTED

```java
public static final
SocketFlow.Status
NOT_SUPPORTED
```

Flow creation not supported for this socket.

---

#### NOT_SUPPORTED

public static final

SocketFlow.Status

NOT_SUPPORTED

Flow creation not supported for this socket.

ALREADY_CREATED

```java
public static final
SocketFlow.Status
ALREADY_CREATED
```

A flow already exists with identical attributes.

---

#### ALREADY_CREATED

public static final

SocketFlow.Status

ALREADY_CREATED

A flow already exists with identical attributes.

IN_PROGRESS

```java
public static final
SocketFlow.Status
IN_PROGRESS
```

A flow is being created.

---

#### IN_PROGRESS

public static final

SocketFlow.Status

IN_PROGRESS

A flow is being created.

OTHER

```java
public static final
SocketFlow.Status
OTHER
```

Some other unspecified error.

---

#### OTHER

public static final

SocketFlow.Status

OTHER

Some other unspecified error.

Method Detail

- values

```java
public static
SocketFlow.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
SocketFlow.Status
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
SocketFlow.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

SocketFlow.Status

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);
```

for (SocketFlow.Status c : SocketFlow.Status.values())
System.out.println(c);

valueOf

```java
public static
SocketFlow.Status
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

SocketFlow.Status

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

