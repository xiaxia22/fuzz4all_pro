# Class HttpsConfigurator

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpsConfigurator.html`

### Class Description

```java
public class
HttpsConfigurator

extends
Object
```

This class is used to configure the https parameters for each incoming
https connection on a HttpsServer. Applications need to override
the

configure(HttpsParameters)

method in order to change
the default configuration.

The following

example

shows how this may be done:

```java
SSLContext sslContext = SSLContext.getInstance (....);
HttpsServer server = HttpsServer.create();

server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
public void configure (HttpsParameters params) {

// get the remote address if needed
InetSocketAddress remote = params.getClientAddress();

SSLContext c = getSSLContext();

// get the default parameters
SSLParameters sslparams = c.getDefaultSSLParameters();
if (remote.equals (...) ) {
// modify the default set for client x
}

params.setSSLParameters(sslparams);
}
});
```

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public HttpsConfigurator​(
SSLContext
context)

Creates an Https configuration, with the given SSLContext.

**Parameters:**
- context

- the SSLContext to use for this configurator

**Throws:**
- NullPointerException

- if no SSLContext supplied

---

### Method Details

#### public
SSLContext
getSSLContext()

Returns the SSLContext for this HttpsConfigurator.

**Returns:**
- the SSLContext

---

#### public void configure​(
HttpsParameters
params)

Called by the HttpsServer to configure the parameters
for a https connection currently being established.
The implementation of configure() must call

HttpsParameters.setSSLParameters(SSLParameters)

in order to set the SSL parameters for the connection.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

**Parameters:**
- params

- the HttpsParameters to be configured.

**Since:**
- 1.6

---

### Additional Sections

#### Class HttpsConfigurator

java.lang.Object

- com.sun.net.httpserver.HttpsConfigurator

com.sun.net.httpserver.HttpsConfigurator

```java
public class
HttpsConfigurator

extends
Object
```

This class is used to configure the https parameters for each incoming
https connection on a HttpsServer. Applications need to override
the

configure(HttpsParameters)

method in order to change
the default configuration.

The following

example

shows how this may be done:

```java
SSLContext sslContext = SSLContext.getInstance (....);
HttpsServer server = HttpsServer.create();

server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
public void configure (HttpsParameters params) {

// get the remote address if needed
InetSocketAddress remote = params.getClientAddress();

SSLContext c = getSSLContext();

// get the default parameters
SSLParameters sslparams = c.getDefaultSSLParameters();
if (remote.equals (...) ) {
// modify the default set for client x
}

params.setSSLParameters(sslparams);
}
});
```

**Since:** 1.6

public class

HttpsConfigurator

extends

Object

This class is used to configure the https parameters for each incoming
https connection on a HttpsServer. Applications need to override
the

configure(HttpsParameters)

method in order to change
the default configuration.

The following

example

shows how this may be done:

```java
SSLContext sslContext = SSLContext.getInstance (....);
HttpsServer server = HttpsServer.create();

server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
public void configure (HttpsParameters params) {

// get the remote address if needed
InetSocketAddress remote = params.getClientAddress();

SSLContext c = getSSLContext();

// get the default parameters
SSLParameters sslparams = c.getDefaultSSLParameters();
if (remote.equals (...) ) {
// modify the default set for client x
}

params.setSSLParameters(sslparams);
}
});
```

The following

example

shows how this may be done:

```java
SSLContext sslContext = SSLContext.getInstance (....);
HttpsServer server = HttpsServer.create();

