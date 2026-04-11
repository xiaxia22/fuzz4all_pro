# Interface BeanContextServices

**Source:** `java.desktop\java\beans\beancontext\BeanContextServices.html`

### Class Description

```java
public interface
BeanContextServices

extends
BeanContext
,
BeanContextServicesListener
```

The BeanContextServices interface provides a mechanism for a BeanContext
to expose generic "services" to the BeanContextChild objects within.

**All Superinterfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

,

BeanContextServicesListener

,

Collection

,

DesignMode

,

EventListener

,

Iterable

,

Visibility

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider)

Adds a service to this BeanContext.

BeanContextServiceProvider

s call this method
to register a particular service with this context.
If the service has not previously been added, the

BeanContextServices

associates
the service with the

BeanContextServiceProvider

and
fires a

BeanContextServiceAvailableEvent

to all
currently registered

BeanContextServicesListeners

.
The method then returns

true

, indicating that
the addition of the service was successful.
If the given service has already been added, this method
simply returns

false

.

**Parameters:**
- serviceClass

- the service to add
- serviceProvider

- the

BeanContextServiceProvider

associated with the service

**Returns:**
- true if the service was successful added, false otherwise

---

#### void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider,
boolean revokeCurrentServicesNow)

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method. Upon revocation of
the service, the

BeanContextServices

fires a

BeanContextServiceRevokedEvent

to its
list of currently registered

BeanContextServiceRevokedListeners

and

BeanContextServicesListeners

.

**Parameters:**
- serviceClass

- the service to revoke from this BeanContextServices
- serviceProvider

- the BeanContextServiceProvider associated with
this particular service that is being revoked
- revokeCurrentServicesNow

- a value of

true

indicates an exceptional circumstance where the

BeanContextServiceProvider

or

BeanContextServices

wishes to immediately
terminate service to all currently outstanding references
to the specified service.

---

#### boolean hasService​(
Class
<?> serviceClass)

Reports whether or not a given service is
currently available from this context.

**Parameters:**
- serviceClass

- the service in question

**Returns:**
- true if the service is available

---

#### Object
getService​(
BeanContextChild
child,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector,

BeanContextServiceRevokedListener
bcsrl)
throws
TooManyListenersException

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method. When invoked, this method
gets the service by calling the getService() method on the
underlying

BeanContextServiceProvider

.

**Parameters:**
- child

- the

BeanContextChild

associated with this request
- requestor

- the object requesting the service
- serviceClass

- class of the requested service
- serviceSelector

- the service dependent parameter
- bcsrl

- the

BeanContextServiceRevokedListener

to notify
if the service should later become revoked

**Returns:**
- a reference to this context's named
Service as requested or

null

**Throws:**
- TooManyListenersException

- if there are too many listeners

---

#### void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

**Parameters:**
- child

- the

BeanContextChild
- requestor

- the requestor
- service

- the service

---

#### Iterator
<?> getCurrentServiceClasses()

Gets the currently available services for this context.

**Returns:**
- an

Iterator

consisting of the
currently available services

---

#### Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Parameters:**
- serviceClass

- the specified service

**Returns:**
- the currently available service selectors
for the named serviceClass

---

#### void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)

Adds a

BeanContextServicesListener

to this BeanContext

**Parameters:**
- bcsl

- the

BeanContextServicesListener

to add

---

#### void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)

Removes a

BeanContextServicesListener

from this

BeanContext

**Parameters:**
- bcsl

- the

BeanContextServicesListener

to remove from this context

---

### Additional Sections

#### Interface BeanContextServices

**All Superinterfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

,

BeanContextServicesListener

,

Collection

,

DesignMode

,

EventListener

,

Iterable

,

Visibility

**All Known Implementing Classes:** BeanContextServicesSupport

```java
public interface
BeanContextServices

extends
BeanContext
,
BeanContextServicesListener
```

The BeanContextServices interface provides a mechanism for a BeanContext
to expose generic "services" to the BeanContextChild objects within.

public interface

BeanContextServices

extends

