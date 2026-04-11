# Class HttpsParameters

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpsParameters.html`

### Class Description

```java
public abstract class
HttpsParameters

extends
Object
```

Represents the set of parameters for each https
connection negotiated with clients. One of these
is created and passed to

HttpsConfigurator.configure(HttpsParameters)

for every incoming https connection,
in order to determine the parameters to use.

The underlying SSL parameters may be established either
via the set/get methods of this class, or else via
a

SSLParameters

object. SSLParameters
is the preferred method, because in the future,
additional configuration capabilities may be added to that class, and
it is easier to determine the set of supported parameters and their
default values with SSLParameters. Also, if an SSLParameters object is
provided via

setSSLParameters(SSLParameters)

then those parameter settings
are used, and any settings made in this object are ignored.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpsParameters()

*No description found.*

---

### Method Details

#### public abstract
HttpsConfigurator
getHttpsConfigurator()

Returns the HttpsConfigurator for this HttpsParameters.

---

#### public abstract
InetSocketAddress
getClientAddress()

Returns the address of the remote client initiating the
connection.

---

#### public abstract void setSSLParameters​(
SSLParameters
params)

Sets the SSLParameters to use for this HttpsParameters.
The parameters must be supported by the SSLContext contained
by the HttpsConfigurator associated with this HttpsParameters.
If no parameters are set, then the default behavior is to use
the default parameters from the associated SSLContext.

**Parameters:**
- params

- the SSLParameters to set. If

null

then the existing parameters (if any) remain unchanged.

**Throws:**
- IllegalArgumentException

- if any of the parameters are
invalid or unsupported.

---

#### public
String
[] getCipherSuites()

Returns a copy of the array of ciphersuites or null if none
have been set.

**Returns:**
- a copy of the array of ciphersuites or null if none
have been set.

---

#### public void setCipherSuites​(
String
[] cipherSuites)

Sets the array of ciphersuites.

**Parameters:**
- cipherSuites

- the array of ciphersuites (or null)

---

#### public
String
[] getProtocols()

Returns a copy of the array of protocols or null if none
have been set.

**Returns:**
- a copy of the array of protocols or null if none
have been set.

---

#### public void setProtocols​(
String
[] protocols)

Sets the array of protocols.

**Parameters:**
- protocols

- the array of protocols (or null)

---

#### public boolean getWantClientAuth()

Returns whether client authentication should be requested.

**Returns:**
- whether client authentication should be requested.

---

#### public void setWantClientAuth​(boolean wantClientAuth)

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:**
- wantClientAuth

- whether client authentication should be requested

---

#### public boolean getNeedClientAuth()

Returns whether client authentication should be required.

**Returns:**
- whether client authentication should be required.

---

#### public void setNeedClientAuth​(boolean needClientAuth)

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:**
- needClientAuth

- whether client authentication should be required

---

### Additional Sections

#### Class HttpsParameters

java.lang.Object

- com.sun.net.httpserver.HttpsParameters

com.sun.net.httpserver.HttpsParameters

```java
public abstract class
HttpsParameters