server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
public void configure (HttpsParameters params) {

// get the remote address if needed
InetSocketAddress remote = params.getClientAddress();

SSLContext c = getSSLContext();

// get the default parameters
SSLParameters sslparams = c.getDefaultSSLParameters();
if (remote.equals (...) ) {
// modify the default set for client x
}

params.setSSLParameters(sslparams);
}
});
```

SSLContext sslContext = SSLContext.getInstance (....);
HttpsServer server = HttpsServer.create();

server.setHttpsConfigurator (new HttpsConfigurator(sslContext) {
public void configure (HttpsParameters params) {

// get the remote address if needed
InetSocketAddress remote = params.getClientAddress();

SSLContext c = getSSLContext();

// get the default parameters
SSLParameters sslparams = c.getDefaultSSLParameters();
if (remote.equals (...) ) {
// modify the default set for client x
}

params.setSSLParameters(sslparams);
}
});

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HttpsConfigurator

​(

SSLContext

context)

Creates an Https configuration, with the given SSLContext.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

configure

​(

HttpsParameters

params)

Called by the HttpsServer to configure the parameters
for a https connection currently being established.

SSLContext

getSSLContext

()

Returns the SSLContext for this HttpsConfigurator.

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

Constructor

Description

HttpsConfigurator

​(

SSLContext

context)

Creates an Https configuration, with the given SSLContext.

---

#### Constructor Summary

Creates an Https configuration, with the given SSLContext.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

configure

​(

HttpsParameters

params)

Called by the HttpsServer to configure the parameters
for a https connection currently being established.

SSLContext

getSSLContext

()

Returns the SSLContext for this HttpsConfigurator.

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

Called by the HttpsServer to configure the parameters
for a https connection currently being established.

Returns the SSLContext for this HttpsConfigurator.

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

- HttpsConfigurator

```java
public HttpsConfigurator​(
SSLContext
context)
```

Creates an Https configuration, with the given SSLContext.

**Parameters:** context

- the SSLContext to use for this configurator
**Throws:** NullPointerException

- if no SSLContext supplied

============ METHOD DETAIL ==========

- Method Detail

- getSSLContext

```java
public
SSLContext
getSSLContext()
```

Returns the SSLContext for this HttpsConfigurator.

**Returns:** the SSLContext

- configure

```java
public void configure​(
HttpsParameters
params)
```

Called by the HttpsServer to configure the parameters
for a https connection currently being established.
The implementation of configure() must call

HttpsParameters.setSSLParameters(SSLParameters)

in order to set the SSL parameters for the connection.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

**Parameters:** params

- the HttpsParameters to be configured.
**Since:** 1.6

Constructor Detail

- HttpsConfigurator

```java
public HttpsConfigurator​(
SSLContext
context)
```

Creates an Https configuration, with the given SSLContext.

**Parameters:** context

- the SSLContext to use for this configurator
**Throws:** NullPointerException

- if no SSLContext supplied

---

#### Constructor Detail

HttpsConfigurator

```java
public HttpsConfigurator​(
SSLContext
context)
```

Creates an Https configuration, with the given SSLContext.

**Parameters:** context

- the SSLContext to use for this configurator
**Throws:** NullPointerException

- if no SSLContext supplied

---

#### HttpsConfigurator

public HttpsConfigurator​(

SSLContext

context)

Creates an Https configuration, with the given SSLContext.

Method Detail

- getSSLContext

```java
public
SSLContext
getSSLContext()
```

Returns the SSLContext for this HttpsConfigurator.

**Returns:** the SSLContext

- configure

```java
public void configure​(
HttpsParameters
params)
```

Called by the HttpsServer to configure the parameters
for a https connection currently being established.
The implementation of configure() must call

HttpsParameters.setSSLParameters(SSLParameters)

in order to set the SSL parameters for the connection.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

**Parameters:** params

- the HttpsParameters to be configured.
**Since:** 1.6

---

#### Method Detail

getSSLContext

```java
public
SSLContext
getSSLContext()
```

Returns the SSLContext for this HttpsConfigurator.

**Returns:** the SSLContext

---

#### getSSLContext

public

SSLContext

getSSLContext()

Returns the SSLContext for this HttpsConfigurator.

configure

```java
public void configure​(
HttpsParameters
params)
```

Called by the HttpsServer to configure the parameters
for a https connection currently being established.
The implementation of configure() must call

HttpsParameters.setSSLParameters(SSLParameters)

in order to set the SSL parameters for the connection.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

**Parameters:** params

- the HttpsParameters to be configured.
**Since:** 1.6

---

#### configure

public void configure​(

HttpsParameters

params)

Called by the HttpsServer to configure the parameters
for a https connection currently being established.
The implementation of configure() must call

HttpsParameters.setSSLParameters(SSLParameters)

in order to set the SSL parameters for the connection.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

The default implementation of this method uses the
SSLParameters returned from

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

getSSLContext().getDefaultSSLParameters()

configure() may be overridden in order to modify this behavior.
See, the example

above

.

configure() may be overridden in order to modify this behavior.
See, the example

above

.

---