BeanContext

,

BeanContextServicesListener

The BeanContextServices interface provides a mechanism for a BeanContext
to expose generic "services" to the BeanContextChild objects within.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.beans.beancontext.

BeanContext

globalHierarchyLock

- Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

Adds a

BeanContextServicesListener

to this BeanContext

boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider)

Adds a service to this BeanContext.

Iterator

<?>

getCurrentServiceClasses

()

Gets the currently available services for this context.

Iterator

<?>

getCurrentServiceSelectors

​(

Class

<?> serviceClass)

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

Object

getService

​(

BeanContextChild

child,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector,

BeanContextServiceRevokedListener

bcsrl)

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method.

boolean

hasService

​(

Class

<?> serviceClass)

Reports whether or not a given service is
currently available from this context.

void

releaseService

​(

BeanContextChild

child,

Object

requestor,

Object

service)

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

void

removeBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

Removes a

BeanContextServicesListener

from this

BeanContext

void

revokeService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider,
boolean revokeCurrentServicesNow)

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method.

- Methods declared in interface java.beans.beancontext.

BeanContext

addBeanContextMembershipListener

,

getResource

,

getResourceAsStream

,

instantiateChild

,

removeBeanContextMembershipListener

- Methods declared in interface java.beans.beancontext.

BeanContextChild

addPropertyChangeListener

,

addVetoableChangeListener

,

getBeanContext

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

- Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

- Methods declared in interface java.beans.beancontext.

BeanContextServicesListener

serviceAvailable

- Methods declared in interface java.util.

Collection

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

- Methods declared in interface java.beans.

DesignMode

isDesignTime

,

setDesignTime

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.beans.

Visibility

avoidingGui

,

dontUseGui

,

needsGui

,

okToUseGui

Field Summary

- Fields declared in interface java.beans.beancontext.

BeanContext

globalHierarchyLock

- Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

---

#### Field Summary

Fields declared in interface java.beans.beancontext.

BeanContext

globalHierarchyLock

---

#### Fields declared in interface java.beans.beancontext. BeanContext

Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

---

#### Fields declared in interface java.beans. DesignMode

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

Adds a

BeanContextServicesListener

to this BeanContext

boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider)

Adds a service to this BeanContext.

Iterator

<?>

getCurrentServiceClasses

()

Gets the currently available services for this context.

Iterator

<?>

getCurrentServiceSelectors

​(

Class

<?> serviceClass)

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

Object

getService

​(

BeanContextChild

child,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector,

BeanContextServiceRevokedListener

bcsrl)

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method.

boolean

hasService

​(

Class

<?> serviceClass)

Reports whether or not a given service is
currently available from this context.

void

releaseService

​(

BeanContextChild

child,

Object

requestor,

Object

service)

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

void

removeBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

Removes a

BeanContextServicesListener

from this

BeanContext

void

revokeService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider,
boolean revokeCurrentServicesNow)

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method.

- Methods declared in interface java.beans.beancontext.

BeanContext

addBeanContextMembershipListener

,

getResource

,

getResourceAsStream

,

instantiateChild

,

removeBeanContextMembershipListener

- Methods declared in interface java.beans.beancontext.

BeanContextChild

addPropertyChangeListener

,

addVetoableChangeListener

,

getBeanContext

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

- Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

- Methods declared in interface java.beans.beancontext.

BeanContextServicesListener

serviceAvailable

- Methods declared in interface java.util.

Collection

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

- Methods declared in interface java.beans.

DesignMode

isDesignTime

,

setDesignTime

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.beans.

Visibility

avoidingGui

,

dontUseGui

,

needsGui

,

okToUseGui

---

#### Method Summary

Adds a

BeanContextServicesListener

to this BeanContext

Adds a service to this BeanContext.

Gets the currently available services for this context.

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method.

Reports whether or not a given service is
currently available from this context.

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

Removes a

BeanContextServicesListener

from this

BeanContext

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method.

Methods declared in interface java.beans.beancontext.

BeanContext

