# Class Proxy

**Source:** `java.base\java\net\Proxy.html`

### Class Description

```java
public class
Proxy

extends
Object
```

This class represents a proxy setting, typically a type (http, socks) and
a socket address.
A

Proxy

is an immutable object.

**Since:** 1.5
**See Also:** ProxySelector

---

### Field Details

#### public static final
Proxy
NO_PROXY

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.
Used, for instance, to create sockets bypassing any other global
proxy settings (like SOCKS):

Socket s = new Socket(Proxy.NO_PROXY);

---

### Constructor Details

#### public Proxy​(
Proxy.Type
type,

SocketAddress
sa)

Creates an entry representing a PROXY connection.
Certain combinations are illegal. For instance, for types Http, and
Socks, a SocketAddress

must

be provided.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

**Parameters:**
- type

- the

Type

of the proxy
- sa

- the

SocketAddress

for that proxy

**Throws:**
- IllegalArgumentException

- when the type and the address are
incompatible

---

### Method Details

#### public
Proxy.Type
type()

Returns the proxy type.

**Returns:**
- a Type representing the proxy type

---

#### public
SocketAddress
address()

Returns the socket address of the proxy, or

null

if its a direct connection.

**Returns:**
- a

SocketAddress

representing the socket end
point of the proxy

---

#### public
String
toString()

Constructs a string representation of this Proxy.
This String is constructed by calling toString() on its type
and concatenating " @ " and the toString() result from its address
if its type is not

DIRECT

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object.

---

#### public final boolean equals​(
Object
obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same proxy as
this object.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare against.

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- InetSocketAddress.equals(java.lang.Object)

---

#### public final int hashCode()

Returns a hashcode for this Proxy.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this Proxy.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class Proxy

java.lang.Object

- java.net.Proxy

java.net.Proxy

```java
public class
Proxy

extends
Object
```

This class represents a proxy setting, typically a type (http, socks) and
a socket address.
A

Proxy

is an immutable object.

**Since:** 1.5
**See Also:** ProxySelector

public class

Proxy

extends

Object

This class represents a proxy setting, typically a type (http, socks) and
a socket address.
A

Proxy

is an immutable object.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Proxy.Type

Represents the proxy type.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Proxy

NO_PROXY

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Proxy

​(

Proxy.Type

type,

SocketAddress

sa)

Creates an entry representing a PROXY connection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SocketAddress

address

()

Returns the socket address of the proxy, or

null

if its a direct connection.

boolean

equals

​(

Object

obj)

Compares this object against the specified object.

int

hashCode

()

Returns a hashcode for this Proxy.

String

toString

()

Constructs a string representation of this Proxy.

Proxy.Type

type

()

Returns the proxy type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Proxy.Type

Represents the proxy type.

---

#### Nested Class Summary

Represents the proxy type.

Field Summary

Fields

Modifier and Type

Field

Description

static

Proxy

NO_PROXY

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.

---

#### Field Summary

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.

Constructor Summary

Constructors

Constructor

Description

Proxy

​(

Proxy.Type

type,

SocketAddress

sa)

Creates an entry representing a PROXY connection.

---

#### Constructor Summary

Creates an entry representing a PROXY connection.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SocketAddress

address

()

Returns the socket address of the proxy, or

null

if its a direct connection.

boolean

equals

​(

Object

obj)

Compares this object against the specified object.

int

hashCode

()

Returns a hashcode for this Proxy.

String

toString

()

Constructs a string representation of this Proxy.

Proxy.Type

type

()

Returns the proxy type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Returns the socket address of the proxy, or

null

if its a direct connection.

Compares this object against the specified object.

Returns a hashcode for this Proxy.

Constructs a string representation of this Proxy.

Returns the proxy type.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

============ FIELD DETAIL ===========

- Field Detail

- NO_PROXY

```java
public static final
Proxy
NO_PROXY
```

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.
Used, for instance, to create sockets bypassing any other global
proxy settings (like SOCKS):

Socket s = new Socket(Proxy.NO_PROXY);

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Proxy

```java
public Proxy​(
Proxy.Type
type,

SocketAddress
sa)
```

Creates an entry representing a PROXY connection.
Certain combinations are illegal. For instance, for types Http, and
Socks, a SocketAddress

must

be provided.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

**Parameters:** type

- the

Type

of the proxy
**Parameters:** sa

- the

SocketAddress

for that proxy
**Throws:** IllegalArgumentException

- when the type and the address are
incompatible

============ METHOD DETAIL ==========

- Method Detail

- type

```java
public
Proxy.Type
type()
```

Returns the proxy type.

**Returns:** a Type representing the proxy type

- address

```java
public
SocketAddress
address()
```