extends
Object
```

Represents the set of parameters for each https
connection negotiated with clients. One of these
is created and passed to

HttpsConfigurator.configure(HttpsParameters)

for every incoming https connection,
in order to determine the parameters to use.

The underlying SSL parameters may be established either
via the set/get methods of this class, or else via
a

SSLParameters

object. SSLParameters
is the preferred method, because in the future,
additional configuration capabilities may be added to that class, and
it is easier to determine the set of supported parameters and their
default values with SSLParameters. Also, if an SSLParameters object is
provided via

setSSLParameters(SSLParameters)

then those parameter settings
are used, and any settings made in this object are ignored.

**Since:** 1.6

public abstract class

HttpsParameters

extends

Object

Represents the set of parameters for each https
connection negotiated with clients. One of these
is created and passed to

HttpsConfigurator.configure(HttpsParameters)

for every incoming https connection,
in order to determine the parameters to use.

The underlying SSL parameters may be established either
via the set/get methods of this class, or else via
a

SSLParameters

object. SSLParameters
is the preferred method, because in the future,
additional configuration capabilities may be added to that class, and
it is easier to determine the set of supported parameters and their
default values with SSLParameters. Also, if an SSLParameters object is
provided via

setSSLParameters(SSLParameters)

then those parameter settings
are used, and any settings made in this object are ignored.

The underlying SSL parameters may be established either
via the set/get methods of this class, or else via
a

SSLParameters

object. SSLParameters
is the preferred method, because in the future,
additional configuration capabilities may be added to that class, and
it is easier to determine the set of supported parameters and their
default values with SSLParameters. Also, if an SSLParameters object is
provided via

setSSLParameters(SSLParameters)

then those parameter settings
are used, and any settings made in this object are ignored.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsParameters

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

[]

getCipherSuites

()

Returns a copy of the array of ciphersuites or null if none
have been set.

abstract

InetSocketAddress

getClientAddress

()

Returns the address of the remote client initiating the
connection.

abstract

HttpsConfigurator

getHttpsConfigurator

()

Returns the HttpsConfigurator for this HttpsParameters.

boolean

getNeedClientAuth

()

Returns whether client authentication should be required.

String

[]

getProtocols

()

Returns a copy of the array of protocols or null if none
have been set.

boolean

getWantClientAuth

()

Returns whether client authentication should be requested.

void

setCipherSuites

​(

String

[] cipherSuites)

Sets the array of ciphersuites.

void

setNeedClientAuth

​(boolean needClientAuth)

Sets whether client authentication should be required.

void

setProtocols

​(

String

[] protocols)

Sets the array of protocols.

abstract void

setSSLParameters

​(

SSLParameters

params)

Sets the SSLParameters to use for this HttpsParameters.

void

setWantClientAuth

​(boolean wantClientAuth)

Sets whether client authentication should be requested.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsParameters

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

[]

getCipherSuites

()

Returns a copy of the array of ciphersuites or null if none
have been set.

abstract

InetSocketAddress

getClientAddress

()

Returns the address of the remote client initiating the
connection.

abstract

HttpsConfigurator

getHttpsConfigurator

()

Returns the HttpsConfigurator for this HttpsParameters.

boolean

getNeedClientAuth

()

Returns whether client authentication should be required.

String

[]

getProtocols

()

Returns a copy of the array of protocols or null if none
have been set.

boolean

getWantClientAuth

()

Returns whether client authentication should be requested.

void

setCipherSuites

​(

String

[] cipherSuites)

Sets the array of ciphersuites.

void

setNeedClientAuth

​(boolean needClientAuth)

Sets whether client authentication should be required.

void

setProtocols

​(

String

[] protocols)

Sets the array of protocols.

abstract void

setSSLParameters

​(

SSLParameters

params)

Sets the SSLParameters to use for this HttpsParameters.

void

setWantClientAuth

​(boolean wantClientAuth)

Sets whether client authentication should be requested.

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

Returns a copy of the array of ciphersuites or null if none
have been set.

Returns the address of the remote client initiating the
connection.

Returns the HttpsConfigurator for this HttpsParameters.

Returns whether client authentication should be required.

Returns a copy of the array of protocols or null if none
have been set.

Returns whether client authentication should be requested.

Sets the array of ciphersuites.

Sets whether client authentication should be required.

Sets the array of protocols.

Sets the SSLParameters to use for this HttpsParameters.

Sets whether client authentication should be requested.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HttpsParameters

```java
protected HttpsParameters()
```

============ METHOD DETAIL ==========

- Method Detail

- getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Returns the HttpsConfigurator for this HttpsParameters.

- getClientAddress

```java
public abstract
InetSocketAddress
getClientAddress()
```

Returns the address of the remote client initiating the
connection.

- setSSLParameters

```java
public abstract void setSSLParameters​(
SSLParameters
params)
```

Sets the SSLParameters to use for this HttpsParameters.
The parameters must be supported by the SSLContext contained
by the HttpsConfigurator associated with this HttpsParameters.
If no parameters are set, then the default behavior is to use
the default parameters from the associated SSLContext.

**Parameters:** params

- the SSLParameters to set. If

null

then the existing parameters (if any) remain unchanged.
**Throws:** IllegalArgumentException

- if any of the parameters are
invalid or unsupported.

- getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

- setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

- getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

- setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

- getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

- setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

- getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

- setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

Constructor Detail

- HttpsParameters

```java
protected HttpsParameters()
```

---

#### Constructor Detail

HttpsParameters

```java
protected HttpsParameters()
```

---

#### HttpsParameters

protected HttpsParameters()

Method Detail

- getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Returns the HttpsConfigurator for this HttpsParameters.

- getClientAddress

```java
public abstract
InetSocketAddress
getClientAddress()
```

Returns the address of the remote client initiating the
connection.

- setSSLParameters

```java
public abstract void setSSLParameters​(
SSLParameters
params)
```

Sets the SSLParameters to use for this HttpsParameters.
The parameters must be supported by the SSLContext contained
by the HttpsConfigurator associated with this HttpsParameters.
If no parameters are set, then the default behavior is to use
the default parameters from the associated SSLContext.

**Parameters:** params

- the SSLParameters to set. If

null

then the existing parameters (if any) remain unchanged.
**Throws:** IllegalArgumentException

- if any of the parameters are
invalid or unsupported.

- getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

- setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

- getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

- setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

- getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

- setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

- getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

- setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

---

#### Method Detail

getHttpsConfigurator

```java
public abstract
HttpsConfigurator
getHttpsConfigurator()
```

Returns the HttpsConfigurator for this HttpsParameters.

---

#### getHttpsConfigurator

public abstract

HttpsConfigurator

getHttpsConfigurator()

Returns the HttpsConfigurator for this HttpsParameters.

getClientAddress

```java
public abstract
InetSocketAddress
getClientAddress()
```

Returns the address of the remote client initiating the
connection.

---

#### getClientAddress

public abstract

InetSocketAddress

getClientAddress()

Returns the address of the remote client initiating the
connection.

setSSLParameters

```java
public abstract void setSSLParameters​(
SSLParameters
params)
```

Sets the SSLParameters to use for this HttpsParameters.
The parameters must be supported by the SSLContext contained
by the HttpsConfigurator associated with this HttpsParameters.
If no parameters are set, then the default behavior is to use
the default parameters from the associated SSLContext.

**Parameters:** params

- the SSLParameters to set. If

null

then the existing parameters (if any) remain unchanged.
**Throws:** IllegalArgumentException

- if any of the parameters are
invalid or unsupported.

---

#### setSSLParameters

public abstract void setSSLParameters​(

SSLParameters

params)

Sets the SSLParameters to use for this HttpsParameters.
The parameters must be supported by the SSLContext contained
by the HttpsConfigurator associated with this HttpsParameters.
If no parameters are set, then the default behavior is to use
the default parameters from the associated SSLContext.

getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

---

#### getCipherSuites

public

String

[] getCipherSuites()

Returns a copy of the array of ciphersuites or null if none
have been set.

setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

---

#### setCipherSuites

public void setCipherSuites​(

String

[] cipherSuites)

Sets the array of ciphersuites.

getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

---

#### getProtocols

public

String

[] getProtocols()

Returns a copy of the array of protocols or null if none
have been set.

setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

---

#### setProtocols

public void setProtocols​(

String

[] protocols)

Sets the array of protocols.

getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

---

#### getWantClientAuth

public boolean getWantClientAuth()

Returns whether client authentication should be requested.

setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

---

#### setWantClientAuth

public void setWantClientAuth​(boolean wantClientAuth)

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

---

#### getNeedClientAuth

public boolean getNeedClientAuth()

Returns whether client authentication should be required.

setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

---

#### setNeedClientAuth

public void setNeedClientAuth​(boolean needClientAuth)

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

---

