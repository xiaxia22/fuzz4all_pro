# Interface SocketOption<T>

**Source:** `java.base\java\net\SocketOption.html`

### Class Description

```java
public interface
SocketOption<T>
```

A socket option associated with a socket.

In the

channels

package, the

NetworkChannel

interface defines the

setOption

and

getOption

methods to set and query the channel's socket options.

**Type Parameters:** T

- The type of the socket option value.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of the socket option.

**Returns:**
- the name of the socket option

---

#### Class
<
T
> type()

Returns the type of the socket option value.

**Returns:**
- the type of the socket option value

---

### Additional Sections

#### Interface SocketOption<T>

**Type Parameters:** T

- The type of the socket option value.

**All Known Subinterfaces:** SctpSocketOption

<T>

```java
public interface
SocketOption<T>
```

A socket option associated with a socket.

In the

channels

package, the

NetworkChannel

interface defines the

setOption

and

getOption

methods to set and query the channel's socket options.

**Since:** 1.7
**See Also:** StandardSocketOptions

public interface

SocketOption<T>

A socket option associated with a socket.

In the

channels

package, the

NetworkChannel

interface defines the

setOption

and

getOption

methods to set and query the channel's socket options.

In the

channels

package, the

NetworkChannel

interface defines the

setOption

and

getOption

methods to set and query the channel's socket options.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the socket option.

Class

<

T

>

type

()

Returns the type of the socket option value.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the socket option.

Class

<

T

>

type

()

Returns the type of the socket option value.

---

#### Method Summary

Returns the name of the socket option.

Returns the type of the socket option value.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the socket option.

**Returns:** the name of the socket option

- type

```java
Class
<
T
> type()
```

Returns the type of the socket option value.

**Returns:** the type of the socket option value

Method Detail

- name

```java
String
name()
```

Returns the name of the socket option.

**Returns:** the name of the socket option

- type

```java
Class
<
T
> type()
```

Returns the type of the socket option value.

**Returns:** the type of the socket option value

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the socket option.

**Returns:** the name of the socket option

---

#### name

String

name()

Returns the name of the socket option.

type

```java
Class
<
T
> type()
```

Returns the type of the socket option value.

**Returns:** the type of the socket option value

---

#### type

Class

<

T

> type()

Returns the type of the socket option value.

---

