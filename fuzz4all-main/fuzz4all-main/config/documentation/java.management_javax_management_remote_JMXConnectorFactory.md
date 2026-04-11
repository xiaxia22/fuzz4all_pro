# Class JMXConnectorFactory

**Source:** `java.management\javax\management\remote\JMXConnectorFactory.html`

### Class Description

```java
public class
JMXConnectorFactory

extends
Object
```

Factory to create JMX API connector clients. There
are no instances of this class.

Connections are usually made using the

connect

method of this class. More
advanced applications can separate the creation of the connector
client, using

newJMXConnector

and the establishment of the connection itself, using

JMXConnector.connect(Map)

.

Each client is created by an instance of

JMXConnectorProvider

. This instance is found as follows. Suppose
the given

JMXServiceURL

looks like

"service:jmx:

protocol

:

remainder

"

.
Then the factory will attempt to find the appropriate

JMXConnectorProvider

for

protocol

. Each
occurrence of the character

+

or

-

in

protocol

is replaced by

.

or

_

, respectively.

A

provider package list

is searched for as follows:

- If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.pkgs

then the
associated value is the provider package list.

Otherwise, if the system property

jmx.remote.protocol.provider.pkgs

exists, then its value
is the provider package list.

Otherwise, there is no provider package list.

The provider package list is a string that is interpreted as a
list of non-empty Java package names separated by vertical bars
(

|

). If the string is empty, then so is the provider
package list. If the provider package list is not a String, or if
it contains an element that is an empty string, a

JMXProviderException

is thrown.

If the provider package list exists and is not empty, then for
each element

pkg

of the list, the factory
will attempt to load the class

pkg

.

protocol

.ClientProvider

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.class.loader

then the
associated value is the class loader to use to load the provider.
If the associated value is not an instance of

ClassLoader

, an

IllegalArgumentException

is thrown.

If the

jmx.remote.protocol.provider.class.loader

key is not present in the

environment

parameter, the
calling thread's context class loader is used.

If the attempt to load this class produces a

ClassNotFoundException

, the search for a handler continues with
the next element of the list.

Otherwise, a problem with the provider found is signalled by a

JMXProviderException

whose

cause

indicates the underlying
exception, as follows:

- if the attempt to load the class produces an exception other
than

ClassNotFoundException

, that is the

cause

;

if

Class.newInstance()

for the class produces an
exception, that is the

cause

.

If no provider is found by the above steps, including the
default case where there is no provider package list, then the
implementation will use its own provider for

protocol

, or it will throw a

MalformedURLException

if there is none. An
implementation may choose to find providers by other means. For
example, it may support

service providers

,
where the service interface is

JMXConnectorProvider

.

Every implementation must support the RMI connector protocol with
the default RMI transport, specified with string

rmi

.

Once a provider is found, the result of the

newJMXConnector

method is the result of calling

newJMXConnector

on the provider.

The

Map

parameter passed to the

JMXConnectorProvider

is a new read-only

Map

that contains all the entries that were in the

environment

parameter to

JMXConnectorFactory.newJMXConnector

, if there was one.
Additionally, if the

jmx.remote.protocol.provider.class.loader

key is not
present in the

environment

parameter, it is added to
the new read-only

Map

. The associated value is the
calling thread's context class loader.

**Since:** 1.5

---

### Field Details

#### public static final
String
DEFAULT_CLASS_LOADER

Name of the attribute that specifies the default class
loader. This class loader is used to deserialize return values and
exceptions from remote

MBeanServerConnection

calls. The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:**
- Constant Field Values

---

#### public static final
String
PROTOCOL_PROVIDER_PACKAGES

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.
The value associated with this attribute is a string with
package names separated by vertical bars (

|

).

**See Also:**
- Constant Field Values

---

#### public static final
String
PROTOCOL_PROVIDER_CLASS_LOADER

Name of the attribute that specifies the class
loader for loading protocol providers.
The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
JMXConnector
connect​(
JMXServiceURL
serviceURL)
throws
IOException

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

**Parameters:**
- serviceURL

- the address of the connector server to
connect to.

