# Class BeanContextServiceRevokedEvent

**Source:** `java.desktop\java\beans\beancontext\BeanContextServiceRevokedEvent.html`

### Class Description

```java
public class
BeanContextServiceRevokedEvent

extends
BeanContextEvent
```

This event type is used by the

BeanContextServiceRevokedListener

in order to
identify the service being revoked.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Class
<?> serviceClass

A

Class

reference to the service that is being revoked.

---

### Constructor Details

#### public BeanContextServiceRevokedEvent​(
BeanContextServices
bcs,

Class
<?> sc,
boolean invalidate)

Construct a

BeanContextServiceEvent

.

**Parameters:**
- bcs

- the

BeanContextServices

from which this service is being revoked
- sc

- the service that is being revoked
- invalidate

-

true

for immediate revocation

---

### Method Details

#### public
BeanContextServices
getSourceAsBeanContextServices()

Gets the source as a reference of type

BeanContextServices

**Returns:**
- the

BeanContextServices

from which
this service is being revoked

---

#### public
Class
<?> getServiceClass()

Gets the service class that is the subject of this notification

**Returns:**
- A

Class

reference to the
service that is being revoked

---

#### public boolean isServiceClass​(
Class
<?> service)

Checks this event to determine whether or not
the service being revoked is of a particular class.

**Parameters:**
- service

- the service of interest (should be non-null)

**Returns:**
- true

if the service being revoked is of the
same class as the specified service

---

#### public boolean isCurrentServiceInvalidNow()

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

**Returns:**
- true

if current service is being forcibly revoked

---

### Additional Sections

#### Class BeanContextServiceRevokedEvent

java.lang.Object

- java.util.EventObject
- - java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextServiceRevokedEvent

java.util.EventObject

- java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextServiceRevokedEvent

java.beans.beancontext.BeanContextEvent

- java.beans.beancontext.BeanContextServiceRevokedEvent

java.beans.beancontext.BeanContextServiceRevokedEvent

**All Implemented Interfaces:** Serializable

```java
public class
BeanContextServiceRevokedEvent

extends
BeanContextEvent
```

This event type is used by the

BeanContextServiceRevokedListener

in order to
identify the service being revoked.

**See Also:** Serialized Form

public class

BeanContextServiceRevokedEvent

extends

BeanContextEvent

This event type is used by the

BeanContextServiceRevokedListener

in order to
identify the service being revoked.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Class

<?>

serviceClass

A

Class

reference to the service that is being revoked.

- Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BeanContextServiceRevokedEvent

​(

BeanContextServices

bcs,

Class

<?> sc,
boolean invalidate)

Construct a

BeanContextServiceEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getServiceClass

()

Gets the service class that is the subject of this notification

BeanContextServices

getSourceAsBeanContextServices

()

Gets the source as a reference of type

BeanContextServices

boolean

isCurrentServiceInvalidNow

()

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

boolean

isServiceClass

​(

Class

<?> service)

Checks this event to determine whether or not
the service being revoked is of a particular class.

- Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

protected

Class

<?>

serviceClass

A

Class

reference to the service that is being revoked.

- Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

A

Class

reference to the service that is being revoked.

Fields declared in class java.beans.beancontext.

BeanContextEvent

propagatedFrom

---

#### Fields declared in class java.beans.beancontext. BeanContextEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

BeanContextServiceRevokedEvent

​(

BeanContextServices

bcs,

Class

<?> sc,
boolean invalidate)

Construct a

BeanContextServiceEvent

.

---

#### Constructor Summary

Construct a

BeanContextServiceEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getServiceClass

()

Gets the service class that is the subject of this notification

BeanContextServices

getSourceAsBeanContextServices

()

Gets the source as a reference of type

BeanContextServices

boolean

isCurrentServiceInvalidNow

()

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

boolean

isServiceClass

​(

Class

<?> service)

Checks this event to determine whether or not
the service being revoked is of a particular class.

- Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Gets the service class that is the subject of this notification

Gets the source as a reference of type

BeanContextServices

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

Checks this event to determine whether or not
the service being revoked is of a particular class.

Methods declared in class java.beans.beancontext.

BeanContextEvent

getBeanContext

,

getPropagatedFrom

,

isPropagated

,

setPropagatedFrom

---

#### Methods declared in class java.beans.beancontext. BeanContextEvent

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- serviceClass

```java
protected
Class
<?> serviceClass
```

A

Class

reference to the service that is being revoked.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextServiceRevokedEvent

```java
public BeanContextServiceRevokedEvent​(
BeanContextServices
bcs,

Class
<?> sc,
boolean invalidate)
```

Construct a

BeanContextServiceEvent

