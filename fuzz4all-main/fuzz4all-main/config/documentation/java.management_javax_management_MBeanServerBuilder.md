# Class MBeanServerBuilder

**Source:** `java.management\javax\management\MBeanServerBuilder.html`

### Class Description

```java
public class
MBeanServerBuilder

extends
Object
```

This class represents a builder that creates a default

MBeanServer

implementation.
The JMX

MBeanServerFactory

allows
applications to provide their custom MBeanServer
implementation by providing a subclass of this class.

**Since:** 1.5
**See Also:** MBeanServer

,

MBeanServerFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanServerBuilder()

Public default constructor.

---

### Method Details

#### public
MBeanServerDelegate
newMBeanServerDelegate()

This method creates a new MBeanServerDelegate for a new MBeanServer.
When creating a new MBeanServer the

MBeanServerFactory

first calls this method
in order to create a new MBeanServerDelegate.

Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

**Returns:**
- A new

MBeanServerDelegate

.

---

#### public
MBeanServer
newMBeanServer​(
String
defaultDomain,

MBeanServer
outer,

MBeanServerDelegate
delegate)

This method creates a new MBeanServer implementation object.
When creating a new MBeanServer the

MBeanServerFactory

first calls

newMBeanServerDelegate()

in order to obtain a new

MBeanServerDelegate

for the new
MBeanServer. Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

**Parameters:**
- defaultDomain

- Default domain of the new MBeanServer.
- outer

- A pointer to the MBeanServer object that must be
passed to the MBeans when invoking their

MBeanRegistration

interface.
- delegate

- A pointer to the MBeanServerDelegate associated
with the new MBeanServer. The new MBeanServer must register
this MBean in its MBean repository.

**Returns:**
- A new private implementation of an MBeanServer.

---

### Additional Sections

#### Class MBeanServerBuilder

java.lang.Object

- javax.management.MBeanServerBuilder

javax.management.MBeanServerBuilder

```java
public class
MBeanServerBuilder

extends
Object
```

This class represents a builder that creates a default

MBeanServer

implementation.
The JMX

MBeanServerFactory

allows
applications to provide their custom MBeanServer
implementation by providing a subclass of this class.

**Since:** 1.5
**See Also:** MBeanServer

,

MBeanServerFactory

public class

MBeanServerBuilder

extends

Object

This class represents a builder that creates a default

MBeanServer

implementation.
The JMX

MBeanServerFactory

allows
applications to provide their custom MBeanServer
implementation by providing a subclass of this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerBuilder

()

Public default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MBeanServer

newMBeanServer

​(

String

defaultDomain,

MBeanServer

outer,

MBeanServerDelegate

delegate)

This method creates a new MBeanServer implementation object.

MBeanServerDelegate

newMBeanServerDelegate

()

This method creates a new MBeanServerDelegate for a new MBeanServer.

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

MBeanServerBuilder

()

Public default constructor.

---

#### Constructor Summary

Public default constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MBeanServer

newMBeanServer

​(

String

defaultDomain,

MBeanServer

outer,

MBeanServerDelegate

delegate)

This method creates a new MBeanServer implementation object.

MBeanServerDelegate

newMBeanServerDelegate

()

This method creates a new MBeanServerDelegate for a new MBeanServer.

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

This method creates a new MBeanServer implementation object.

This method creates a new MBeanServerDelegate for a new MBeanServer.

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

- MBeanServerBuilder

```java
public MBeanServerBuilder()
```

Public default constructor.

============ METHOD DETAIL ==========

- Method Detail

- newMBeanServerDelegate

```java
public
MBeanServerDelegate
newMBeanServerDelegate()
```

This method creates a new MBeanServerDelegate for a new MBeanServer.
When creating a new MBeanServer the

MBeanServerFactory

first calls this method
in order to create a new MBeanServerDelegate.

Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

**Returns:** A new

MBeanServerDelegate

.

- newMBeanServer

```java
public
MBeanServer
newMBeanServer​(
String
defaultDomain,

MBeanServer
outer,

MBeanServerDelegate
delegate)
```

This method creates a new MBeanServer implementation object.
When creating a new MBeanServer the

MBeanServerFactory

first calls

newMBeanServerDelegate()

in order to obtain a new

MBeanServerDelegate

for the new
MBeanServer. Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

**Parameters:** defaultDomain

- Default domain of the new MBeanServer.
**Parameters:** outer

- A pointer to the MBeanServer object that must be
passed to the MBeans when invoking their

MBeanRegistration

interface.
**Parameters:** delegate