**Returns:**
- a

JMXConnector

whose

connect

method has been called.

**Throws:**
- NullPointerException

- if

serviceURL

is null.
- IOException

- if the connector client or the
connection cannot be made because of a communication problem.
- SecurityException

- if the connection cannot be made
for security reasons.

---

#### public static
JMXConnector
connect​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException

Creates a connection to the connector server at the given
address.

This method is equivalent to:

```java
JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);
```

**Parameters:**
- serviceURL

- the address of the connector server to connect to.
- environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.

**Returns:**
- a

JMXConnector

representing the newly-made
connection. Each successful call to this method produces a
different object.

**Throws:**
- NullPointerException

- if

serviceURL

is null.
- IOException

- if the connector client or the
connection cannot be made because of a communication problem.
- SecurityException

- if the connection cannot be made
for security reasons.

---

#### public static
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException

Creates a connector client for the connector server at the
given address. The resultant client is not connected until its

connect

method is called.

**Parameters:**
- serviceURL

- the address of the connector server to connect to.
- environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.

**Returns:**
- a

JMXConnector

representing the new
connector client. Each successful call to this method produces
a different object.

**Throws:**
- NullPointerException

- if

serviceURL

is null.
- IOException

- if the connector client cannot be made
because of a communication problem.
- MalformedURLException

- if there is no provider for the
protocol in

serviceURL

.
- JMXProviderException

- if there is a provider for the
protocol in

serviceURL

but it cannot be used for
some reason.

---

### Additional Sections

#### Class JMXConnectorFactory

java.lang.Object

- javax.management.remote.JMXConnectorFactory

javax.management.remote.JMXConnectorFactory

```java
public class
JMXConnectorFactory

extends
Object
```

Factory to create JMX API connector clients. There
are no instances of this class.

Connections are usually made using the

connect

method of this class. More
advanced applications can separate the creation of the connector
client, using

newJMXConnector

and the establishment of the connection itself, using

JMXConnector.connect(Map)

.

Each client is created by an instance of

JMXConnectorProvider

. This instance is found as follows. Suppose
the given

JMXServiceURL

looks like

"service:jmx:

protocol

:

remainder

"

.
Then the factory will attempt to find the appropriate

JMXConnectorProvider

for

protocol

. Each
occurrence of the character

+

or

-

in

protocol

is replaced by

.

or

_

, respectively.

A

provider package list

is searched for as follows:

- If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.pkgs

then the
associated value is the provider package list.

Otherwise, if the system property

jmx.remote.protocol.provider.pkgs

exists, then its value
is the provider package list.

Otherwise, there is no provider package list.

The provider package list is a string that is interpreted as a
list of non-empty Java package names separated by vertical bars
(

|

). If the string is empty, then so is the provider
package list. If the provider package list is not a String, or if
it contains an element that is an empty string, a

JMXProviderException

is thrown.

If the provider package list exists and is not empty, then for
each element

pkg

of the list, the factory
will attempt to load the class

pkg

.

protocol

.ClientProvider

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.class.loader

then the
associated value is the class loader to use to load the provider.
If the associated value is not an instance of

ClassLoader

, an

IllegalArgumentException

is thrown.

If the

jmx.remote.protocol.provider.class.loader

key is not present in the

environment

parameter, the
calling thread's context class loader is used.

If the attempt to load this class produces a

ClassNotFoundException

, the search for a handler continues with
the next element of the list.

Otherwise, a problem with the provider found is signalled by a

JMXProviderException

whose

cause

indicates the underlying
exception, as follows:

- if the attempt to load the class produces an exception other
than

ClassNotFoundException

, that is the

cause

;

if

Class.newInstance()

for the class produces an
exception, that is the

cause

.

If no provider is found by the above steps, including the
default case where there is no provider package list, then the
implementation will use its own provider for

protocol

, or it will throw a

MalformedURLException

if there is none. An
implementation may choose to find providers by other means. For
example, it may support

service providers

,
where the service interface is

JMXConnectorProvider

.

Every implementation must support the RMI connector protocol with
the default RMI transport, specified with string