addBeanContextMembershipListener

,

getResource

,

getResourceAsStream

,

instantiateChild

,

removeBeanContextMembershipListener

---

#### Methods declared in interface java.beans.beancontext. BeanContext

Methods declared in interface java.beans.beancontext.

BeanContextChild

addPropertyChangeListener

,

addVetoableChangeListener

,

getBeanContext

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

---

#### Methods declared in interface java.beans.beancontext. BeanContextChild

Methods declared in interface java.beans.beancontext.

BeanContextServiceRevokedListener

serviceRevoked

---

#### Methods declared in interface java.beans.beancontext. BeanContextServiceRevokedListener

Methods declared in interface java.beans.beancontext.

BeanContextServicesListener

serviceAvailable

---

#### Methods declared in interface java.beans.beancontext. BeanContextServicesListener

Methods declared in interface java.util.

Collection

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

parallelStream

,

remove

,

removeAll

,

removeIf

,

retainAll

,

size

,

spliterator

,

stream

,

toArray

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.beans.

DesignMode

isDesignTime

,

setDesignTime

---

#### Methods declared in interface java.beans. DesignMode

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

Methods declared in interface java.beans.

Visibility

avoidingGui

,

dontUseGui

,

needsGui

,

okToUseGui

---

#### Methods declared in interface java.beans. Visibility

============ METHOD DETAIL ==========

- Method Detail

- addService

```java
boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider)
```

Adds a service to this BeanContext.

BeanContextServiceProvider

s call this method
to register a particular service with this context.
If the service has not previously been added, the

BeanContextServices

associates
the service with the

BeanContextServiceProvider

and
fires a

BeanContextServiceAvailableEvent

to all
currently registered

BeanContextServicesListeners

.
The method then returns

true

, indicating that
the addition of the service was successful.
If the given service has already been added, this method
simply returns

false

.

**Parameters:** serviceClass

- the service to add
**Parameters:** serviceProvider

- the

BeanContextServiceProvider

associated with the service
**Returns:** true if the service was successful added, false otherwise

- revokeService

```java
void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider,
boolean revokeCurrentServicesNow)
```

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method. Upon revocation of
the service, the

BeanContextServices

fires a

BeanContextServiceRevokedEvent

to its
list of currently registered

BeanContextServiceRevokedListeners

and

BeanContextServicesListeners

.

**Parameters:** serviceClass

- the service to revoke from this BeanContextServices
**Parameters:** serviceProvider

- the BeanContextServiceProvider associated with
this particular service that is being revoked
**Parameters:** revokeCurrentServicesNow

- a value of

true

indicates an exceptional circumstance where the

BeanContextServiceProvider

or

BeanContextServices

wishes to immediately
terminate service to all currently outstanding references
to the specified service.

- hasService

```java
boolean hasService​(
Class
<?> serviceClass)
```

Reports whether or not a given service is
currently available from this context.

**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

- getService

```java
Object
getService​(
BeanContextChild
child,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector,

BeanContextServiceRevokedListener
bcsrl)
throws
TooManyListenersException
```

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method. When invoked, this method
gets the service by calling the getService() method on the
underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild

associated with this request
**Parameters:** requestor

- the object requesting the service
**Parameters:** serviceClass

- class of the requested service
**Parameters:** serviceSelector

- the service dependent parameter
**Parameters:** bcsrl

- the

BeanContextServiceRevokedListener

to notify
if the service should later become revoked
**Returns:** a reference to this context's named
Service as requested or

null
**Throws:** TooManyListenersException

- if there are too many listeners

- releaseService

```java
void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

- getCurrentServiceClasses

```java
Iterator
<?> getCurrentServiceClasses()
```

Gets the currently available services for this context.

**Returns:** an

Iterator

consisting of the
currently available services

- getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Parameters:** serviceClass

- the specified service
**Returns:** the currently available service selectors
for the named serviceClass

- addBeanContextServicesListener

```java
void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Adds a

BeanContextServicesListener

to this BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to add

- removeBeanContextServicesListener