Returns the socket address of the proxy, or

null

if its a direct connection.

**Returns:** a

SocketAddress

representing the socket end
point of the proxy

- toString

```java
public
String
toString()
```

Constructs a string representation of this Proxy.
This String is constructed by calling toString() on its type
and concatenating " @ " and the toString() result from its address
if its type is not

DIRECT

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same proxy as
this object.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetSocketAddress.equals(java.lang.Object)

- hashCode

```java
public final int hashCode()
```

Returns a hashcode for this Proxy.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Proxy.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- NO_PROXY

```java
public static final
Proxy
NO_PROXY
```

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.
Used, for instance, to create sockets bypassing any other global
proxy settings (like SOCKS):

Socket s = new Socket(Proxy.NO_PROXY);

---

#### Field Detail

NO_PROXY

```java
public static final
Proxy
NO_PROXY
```

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.
Used, for instance, to create sockets bypassing any other global
proxy settings (like SOCKS):

Socket s = new Socket(Proxy.NO_PROXY);

---

#### NO_PROXY

public static final

Proxy

NO_PROXY

A proxy setting that represents a

DIRECT

connection,
basically telling the protocol handler not to use any proxying.
Used, for instance, to create sockets bypassing any other global
proxy settings (like SOCKS):

Socket s = new Socket(Proxy.NO_PROXY);

Socket s = new Socket(Proxy.NO_PROXY);

Constructor Detail

- Proxy

```java
public Proxy​(
Proxy.Type
type,

SocketAddress
sa)
```

Creates an entry representing a PROXY connection.
Certain combinations are illegal. For instance, for types Http, and
Socks, a SocketAddress

must

be provided.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

**Parameters:** type

- the

Type

of the proxy
**Parameters:** sa

- the

SocketAddress

for that proxy
**Throws:** IllegalArgumentException

- when the type and the address are
incompatible

---

#### Constructor Detail

Proxy

```java
public Proxy​(
Proxy.Type
type,

SocketAddress
sa)
```

Creates an entry representing a PROXY connection.
Certain combinations are illegal. For instance, for types Http, and
Socks, a SocketAddress

must

be provided.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

**Parameters:** type

- the

Type

of the proxy
**Parameters:** sa

- the

SocketAddress

for that proxy
**Throws:** IllegalArgumentException

- when the type and the address are
incompatible

---

#### Proxy

public Proxy​(

Proxy.Type

type,

SocketAddress

sa)

Creates an entry representing a PROXY connection.
Certain combinations are illegal. For instance, for types Http, and
Socks, a SocketAddress

must

be provided.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

Use the

Proxy.NO_PROXY

constant
for representing a direct connection.

Method Detail

- type

```java
public
Proxy.Type
type()
```

Returns the proxy type.

**Returns:** a Type representing the proxy type

- address

```java
public
SocketAddress
address()
```

Returns the socket address of the proxy, or

null

if its a direct connection.

**Returns:** a

SocketAddress

representing the socket end
point of the proxy

- toString

```java
public
String
toString()
```

Constructs a string representation of this Proxy.
This String is constructed by calling toString() on its type
and concatenating " @ " and the toString() result from its address
if its type is not

DIRECT

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same proxy as
this object.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetSocketAddress.equals(java.lang.Object)

- hashCode

```java
public final int hashCode()
```

Returns a hashcode for this Proxy.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Proxy.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

type

```java
public
Proxy.Type
type()
```

Returns the proxy type.

**Returns:** a Type representing the proxy type

---

#### type

public

Proxy.Type

type()

Returns the proxy type.

address

```java
public
SocketAddress
address()
```

Returns the socket address of the proxy, or

null

if its a direct connection.

**Returns:** a

SocketAddress

representing the socket end
point of the proxy

---

#### address

public

SocketAddress

address()

Returns the socket address of the proxy, or

null

if its a direct connection.

toString

```java
public
String
toString()
```

Constructs a string representation of this Proxy.
This String is constructed by calling toString() on its type
and concatenating " @ " and the toString() result from its address
if its type is not

DIRECT

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

---

#### toString

public

String

toString()

Constructs a string representation of this Proxy.
This String is constructed by calling toString() on its type
and concatenating " @ " and the toString() result from its address
if its type is not

DIRECT

.

equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same proxy as
this object.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetSocketAddress.equals(java.lang.Object)

---

#### equals

public final boolean equals​(

Object

obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same proxy as
this object.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

Two instances of

Proxy

represent the same
address if both the SocketAddresses and type are equal.

hashCode

```java
public final int hashCode()
```

Returns a hashcode for this Proxy.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Proxy.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hashcode for this Proxy.

---