rmi

.

Once a provider is found, the result of the

newJMXConnector

method is the result of calling

newJMXConnector

on the provider.

The

Map

parameter passed to the

JMXConnectorProvider

is a new read-only

Map

that contains all the entries that were in the

environment

parameter to

JMXConnectorFactory.newJMXConnector

, if there was one.
Additionally, if the

jmx.remote.protocol.provider.class.loader

key is not
present in the

environment

parameter, it is added to
the new read-only

Map

. The associated value is the
calling thread's context class loader.

**Since:** 1.5

public class

JMXConnectorFactory

extends

Object

Factory to create JMX API connector clients. There
are no instances of this class.

Connections are usually made using the

connect

method of this class. More
advanced applications can separate the creation of the connector
client, using

newJMXConnector

and the establishment of the connection itself, using

JMXConnector.connect(Map)

.

Each client is created by an instance of

JMXConnectorProvider

. This instance is found as follows. Suppose
the given

JMXServiceURL

looks like

"service:jmx:

protocol

:

remainder

"

.
Then the factory will attempt to find the appropriate

JMXConnectorProvider

for

protocol

. Each
occurrence of the character

+

or

-

in

protocol

is replaced by

.

or

_

, respectively.

A

provider package list

is searched for as follows:

- If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.pkgs

then the
associated value is the provider package list.

Otherwise, if the system property

jmx.remote.protocol.provider.pkgs

exists, then its value
is the provider package list.

Otherwise, there is no provider package list.

The provider package list is a string that is interpreted as a
list of non-empty Java package names separated by vertical bars
(

|

). If the string is empty, then so is the provider
package list. If the provider package list is not a String, or if
it contains an element that is an empty string, a

JMXProviderException

is thrown.

If the provider package list exists and is not empty, then for
each element

pkg

of the list, the factory
will attempt to load the class

pkg

.

protocol

.ClientProvider

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.class.loader

then the
associated value is the class loader to use to load the provider.
If the associated value is not an instance of

ClassLoader

, an

IllegalArgumentException

is thrown.

If the

jmx.remote.protocol.provider.class.loader

key is not present in the

environment

parameter, the
calling thread's context class loader is used.

If the attempt to load this class produces a

ClassNotFoundException

, the search for a handler continues with
the next element of the list.

Otherwise, a problem with the provider found is signalled by a

JMXProviderException

whose

cause

indicates the underlying
exception, as follows:

- if the attempt to load the class produces an exception other
than

ClassNotFoundException

, that is the

cause

;

if

Class.newInstance()

for the class produces an
exception, that is the

cause

.

If no provider is found by the above steps, including the
default case where there is no provider package list, then the
implementation will use its own provider for

protocol

, or it will throw a

MalformedURLException

if there is none. An
implementation may choose to find providers by other means. For
example, it may support

service providers

,
where the service interface is

JMXConnectorProvider

.

Every implementation must support the RMI connector protocol with
the default RMI transport, specified with string

rmi

.

Once a provider is found, the result of the

newJMXConnector

method is the result of calling

newJMXConnector

on the provider.

The

Map

parameter passed to the

JMXConnectorProvider

is a new read-only

Map

that contains all the entries that were in the

environment

parameter to

JMXConnectorFactory.newJMXConnector

, if there was one.
Additionally, if the

jmx.remote.protocol.provider.class.loader

key is not
present in the

environment

parameter, it is added to
the new read-only

Map

. The associated value is the
calling thread's context class loader.

Factory to create JMX API connector clients. There
are no instances of this class.

Connections are usually made using the

connect

method of this class. More
advanced applications can separate the creation of the connector
client, using

newJMXConnector

and the establishment of the connection itself, using

JMXConnector.connect(Map)

.

Each client is created by an instance of

JMXConnectorProvider

. This instance is found as follows. Suppose
the given

JMXServiceURL

looks like

"service:jmx:

protocol

:

remainder

"

.
Then the factory will attempt to find the appropriate

JMXConnectorProvider

for

protocol

. Each
occurrence of the character

+

or

-

in