- A pointer to the MBeanServerDelegate associated
with the new MBeanServer. The new MBeanServer must register
this MBean in its MBean repository.
**Returns:** A new private implementation of an MBeanServer.

Constructor Detail

- MBeanServerBuilder

```java
public MBeanServerBuilder()
```

Public default constructor.

---

#### Constructor Detail

MBeanServerBuilder

```java
public MBeanServerBuilder()
```

Public default constructor.

---

#### MBeanServerBuilder

public MBeanServerBuilder()

Public default constructor.

Method Detail

- newMBeanServerDelegate

```java
public
MBeanServerDelegate
newMBeanServerDelegate()
```

This method creates a new MBeanServerDelegate for a new MBeanServer.
When creating a new MBeanServer the

MBeanServerFactory

first calls this method
in order to create a new MBeanServerDelegate.

Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

**Returns:** A new

MBeanServerDelegate

.

- newMBeanServer

```java
public
MBeanServer
newMBeanServer​(
String
defaultDomain,

MBeanServer
outer,

MBeanServerDelegate
delegate)
```

This method creates a new MBeanServer implementation object.
When creating a new MBeanServer the

MBeanServerFactory

first calls

newMBeanServerDelegate()

in order to obtain a new

MBeanServerDelegate

for the new
MBeanServer. Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

**Parameters:** defaultDomain

- Default domain of the new MBeanServer.
**Parameters:** outer

- A pointer to the MBeanServer object that must be
passed to the MBeans when invoking their

MBeanRegistration

interface.
**Parameters:** delegate

- A pointer to the MBeanServerDelegate associated
with the new MBeanServer. The new MBeanServer must register
this MBean in its MBean repository.
**Returns:** A new private implementation of an MBeanServer.

---

#### Method Detail

newMBeanServerDelegate

```java
public
MBeanServerDelegate
newMBeanServerDelegate()
```

This method creates a new MBeanServerDelegate for a new MBeanServer.
When creating a new MBeanServer the

MBeanServerFactory

first calls this method
in order to create a new MBeanServerDelegate.

Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

**Returns:** A new

MBeanServerDelegate

.

---

#### newMBeanServerDelegate

public

MBeanServerDelegate

newMBeanServerDelegate()

This method creates a new MBeanServerDelegate for a new MBeanServer.
When creating a new MBeanServer the

MBeanServerFactory

first calls this method
in order to create a new MBeanServerDelegate.

Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this method. It could
be, for instance, a new object wrapping the previously
returned object.

newMBeanServer

```java
public
MBeanServer
newMBeanServer​(
String
defaultDomain,

MBeanServer
outer,

MBeanServerDelegate
delegate)
```

This method creates a new MBeanServer implementation object.
When creating a new MBeanServer the

MBeanServerFactory

first calls

newMBeanServerDelegate()

in order to obtain a new

MBeanServerDelegate

for the new
MBeanServer. Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

**Parameters:** defaultDomain

- Default domain of the new MBeanServer.
**Parameters:** outer

- A pointer to the MBeanServer object that must be
passed to the MBeans when invoking their

MBeanRegistration

interface.
**Parameters:** delegate

- A pointer to the MBeanServerDelegate associated
with the new MBeanServer. The new MBeanServer must register
this MBean in its MBean repository.
**Returns:** A new private implementation of an MBeanServer.

---

#### newMBeanServer

public

MBeanServer

newMBeanServer​(

String

defaultDomain,

MBeanServer

outer,

MBeanServerDelegate

delegate)

This method creates a new MBeanServer implementation object.
When creating a new MBeanServer the

MBeanServerFactory

first calls

newMBeanServerDelegate()

in order to obtain a new

MBeanServerDelegate

for the new
MBeanServer. Then it calls

newMBeanServer(defaultDomain,outer,delegate)

passing the

delegate

that should be used by the MBeanServer
implementation.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

Note that the passed

delegate

might not be directly the
MBeanServerDelegate that was returned by this implementation. It could
be, for instance, a new object wrapping the previously
returned delegate.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

The

outer

parameter is a pointer to the MBeanServer that
should be passed to the

MBeanRegistration

interface when registering MBeans inside the MBeanServer.
If

outer

is

null

, then the MBeanServer
implementation must use its own

this

reference when
invoking the

MBeanRegistration

interface.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

This makes it possible for a MBeanServer implementation to wrap
another MBeanServer implementation, in order to implement, e.g,
security checks, or to prevent access to the actual MBeanServer
implementation by returning a pointer to a wrapping object.

---

