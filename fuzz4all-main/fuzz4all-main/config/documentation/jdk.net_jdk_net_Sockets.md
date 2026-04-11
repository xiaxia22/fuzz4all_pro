# Class Sockets

**Source:** `jdk.net\jdk\net\Sockets.html`

### Class Description

```java
public class
Sockets

extends
Object
```

Defines static methods to set and get socket options defined by the

SocketOption

interface. All of the standard options defined
by

Socket

,

ServerSocket

, and

DatagramSocket

can be set this way, as well as additional
or platform specific options supported by each socket type.

The

supportedOptions(Class)

method can be called to determine
the complete set of options available (per socket type) on the
current system.

When a security manager is installed, some non-standard socket options
may require a security permission before being set or get.
The details are specified in

ExtendedSocketOptions

. No permission
is required for

StandardSocketOptions

.

**See Also:** NetworkChannel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static <T> void setOption​(
Socket
s,

SocketOption
<T> name,
T value)
throws
IOException

Sets the value of a socket option on a

Socket

**Parameters:**
- s

- the socket
- name

- The socket option
- value

- The value of the socket option. May be null for some
options.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IllegalArgumentException

- if the value is not valid for
the option.
- IOException

- if an I/O error occurs, or socket is closed.
- SecurityException

- if a security manager is set and the
caller does not have any required permission.
- NullPointerException

- if name is null

**See Also:**
- StandardSocketOptions

---

#### public static <T> T getOption​(
Socket
s,

SocketOption
<T> name)
throws
IOException

Returns the value of a socket option from a

Socket

**Parameters:**
- s

- the socket
- name

- The socket option

**Returns:**
- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IOException

- if an I/O error occurs
- SecurityException

- if a security manager is set and the
caller does not have any required permission.
- NullPointerException

- if name is null

**See Also:**
- StandardSocketOptions

---

#### public static <T> void setOption​(
ServerSocket
s,

SocketOption
<T> name,
T value)
throws
IOException

Sets the value of a socket option on a

ServerSocket

**Parameters:**
- s

- the socket
- name

- The socket option
- value

- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IllegalArgumentException

- if the value is not valid for
the option.
- IOException

- if an I/O error occurs
- NullPointerException

- if name is null
- SecurityException

- if a security manager is set and the
caller does not have any required permission.

**See Also:**
- StandardSocketOptions

---

#### public static <T> T getOption​(
ServerSocket
s,

SocketOption
<T> name)
throws
IOException

Returns the value of a socket option from a

ServerSocket

**Parameters:**
- s

- the socket
- name

- The socket option

**Returns:**
- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IOException

- if an I/O error occurs
- NullPointerException

- if name is null
- SecurityException

- if a security manager is set and the
caller does not have any required permission.

**See Also:**
- StandardSocketOptions

---

#### public static <T> void setOption​(
DatagramSocket
s,

SocketOption
<T> name,
T value)
throws
IOException

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

**Parameters:**
- s

- the socket
- name

- The socket option
- value

- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IllegalArgumentException

- if the value is not valid for
the option.
- IOException

- if an I/O error occurs
- NullPointerException

- if name is null
- SecurityException

- if a security manager is set and the
caller does not have any required permission.

**See Also:**
- StandardSocketOptions

---

#### public static <T> T getOption​(
DatagramSocket
s,

SocketOption
<T> name)
throws
IOException

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

**Parameters:**
- s

- the socket
- name

- The socket option

**Returns:**
- The value of the socket option.

**Throws:**
- UnsupportedOperationException

- if the socket does not support
the option.
- IOException

- if an I/O error occurs
- NullPointerException

- if name is null
- SecurityException

- if a security manager is set and the
caller does not have any required permission.

**See Also:**
- StandardSocketOptions

---

#### public static
Set
<
SocketOption
<?>> supportedOptions​(
Class
<?> socketType)

Returns a set of

SocketOption

s supported by the
given socket type. This set may include standard options and also
non standard extended options.

**Parameters:**
- socketType

- the type of java.net socket

**Throws:**
- IllegalArgumentException

- if socketType is not a valid
socket type from the java.net package.

---

### Additional Sections

#### Class Sockets

java.lang.Object

- jdk.net.Sockets

jdk.net.Sockets

```java
public class
Sockets

extends
Object
```

Defines static methods to set and get socket options defined by the

SocketOption

interface. All of the standard options defined
by

Socket

,

ServerSocket

, and

DatagramSocket

can be set this way, as well as additional
or platform specific options supported by each socket type.

The

supportedOptions(Class)

method can be called to determine
the complete set of options available (per socket type) on the
current system.

When a security manager is installed, some non-standard socket options
may require a security permission before being set or get.
The details are specified in

ExtendedSocketOptions

. No permission
is required for

StandardSocketOptions

.

**See Also:** NetworkChannel

public class

Sockets

extends

Object

Defines static methods to set and get socket options defined by the

SocketOption

interface. All of the standard options defined
by

Socket

,

ServerSocket

, and

DatagramSocket

can be set this way, as well as additional
or platform specific options supported by each socket type.

The

supportedOptions(Class)

method can be called to determine
the complete set of options available (per socket type) on the
current system.

When a security manager is installed, some non-standard socket options
may require a security permission before being set or get.
The details are specified in

ExtendedSocketOptions

. No permission
is required for

StandardSocketOptions

.

The

supportedOptions(Class)

method can be called to determine
the complete set of options available (per socket type) on the
current system.

When a security manager is installed, some non-standard socket options
may require a security permission before being set or get.
The details are specified in

ExtendedSocketOptions

. No permission
is required for

StandardSocketOptions

.

When a security manager is installed, some non-standard socket options
may require a security permission before being set or get.
The details are specified in

ExtendedSocketOptions

. No permission
is required for