protocol

is replaced by

.

or

_

, respectively.

A

provider package list

is searched for as follows:

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.pkgs

then the
associated value is the provider package list.

Otherwise, if the system property

jmx.remote.protocol.provider.pkgs

exists, then its value
is the provider package list.

Otherwise, there is no provider package list.

The provider package list is a string that is interpreted as a
list of non-empty Java package names separated by vertical bars
(

|

). If the string is empty, then so is the provider
package list. If the provider package list is not a String, or if
it contains an element that is an empty string, a

JMXProviderException

is thrown.

If the provider package list exists and is not empty, then for
each element

pkg

of the list, the factory
will attempt to load the class

pkg

.

protocol

.ClientProvider

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.class.loader

then the
associated value is the class loader to use to load the provider.
If the associated value is not an instance of

ClassLoader

, an

IllegalArgumentException

is thrown.

If the

jmx.remote.protocol.provider.class.loader

key is not present in the

environment

parameter, the
calling thread's context class loader is used.

If the attempt to load this class produces a

ClassNotFoundException

, the search for a handler continues with
the next element of the list.

Otherwise, a problem with the provider found is signalled by a

JMXProviderException

whose

cause

indicates the underlying
exception, as follows:

- if the attempt to load the class produces an exception other
than

ClassNotFoundException

, that is the

cause

;

if

Class.newInstance()

for the class produces an
exception, that is the

cause

.

If no provider is found by the above steps, including the
default case where there is no provider package list, then the
implementation will use its own provider for

protocol

, or it will throw a

MalformedURLException

if there is none. An
implementation may choose to find providers by other means. For
example, it may support

service providers

,
where the service interface is

JMXConnectorProvider

.

Every implementation must support the RMI connector protocol with
the default RMI transport, specified with string

rmi

.

Once a provider is found, the result of the

newJMXConnector

method is the result of calling

newJMXConnector

on the provider.

The

Map

parameter passed to the

JMXConnectorProvider

is a new read-only

Map

that contains all the entries that were in the

environment

parameter to

JMXConnectorFactory.newJMXConnector

, if there was one.
Additionally, if the

jmx.remote.protocol.provider.class.loader

key is not
present in the

environment

parameter, it is added to
the new read-only

Map

. The associated value is the
calling thread's context class loader.

If the

environment

parameter to

newJMXConnector

contains the
key

jmx.remote.protocol.provider.class.loader

then the
associated value is the class loader to use to load the provider.
If the associated value is not an instance of

ClassLoader

, an

IllegalArgumentException

is thrown.

If the

jmx.remote.protocol.provider.class.loader

key is not present in the

environment

parameter, the
calling thread's context class loader is used.

If the attempt to load this class produces a

ClassNotFoundException

, the search for a handler continues with
the next element of the list.

Otherwise, a problem with the provider found is signalled by a

JMXProviderException

whose

cause

indicates the underlying
exception, as follows:

if the attempt to load the class produces an exception other
than

ClassNotFoundException

, that is the

cause

;

if

Class.newInstance()

for the class produces an
exception, that is the

cause

.

If no provider is found by the above steps, including the
default case where there is no provider package list, then the
implementation will use its own provider for

protocol

, or it will throw a

MalformedURLException

if there is none. An
implementation may choose to find providers by other means. For
example, it may support

service providers

,
where the service interface is

JMXConnectorProvider

.

Every implementation must support the RMI connector protocol with
the default RMI transport, specified with string

rmi

.

Once a provider is found, the result of the

newJMXConnector

method is the result of calling

newJMXConnector

on the provider.

The

Map

parameter passed to the

JMXConnectorProvider

is a new read-only

Map

that contains all the entries that were in the

environment

parameter to

JMXConnectorFactory.newJMXConnector

, if there was one.
Additionally, if the

jmx.remote.protocol.provider.class.loader

key is not
present in the

environment

parameter, it is added to
the new read-only

Map

. The associated value is the
calling thread's context class loader.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_CLASS_LOADER

Name of the attribute that specifies the default class
loader.

static

String