.

**Parameters:** bcs

- the

BeanContextServices

from which this service is being revoked
**Parameters:** sc

- the service that is being revoked
**Parameters:** invalidate

-

true

for immediate revocation

============ METHOD DETAIL ==========

- Method Detail

- getSourceAsBeanContextServices

```java
public
BeanContextServices
getSourceAsBeanContextServices()
```

Gets the source as a reference of type

BeanContextServices

**Returns:** the

BeanContextServices

from which
this service is being revoked

- getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification

**Returns:** A

Class

reference to the
service that is being revoked

- isServiceClass

```java
public boolean isServiceClass​(
Class
<?> service)
```

Checks this event to determine whether or not
the service being revoked is of a particular class.

**Parameters:** service

- the service of interest (should be non-null)
**Returns:** true

if the service being revoked is of the
same class as the specified service

- isCurrentServiceInvalidNow

```java
public boolean isCurrentServiceInvalidNow()
```

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

**Returns:** true

if current service is being forcibly revoked

Field Detail

- serviceClass

```java
protected
Class
<?> serviceClass
```

A

Class

reference to the service that is being revoked.

---

#### Field Detail

serviceClass

```java
protected
Class
<?> serviceClass
```

A

Class

reference to the service that is being revoked.

---

#### serviceClass

protected

Class

<?> serviceClass

A

Class

reference to the service that is being revoked.

Constructor Detail

- BeanContextServiceRevokedEvent

```java
public BeanContextServiceRevokedEvent​(
BeanContextServices
bcs,

Class
<?> sc,
boolean invalidate)
```

Construct a

BeanContextServiceEvent

.

**Parameters:** bcs

- the

BeanContextServices

from which this service is being revoked
**Parameters:** sc

- the service that is being revoked
**Parameters:** invalidate

-

true

for immediate revocation

---

#### Constructor Detail

BeanContextServiceRevokedEvent

```java
public BeanContextServiceRevokedEvent​(
BeanContextServices
bcs,

Class
<?> sc,
boolean invalidate)
```

Construct a

BeanContextServiceEvent

.

**Parameters:** bcs

- the

BeanContextServices

from which this service is being revoked
**Parameters:** sc

- the service that is being revoked
**Parameters:** invalidate

-

true

for immediate revocation

---

#### BeanContextServiceRevokedEvent

public BeanContextServiceRevokedEvent​(

BeanContextServices

bcs,

Class

<?> sc,
boolean invalidate)

Construct a

BeanContextServiceEvent

.

Method Detail

- getSourceAsBeanContextServices

```java
public
BeanContextServices
getSourceAsBeanContextServices()
```

Gets the source as a reference of type

BeanContextServices

**Returns:** the

BeanContextServices

from which
this service is being revoked

- getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification

**Returns:** A

Class

reference to the
service that is being revoked

- isServiceClass

```java
public boolean isServiceClass​(
Class
<?> service)
```

Checks this event to determine whether or not
the service being revoked is of a particular class.

**Parameters:** service

- the service of interest (should be non-null)
**Returns:** true

if the service being revoked is of the
same class as the specified service

- isCurrentServiceInvalidNow

```java
public boolean isCurrentServiceInvalidNow()
```

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

**Returns:** true

if current service is being forcibly revoked

---

#### Method Detail

getSourceAsBeanContextServices

```java
public
BeanContextServices
getSourceAsBeanContextServices()
```

Gets the source as a reference of type

BeanContextServices

**Returns:** the

BeanContextServices

from which
this service is being revoked

---

#### getSourceAsBeanContextServices

public

BeanContextServices

getSourceAsBeanContextServices()

Gets the source as a reference of type

BeanContextServices

getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification

**Returns:** A

Class

reference to the
service that is being revoked

---

#### getServiceClass

public

Class

<?> getServiceClass()

Gets the service class that is the subject of this notification

isServiceClass

```java
public boolean isServiceClass​(
Class
<?> service)
```

Checks this event to determine whether or not
the service being revoked is of a particular class.

**Parameters:** service

- the service of interest (should be non-null)
**Returns:** true

if the service being revoked is of the
same class as the specified service

---

#### isServiceClass

public boolean isServiceClass​(

Class

<?> service)

Checks this event to determine whether or not
the service being revoked is of a particular class.

isCurrentServiceInvalidNow

```java
public boolean isCurrentServiceInvalidNow()
```

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

**Returns:** true

if current service is being forcibly revoked

---

#### isCurrentServiceInvalidNow

public boolean isCurrentServiceInvalidNow()

Reports if the current service is being forcibly revoked,
in which case the references are now invalidated and unusable.

---

