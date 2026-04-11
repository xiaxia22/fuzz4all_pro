# Class SocketFlow

**Source:** `jdk.net\jdk\net\SocketFlow.html`

### Class Description

```java
public class
SocketFlow

extends
Object
```

Represents the service level properties for the platform specific socket
option

ExtendedSocketOptions.SO_FLOW_SLA

.

The priority and bandwidth parameters must be set before
setting the socket option.

When the

SO_FLOW_SLA

option is set then it may not take effect
immediately. If the value of the socket option is obtained with

getOption()

then the status may be returned as

INPROGRESS

until it takes effect. The priority and bandwidth values are only valid when
the status is returned as OK.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

**Since:** 1.8

---

### Field Details

#### @Native

public static final int UNSET

**See Also:**
- Constant Field Values

---

#### @Native

public static final int NORMAL_PRIORITY

**See Also:**
- Constant Field Values

---

#### @Native

public static final int HIGH_PRIORITY

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
SocketFlow
create()

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

---

#### public
SocketFlow
priority​(int priority)

Sets this SocketFlow's priority. Must be either NORMAL_PRIORITY
HIGH_PRIORITY. If not set, a flow's priority is normal.

**Throws:**
- IllegalArgumentException

- if priority is not NORMAL_PRIORITY or
HIGH_PRIORITY.

---

#### public
SocketFlow
bandwidth​(long bandwidth)

Sets this SocketFlow's bandwidth. Must be greater than or equal to zero.
A value of zero drops all packets for the socket.

**Throws:**
- IllegalArgumentException

- if bandwidth is less than zero.

---

#### public int priority()

Returns this SocketFlow's priority.

---

#### public long bandwidth()

Returns this SocketFlow's bandwidth.

**Returns:**
- this SocketFlow's bandwidth, or

-1

if status is not OK.

---

#### public
SocketFlow.Status
status()

Returns the Status value of this SocketFlow. NO_STATUS is returned
if the object was not used in a call to set or get the option.

---

### Additional Sections

#### Class SocketFlow

java.lang.Object

- jdk.net.SocketFlow

jdk.net.SocketFlow

```java
public class
SocketFlow

extends
Object
```

Represents the service level properties for the platform specific socket
option

ExtendedSocketOptions.SO_FLOW_SLA

.

The priority and bandwidth parameters must be set before
setting the socket option.

When the

SO_FLOW_SLA

option is set then it may not take effect
immediately. If the value of the socket option is obtained with

getOption()

then the status may be returned as

INPROGRESS

until it takes effect. The priority and bandwidth values are only valid when
the status is returned as OK.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

**Since:** 1.8

public class

SocketFlow

extends

Object

Represents the service level properties for the platform specific socket
option

ExtendedSocketOptions.SO_FLOW_SLA

.

The priority and bandwidth parameters must be set before
setting the socket option.

When the

SO_FLOW_SLA

option is set then it may not take effect
immediately. If the value of the socket option is obtained with

getOption()

then the status may be returned as

INPROGRESS

until it takes effect. The priority and bandwidth values are only valid when
the status is returned as OK.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

The priority and bandwidth parameters must be set before
setting the socket option.

When the

SO_FLOW_SLA

option is set then it may not take effect
immediately. If the value of the socket option is obtained with

getOption()

then the status may be returned as

INPROGRESS

until it takes effect. The priority and bandwidth values are only valid when
the status is returned as OK.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

When the

SO_FLOW_SLA

option is set then it may not take effect
immediately. If the value of the socket option is obtained with

getOption()

then the status may be returned as

INPROGRESS

until it takes effect. The priority and bandwidth values are only valid when
the status is returned as OK.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

When a security manager is installed, a

NetworkPermission

is required to set or get this option.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SocketFlow.Status

Enumeration of the return values from the SO_FLOW_SLA
socket option.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

HIGH_PRIORITY

static int

NORMAL_PRIORITY

static int

UNSET

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

bandwidth

()

Returns this SocketFlow's bandwidth.

SocketFlow

bandwidth

​(long bandwidth)

Sets this SocketFlow's bandwidth.

static

SocketFlow

create

()

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

int

priority

()

Returns this SocketFlow's priority.

SocketFlow

priority

​(int priority)

Sets this SocketFlow's priority.

SocketFlow.Status

status

()

Returns the Status value of this SocketFlow.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SocketFlow.Status

Enumeration of the return values from the SO_FLOW_SLA
socket option.

---

#### Nested Class Summary

Enumeration of the return values from the SO_FLOW_SLA
socket option.

Field Summary

Fields

Modifier and Type

Field

Description

static int

HIGH_PRIORITY

static int

NORMAL_PRIORITY

static int

UNSET

---

#### Field Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

bandwidth

()

Returns this SocketFlow's bandwidth.

SocketFlow

bandwidth

​(long bandwidth)

Sets this SocketFlow's bandwidth.

static

SocketFlow

create

()

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

int

priority

()

Returns this SocketFlow's priority.

SocketFlow

priority

​(int priority)

Sets this SocketFlow's priority.

SocketFlow.Status

status

()

Returns the Status value of this SocketFlow.

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

Returns this SocketFlow's bandwidth.

Sets this SocketFlow's bandwidth.

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

Returns this SocketFlow's priority.

Sets this SocketFlow's priority.

Returns the Status value of this SocketFlow.

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

============ FIELD DETAIL ===========

- Field Detail

- UNSET

```java
@Native

public static final int UNSET
```