PROTOCOL_PROVIDER_CLASS_LOADER

Name of the attribute that specifies the class
loader for loading protocol providers.

static

String

PROTOCOL_PROVIDER_PACKAGES

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JMXConnector

connect

​(

JMXServiceURL

serviceURL)

Creates a connection to the connector server at the given
address.

static

JMXConnector

connect

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a connection to the connector server at the given
address.

static

JMXConnector

newJMXConnector

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a connector client for the connector server at the
given address.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_CLASS_LOADER

Name of the attribute that specifies the default class
loader.

static

String

PROTOCOL_PROVIDER_CLASS_LOADER

Name of the attribute that specifies the class
loader for loading protocol providers.

static

String

PROTOCOL_PROVIDER_PACKAGES

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.

---

#### Field Summary

Name of the attribute that specifies the default class
loader.

Name of the attribute that specifies the class
loader for loading protocol providers.

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

JMXConnector

connect

​(

JMXServiceURL

serviceURL)

Creates a connection to the connector server at the given
address.

static

JMXConnector

connect

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a connection to the connector server at the given
address.

static

JMXConnector

newJMXConnector

​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)

Creates a connector client for the connector server at the
given address.

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

Creates a connection to the connector server at the given
address.

Creates a connector client for the connector server at the
given address.

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

- DEFAULT_CLASS_LOADER

```java
public static final
String
DEFAULT_CLASS_LOADER
```

Name of the attribute that specifies the default class
loader. This class loader is used to deserialize return values and
exceptions from remote

MBeanServerConnection

calls. The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

- PROTOCOL_PROVIDER_PACKAGES

```java
public static final
String
PROTOCOL_PROVIDER_PACKAGES
```

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.
The value associated with this attribute is a string with
package names separated by vertical bars (

|

).

**See Also:** Constant Field Values

- PROTOCOL_PROVIDER_CLASS_LOADER

```java
public static final
String
PROTOCOL_PROVIDER_CLASS_LOADER
```

Name of the attribute that specifies the class
loader for loading protocol providers.
The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

**Parameters:** serviceURL

- the address of the connector server to
connect to.
**Returns:** a

JMXConnector

whose

connect

method has been called.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

- connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to:

```java
JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);
```

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the newly-made
connection. Each successful call to this method produces a
different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

- newJMXConnector

```java
public static
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connector client for the connector server at the
given address. The resultant client is not connected until its

connect

method is called.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client cannot be made
because of a communication problem.
**Throws:** MalformedURLException

- if there is no provider for the
protocol in

serviceURL

.
**Throws:** JMXProviderException

- if there is a provider for the
protocol in

serviceURL

but it cannot be used for
some reason.

Field Detail

- DEFAULT_CLASS_LOADER

```java
public static final
String
DEFAULT_CLASS_LOADER
```

Name of the attribute that specifies the default class
loader. This class loader is used to deserialize return values and
exceptions from remote

MBeanServerConnection

calls. The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

- PROTOCOL_PROVIDER_PACKAGES

```java
public static final
String
PROTOCOL_PROVIDER_PACKAGES
```

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.
The value associated with this attribute is a string with
package names separated by vertical bars (

|

).

**See Also:** Constant Field Values

- PROTOCOL_PROVIDER_CLASS_LOADER

```java
public static final
String
PROTOCOL_PROVIDER_CLASS_LOADER
```

Name of the attribute that specifies the class
loader for loading protocol providers.
The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_CLASS_LOADER

```java
public static final
String
DEFAULT_CLASS_LOADER
```

Name of the attribute that specifies the default class
loader. This class loader is used to deserialize return values and
exceptions from remote

MBeanServerConnection

calls. The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

---

#### DEFAULT_CLASS_LOADER

public static final

String

DEFAULT_CLASS_LOADER

Name of the attribute that specifies the default class
loader. This class loader is used to deserialize return values and
exceptions from remote

MBeanServerConnection

calls. The value associated with this attribute is an instance
of

ClassLoader

.

PROTOCOL_PROVIDER_PACKAGES

```java
public static final
String
PROTOCOL_PROVIDER_PACKAGES
```

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.
The value associated with this attribute is a string with
package names separated by vertical bars (

|

).

**See Also:** Constant Field Values

---

#### PROTOCOL_PROVIDER_PACKAGES

public static final

String

PROTOCOL_PROVIDER_PACKAGES

Name of the attribute that specifies the provider packages
that are consulted when looking for the handler for a protocol.
The value associated with this attribute is a string with
package names separated by vertical bars (

|

).

PROTOCOL_PROVIDER_CLASS_LOADER

```java
public static final
String
PROTOCOL_PROVIDER_CLASS_LOADER
```

Name of the attribute that specifies the class
loader for loading protocol providers.
The value associated with this attribute is an instance
of

ClassLoader

.

**See Also:** Constant Field Values

---

#### PROTOCOL_PROVIDER_CLASS_LOADER

public static final

String

PROTOCOL_PROVIDER_CLASS_LOADER

Name of the attribute that specifies the class
loader for loading protocol providers.
The value associated with this attribute is an instance
of

ClassLoader

.

Method Detail

- connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

**Parameters:** serviceURL

- the address of the connector server to
connect to.
**Returns:** a

JMXConnector

whose

connect

method has been called.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

- connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to:

```java
JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);
```

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the newly-made
connection. Each successful call to this method produces a
different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

- newJMXConnector

```java
public static
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connector client for the connector server at the
given address. The resultant client is not connected until its