```java
void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Removes a

BeanContextServicesListener

from this

BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

Method Detail

- addService

```java
boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider)
```

Adds a service to this BeanContext.

BeanContextServiceProvider

s call this method
to register a particular service with this context.
If the service has not previously been added, the

BeanContextServices

associates
the service with the

BeanContextServiceProvider

and
fires a

BeanContextServiceAvailableEvent

to all
currently registered

BeanContextServicesListeners

.
The method then returns

true

, indicating that
the addition of the service was successful.
If the given service has already been added, this method
simply returns

false

.

**Parameters:** serviceClass

- the service to add
**Parameters:** serviceProvider

- the

BeanContextServiceProvider

associated with the service
**Returns:** true if the service was successful added, false otherwise

- revokeService

```java
void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider,
boolean revokeCurrentServicesNow)
```

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method. Upon revocation of
the service, the

BeanContextServices

fires a

BeanContextServiceRevokedEvent

to its
list of currently registered

BeanContextServiceRevokedListeners

and

BeanContextServicesListeners

.

**Parameters:** serviceClass

- the service to revoke from this BeanContextServices
**Parameters:** serviceProvider

- the BeanContextServiceProvider associated with
this particular service that is being revoked
**Parameters:** revokeCurrentServicesNow

- a value of

true

indicates an exceptional circumstance where the

BeanContextServiceProvider

or

BeanContextServices

wishes to immediately
terminate service to all currently outstanding references
to the specified service.

- hasService

```java
boolean hasService​(
Class
<?> serviceClass)
```

Reports whether or not a given service is
currently available from this context.

**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

- getService

```java
Object
getService​(
BeanContextChild
child,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector,

BeanContextServiceRevokedListener
bcsrl)
throws
TooManyListenersException
```

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method. When invoked, this method
gets the service by calling the getService() method on the
underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild

associated with this request
**Parameters:** requestor

- the object requesting the service
**Parameters:** serviceClass

- class of the requested service
**Parameters:** serviceSelector

- the service dependent parameter
**Parameters:** bcsrl

- the

BeanContextServiceRevokedListener

to notify
if the service should later become revoked
**Returns:** a reference to this context's named
Service as requested or

null
**Throws:** TooManyListenersException

- if there are too many listeners

- releaseService

```java
void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

- getCurrentServiceClasses

```java
Iterator
<?> getCurrentServiceClasses()
```

Gets the currently available services for this context.

**Returns:** an

Iterator

consisting of the
currently available services

- getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Parameters:** serviceClass

- the specified service
**Returns:** the currently available service selectors
for the named serviceClass

- addBeanContextServicesListener

```java
void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Adds a

BeanContextServicesListener

to this BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to add

- removeBeanContextServicesListener

```java
void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Removes a

BeanContextServicesListener

from this

BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

---

#### Method Detail

addService

```java
boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider)
```

Adds a service to this BeanContext.

BeanContextServiceProvider

s call this method
to register a particular service with this context.
If the service has not previously been added, the

BeanContextServices

associates
the service with the

BeanContextServiceProvider

and
fires a

BeanContextServiceAvailableEvent

to all
currently registered

BeanContextServicesListeners

.
The method then returns

true

, indicating that
the addition of the service was successful.
If the given service has already been added, this method
simply returns

false

.

**Parameters:** serviceClass

- the service to add
**Parameters:** serviceProvider

- the

BeanContextServiceProvider

associated with the service
**Returns:** true if the service was successful added, false otherwise

---

#### addService

boolean addService​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider)

Adds a service to this BeanContext.

BeanContextServiceProvider

s call this method
to register a particular service with this context.
If the service has not previously been added, the

BeanContextServices

associates
the service with the

BeanContextServiceProvider

and
fires a

BeanContextServiceAvailableEvent

to all
currently registered

BeanContextServicesListeners

.
The method then returns

true

, indicating that
the addition of the service was successful.
If the given service has already been added, this method
simply returns

false

.

revokeService