StandardSocketOptions

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static <T> T

getOption

​(

DatagramSocket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

static <T> T

getOption

​(

ServerSocket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

ServerSocket

static <T> T

getOption

​(

Socket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

Socket

static <T> void

setOption

​(

DatagramSocket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

static <T> void

setOption

​(

ServerSocket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

ServerSocket

static <T> void

setOption

​(

Socket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

Socket

static

Set

<

SocketOption

<?>>

supportedOptions

​(

Class

<?> socketType)

Returns a set of

SocketOption

s supported by the
given socket type.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static <T> T

getOption

​(

DatagramSocket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

static <T> T

getOption

​(

ServerSocket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

ServerSocket

static <T> T

getOption

​(

Socket

s,

SocketOption

<T> name)

Returns the value of a socket option from a

Socket

static <T> void

setOption

​(

DatagramSocket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

static <T> void

setOption

​(

ServerSocket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

ServerSocket

static <T> void

setOption

​(

Socket

s,

SocketOption

<T> name,
T value)

Sets the value of a socket option on a

Socket

static

Set

<

SocketOption

<?>>

supportedOptions

​(

Class

<?> socketType)

Returns a set of

SocketOption

s supported by the
given socket type.

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

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

Returns the value of a socket option from a

ServerSocket

Returns the value of a socket option from a

Socket

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

Sets the value of a socket option on a

ServerSocket

Sets the value of a socket option on a

Socket

Returns a set of

SocketOption

s supported by the
given socket type.

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

============ METHOD DETAIL ==========

- Method Detail

- setOption

```java
public static <T> void setOption​(
Socket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. May be null for some
options.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or socket is closed.
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
Socket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

- setOption

```java
public static <T> void setOption​(
ServerSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
ServerSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- setOption

```java
public static <T> void setOption​(
DatagramSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
DatagramSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- supportedOptions

```java
public static
Set
<
SocketOption
<?>> supportedOptions​(
Class
<?> socketType)
```

Returns a set of

SocketOption

s supported by the
given socket type. This set may include standard options and also
non standard extended options.

**Parameters:** socketType

- the type of java.net socket
**Throws:** IllegalArgumentException

- if socketType is not a valid
socket type from the java.net package.

Method Detail

- setOption

```java
public static <T> void setOption​(
Socket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. May be null for some
options.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or socket is closed.
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
Socket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

- setOption

```java
public static <T> void setOption​(
ServerSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
ServerSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- setOption

```java
public static <T> void setOption​(
DatagramSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- getOption

```java
public static <T> T getOption​(
DatagramSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

- supportedOptions

```java
public static
Set
<
SocketOption
<?>> supportedOptions​(
Class
<?> socketType)
```

Returns a set of

SocketOption

s supported by the
given socket type. This set may include standard options and also
non standard extended options.

**Parameters:** socketType

- the type of java.net socket
**Throws:** IllegalArgumentException

- if socketType is not a valid
socket type from the java.net package.

---

#### Method Detail

setOption

```java
public static <T> void setOption​(
Socket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option. May be null for some
options.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs, or socket is closed.
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

---

#### setOption

public static <T> void setOption​(

Socket

s,

SocketOption

<T> name,
T value)
throws

IOException

Sets the value of a socket option on a

Socket

getOption

```java
public static <T> T getOption​(
Socket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

Socket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**Throws:** NullPointerException

- if name is null
**See Also:** StandardSocketOptions

---

#### getOption

public static <T> T getOption​(

Socket

s,

SocketOption

<T> name)
throws

IOException

Returns the value of a socket option from a

Socket

setOption

```java
public static <T> void setOption​(
ServerSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

---

#### setOption

public static <T> void setOption​(

ServerSocket

s,

SocketOption

<T> name,
T value)
throws

IOException

Sets the value of a socket option on a

ServerSocket

getOption

```java
public static <T> T getOption​(
ServerSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

ServerSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

---

#### getOption

public static <T> T getOption​(

ServerSocket

s,

SocketOption

<T> name)
throws

IOException

Returns the value of a socket option from a

ServerSocket

setOption

```java
public static <T> void setOption​(
DatagramSocket
s,

SocketOption
<T> name,
T value)
throws
IOException
```

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Parameters:** value

- The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IllegalArgumentException

- if the value is not valid for
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

---

#### setOption

public static <T> void setOption​(

DatagramSocket

s,

SocketOption

<T> name,
T value)
throws

IOException

Sets the value of a socket option on a

DatagramSocket

or

MulticastSocket

getOption

```java
public static <T> T getOption​(
DatagramSocket
s,

SocketOption
<T> name)
throws
IOException
```

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

**Parameters:** s

- the socket
**Parameters:** name

- The socket option
**Returns:** The value of the socket option.
**Throws:** UnsupportedOperationException

- if the socket does not support
the option.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if name is null
**Throws:** SecurityException

- if a security manager is set and the
caller does not have any required permission.
**See Also:** StandardSocketOptions

---

#### getOption

public static <T> T getOption​(

DatagramSocket

s,

SocketOption

<T> name)
throws

IOException

Returns the value of a socket option from a

DatagramSocket

or

MulticastSocket

supportedOptions

```java
public static
Set
<
SocketOption
<?>> supportedOptions​(
Class
<?> socketType)
```

Returns a set of

SocketOption

s supported by the
given socket type. This set may include standard options and also
non standard extended options.

**Parameters:** socketType

- the type of java.net socket
**Throws:** IllegalArgumentException

- if socketType is not a valid
socket type from the java.net package.

---

#### supportedOptions

public static

Set

<

SocketOption

<?>> supportedOptions​(

Class

<?> socketType)

Returns a set of

SocketOption

s supported by the
given socket type. This set may include standard options and also
non standard extended options.

---