connect

method is called.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client cannot be made
because of a communication problem.
**Throws:** MalformedURLException

- if there is no provider for the
protocol in

serviceURL

.
**Throws:** JMXProviderException

- if there is a provider for the
protocol in

serviceURL

but it cannot be used for
some reason.

---

#### Method Detail

connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

**Parameters:** serviceURL

- the address of the connector server to
connect to.
**Returns:** a

JMXConnector

whose

connect

method has been called.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

---

#### connect

public static

JMXConnector

connect​(

JMXServiceURL

serviceURL)
throws

IOException

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

Creates a connection to the connector server at the given
address.

This method is equivalent to

connect(serviceURL, null)

.

connect

```java
public static
JMXConnector
connect​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connection to the connector server at the given
address.

This method is equivalent to:

```java
JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);
```

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the newly-made
connection. Each successful call to this method produces a
different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client or the
connection cannot be made because of a communication problem.
**Throws:** SecurityException

- if the connection cannot be made
for security reasons.

---

#### connect

public static

JMXConnector

connect​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)
throws

IOException

Creates a connection to the connector server at the given
address.

This method is equivalent to:

```java
JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);
```

Creates a connection to the connector server at the given
address.

This method is equivalent to:

JMXConnector conn = JMXConnectorFactory.newJMXConnector(serviceURL,
environment);
conn.connect(environment);

newJMXConnector

```java
public static
JMXConnector
newJMXConnector​(
JMXServiceURL
serviceURL,

Map
<
String
,​?> environment)
throws
IOException
```

Creates a connector client for the connector server at the
given address. The resultant client is not connected until its

connect

method is called.

**Parameters:** serviceURL

- the address of the connector server to connect to.
**Parameters:** environment

- a set of attributes to determine how the
connection is made. This parameter can be null. Keys in this
map must be Strings. The appropriate type of each associated
value depends on the attribute. The contents of

environment

are not changed by this call.
**Returns:** a

JMXConnector

representing the new
connector client. Each successful call to this method produces
a different object.
**Throws:** NullPointerException

- if

serviceURL

is null.
**Throws:** IOException

- if the connector client cannot be made
because of a communication problem.
**Throws:** MalformedURLException

- if there is no provider for the
protocol in

serviceURL

.
**Throws:** JMXProviderException

- if there is a provider for the
protocol in

serviceURL

but it cannot be used for
some reason.

---

#### newJMXConnector

public static

JMXConnector

newJMXConnector​(

JMXServiceURL

serviceURL,

Map

<

String

,​?> environment)
throws

IOException

Creates a connector client for the connector server at the
given address. The resultant client is not connected until its

connect

method is called.

---