**See Also:** Constant Field Values

- NORMAL_PRIORITY

```java
@Native

public static final int NORMAL_PRIORITY
```

**See Also:** Constant Field Values

- HIGH_PRIORITY

```java
@Native

public static final int HIGH_PRIORITY
```

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
SocketFlow
create()
```

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

- priority

```java
public
SocketFlow
priority​(int priority)
```

Sets this SocketFlow's priority. Must be either NORMAL_PRIORITY
HIGH_PRIORITY. If not set, a flow's priority is normal.

**Throws:** IllegalArgumentException

- if priority is not NORMAL_PRIORITY or
HIGH_PRIORITY.

- bandwidth

```java
public
SocketFlow
bandwidth​(long bandwidth)
```

Sets this SocketFlow's bandwidth. Must be greater than or equal to zero.
A value of zero drops all packets for the socket.

**Throws:** IllegalArgumentException

- if bandwidth is less than zero.

- priority

```java
public int priority()
```

Returns this SocketFlow's priority.

- bandwidth

```java
public long bandwidth()
```

Returns this SocketFlow's bandwidth.

**Returns:** this SocketFlow's bandwidth, or

-1

if status is not OK.

- status

```java
public
SocketFlow.Status
status()
```

Returns the Status value of this SocketFlow. NO_STATUS is returned
if the object was not used in a call to set or get the option.

Field Detail

- UNSET

```java
@Native

public static final int UNSET
```

**See Also:** Constant Field Values

- NORMAL_PRIORITY

```java
@Native

public static final int NORMAL_PRIORITY
```

**See Also:** Constant Field Values

- HIGH_PRIORITY

```java
@Native

public static final int HIGH_PRIORITY
```

**See Also:** Constant Field Values

---

#### Field Detail

UNSET

```java
@Native

public static final int UNSET
```

**See Also:** Constant Field Values

---

#### UNSET

@Native

public static final int UNSET

NORMAL_PRIORITY

```java
@Native

public static final int NORMAL_PRIORITY
```

**See Also:** Constant Field Values

---

#### NORMAL_PRIORITY

@Native

public static final int NORMAL_PRIORITY

HIGH_PRIORITY

```java
@Native

public static final int HIGH_PRIORITY
```

**See Also:** Constant Field Values

---

#### HIGH_PRIORITY

@Native

public static final int HIGH_PRIORITY

Method Detail

- create

```java
public static
SocketFlow
create()
```

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

- priority

```java
public
SocketFlow
priority​(int priority)
```

Sets this SocketFlow's priority. Must be either NORMAL_PRIORITY
HIGH_PRIORITY. If not set, a flow's priority is normal.

**Throws:** IllegalArgumentException

- if priority is not NORMAL_PRIORITY or
HIGH_PRIORITY.

- bandwidth

```java
public
SocketFlow
bandwidth​(long bandwidth)
```

Sets this SocketFlow's bandwidth. Must be greater than or equal to zero.
A value of zero drops all packets for the socket.

**Throws:** IllegalArgumentException

- if bandwidth is less than zero.

- priority

```java
public int priority()
```

Returns this SocketFlow's priority.

- bandwidth

```java
public long bandwidth()
```

Returns this SocketFlow's bandwidth.

**Returns:** this SocketFlow's bandwidth, or

-1

if status is not OK.

- status

```java
public
SocketFlow.Status
status()
```

Returns the Status value of this SocketFlow. NO_STATUS is returned
if the object was not used in a call to set or get the option.

---

#### Method Detail

create

```java
public static
SocketFlow
create()
```

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

---

#### create

public static

SocketFlow

create()

Creates a new SocketFlow that can be used to set the SO_FLOW_SLA
socket option and create a socket flow.

priority

```java
public
SocketFlow
priority​(int priority)
```

Sets this SocketFlow's priority. Must be either NORMAL_PRIORITY
HIGH_PRIORITY. If not set, a flow's priority is normal.

**Throws:** IllegalArgumentException

- if priority is not NORMAL_PRIORITY or
HIGH_PRIORITY.

---

#### priority

public

SocketFlow

priority​(int priority)

Sets this SocketFlow's priority. Must be either NORMAL_PRIORITY
HIGH_PRIORITY. If not set, a flow's priority is normal.

bandwidth

```java
public
SocketFlow
bandwidth​(long bandwidth)
```

Sets this SocketFlow's bandwidth. Must be greater than or equal to zero.
A value of zero drops all packets for the socket.

**Throws:** IllegalArgumentException

- if bandwidth is less than zero.

---

#### bandwidth

public

SocketFlow

bandwidth​(long bandwidth)

Sets this SocketFlow's bandwidth. Must be greater than or equal to zero.
A value of zero drops all packets for the socket.

priority

```java
public int priority()
```

Returns this SocketFlow's priority.

---

#### priority

public int priority()

Returns this SocketFlow's priority.

bandwidth

```java
public long bandwidth()
```

Returns this SocketFlow's bandwidth.

**Returns:** this SocketFlow's bandwidth, or

-1

if status is not OK.

---

#### bandwidth

public long bandwidth()

Returns this SocketFlow's bandwidth.

status

```java
public
SocketFlow.Status
status()
```

Returns the Status value of this SocketFlow. NO_STATUS is returned
if the object was not used in a call to set or get the option.

---

#### status

public

SocketFlow.Status

status()

Returns the Status value of this SocketFlow. NO_STATUS is returned
if the object was not used in a call to set or get the option.

---