```java
void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
serviceProvider,
boolean revokeCurrentServicesNow)
```

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method. Upon revocation of
the service, the

BeanContextServices

fires a

BeanContextServiceRevokedEvent

to its
list of currently registered

BeanContextServiceRevokedListeners

and

BeanContextServicesListeners

.

**Parameters:** serviceClass

- the service to revoke from this BeanContextServices
**Parameters:** serviceProvider

- the BeanContextServiceProvider associated with
this particular service that is being revoked
**Parameters:** revokeCurrentServicesNow

- a value of

true

indicates an exceptional circumstance where the

BeanContextServiceProvider

or

BeanContextServices

wishes to immediately
terminate service to all currently outstanding references
to the specified service.

---

#### revokeService

void revokeService​(

Class

<?> serviceClass,

BeanContextServiceProvider

serviceProvider,
boolean revokeCurrentServicesNow)

BeanContextServiceProviders wishing to remove
a currently registered service from this context
may do so via invocation of this method. Upon revocation of
the service, the

BeanContextServices

fires a

BeanContextServiceRevokedEvent

to its
list of currently registered

BeanContextServiceRevokedListeners

and

BeanContextServicesListeners

.

hasService

```java
boolean hasService​(
Class
<?> serviceClass)
```

Reports whether or not a given service is
currently available from this context.

**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

---

#### hasService

boolean hasService​(

Class

<?> serviceClass)

Reports whether or not a given service is
currently available from this context.

getService

```java
Object
getService​(
BeanContextChild
child,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector,

BeanContextServiceRevokedListener
bcsrl)
throws
TooManyListenersException
```

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method. When invoked, this method
gets the service by calling the getService() method on the
underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild

associated with this request
**Parameters:** requestor

- the object requesting the service
**Parameters:** serviceClass

- class of the requested service
**Parameters:** serviceSelector

- the service dependent parameter
**Parameters:** bcsrl

- the

BeanContextServiceRevokedListener

to notify
if the service should later become revoked
**Returns:** a reference to this context's named
Service as requested or

null
**Throws:** TooManyListenersException

- if there are too many listeners

---

#### getService

Object

getService​(

BeanContextChild

child,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector,

BeanContextServiceRevokedListener

bcsrl)
throws

TooManyListenersException

A

BeanContextChild

, or any arbitrary object
associated with a

BeanContextChild

, may obtain
a reference to a currently registered service from its
nesting

BeanContextServices

via invocation of this method. When invoked, this method
gets the service by calling the getService() method on the
underlying

BeanContextServiceProvider

.

releaseService

```java
void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

---

#### releaseService

void releaseService​(

BeanContextChild

child,

Object

requestor,

Object

service)

Releases a

BeanContextChild

's
(or any arbitrary object associated with a BeanContextChild)
reference to the specified service by calling releaseService()
on the underlying

BeanContextServiceProvider

.

getCurrentServiceClasses

```java
Iterator
<?> getCurrentServiceClasses()
```

Gets the currently available services for this context.

**Returns:** an

Iterator

consisting of the
currently available services

---

#### getCurrentServiceClasses

Iterator

<?> getCurrentServiceClasses()

Gets the currently available services for this context.

getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Parameters:** serviceClass

- the specified service
**Returns:** the currently available service selectors
for the named serviceClass

---

#### getCurrentServiceSelectors

Iterator

<?> getCurrentServiceSelectors​(

Class

<?> serviceClass)

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

addBeanContextServicesListener

```java
void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Adds a

BeanContextServicesListener

to this BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to add

---

#### addBeanContextServicesListener

void addBeanContextServicesListener​(

BeanContextServicesListener

bcsl)

Adds a

BeanContextServicesListener

to this BeanContext

removeBeanContextServicesListener

```java
void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

Removes a

BeanContextServicesListener

from this

BeanContext

**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

---

#### removeBeanContextServicesListener

void removeBeanContextServicesListener​(

BeanContextServicesListener

bcsl)

Removes a

BeanContextServicesListener

from this

BeanContext

---

