# Class BeanContextServicesSupport

**Source:** `java.desktop\java\beans\beancontext\BeanContextServicesSupport.html`

### Class Description

```java
public class
BeanContextServicesSupport

extends
BeanContextSupport

implements
BeanContextServices
```

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContextServices interface.

Since this class directly implements the BeanContextServices interface,
the class can, and is intended to be used either by subclassing this
implementation, or via delegation of an instance of this class
from another through the BeanContextProxy interface.

**All Implemented Interfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

,

BeanContextServices

,

BeanContextServicesListener

,

DesignMode

,

PropertyChangeListener

,

VetoableChangeListener

,

Visibility

,

Serializable

,

Iterable

,

Collection

,

EventListener

---

### Field Details

#### protected transient
HashMap
<
Object
,​
BeanContextServicesSupport.BCSSServiceProvider
> services

all accesses to the

protected transient HashMap services

field should be synchronized on that object

---

#### protected transient int serializable

The number of instances of a serializable

BeanContextServceProvider

.

---

#### protected transient
BeanContextServicesSupport.BCSSProxyServiceProvider
proxy

Delegate for the

BeanContextServiceProvider

.

---

#### protected transient
ArrayList
<
BeanContextServicesListener
> bcsListeners

List of

BeanContextServicesListener

objects.

---

### Constructor Details

#### public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dTime,
boolean visible)

Construct a BeanContextServicesSupport instance

**Parameters:**
- peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
- lcle

- The current Locale for this BeanContext.
- dTime

- The initial state, true if in design mode, false if runtime.
- visible

- The initial visibility.

---

#### public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

**Parameters:**
- peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
- lcle

- The current Locale for this BeanContext.
- dtime

- The initial state, true if in design mode, false if runtime.

---

#### public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle)

Create an instance using the specified locale

**Parameters:**
- peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
- lcle

- The current Locale for this BeanContext.

---

#### public BeanContextServicesSupport​(
BeanContextServices
peer)

Create an instance with a peer

**Parameters:**
- peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer

---

#### public BeanContextServicesSupport()

Create an instance that is not a delegate of another object

---

### Method Details

#### public void initialize()

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

subclasses may envelope this method, but should not override it or
call it directly.

**Overrides:**
- initialize

in class

BeanContextSupport

---

#### public
BeanContextServices
getBeanContextServicesPeer()

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

**Returns:**
- the instance of

BeanContext

this object is providing the implementation for.

---

#### protected
BeanContextSupport.BCSChild
createBCSChild​(
Object
targetChild,

Object
peer)

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

**Overrides:**
- createBCSChild

in class

BeanContextSupport

**Parameters:**
- targetChild

- the child to create the Child on behalf of
- peer

- the peer if the targetChild and peer are related by BeanContextProxy

**Returns:**
- Subtype-specific subclass of Child without overriding collection methods

---

#### protected
BeanContextServicesSupport.BCSSServiceProvider
createBCSSServiceProvider​(
Class
<?> sc,

BeanContextServiceProvider
bcsp)

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

**Parameters:**
- sc

- the class
- bcsp

- the service provider

**Returns:**
- a service provider without overriding addService()

---

#### public void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)

add a BeanContextServicesListener

**Specified by:**
- addBeanContextServicesListener

in interface

BeanContextServices

**Parameters:**
- bcsl

- the

BeanContextServicesListener

to add

**Throws:**
- NullPointerException

- if the argument is null

---

#### public void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)

remove a BeanContextServicesListener

**Specified by:**
- removeBeanContextServicesListener

in interface

BeanContextServices

**Parameters:**
- bcsl

- the

BeanContextServicesListener

to remove from this context

---

#### public boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp)

add a service

**Specified by:**
- addService

in interface

BeanContextServices

**Parameters:**
- serviceClass

- the service class
- bcsp

- the service provider

**Returns:**
- true if the service was successful added, false otherwise

---

#### protected boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean fireEvent)

add a service

**Parameters:**
- serviceClass

- the service class
- bcsp

- the service provider
- fireEvent

- whether or not an event should be fired

**Returns:**
- true if the service was successfully added

---

#### public void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean revokeCurrentServicesNow)

remove a service

**Specified by:**
- revokeService

in interface

BeanContextServices

**Parameters:**
- serviceClass

- the service class
- bcsp

- the service provider
- revokeCurrentServicesNow

- whether or not to revoke the service

---

#### public boolean hasService​(
Class
<?> serviceClass)

has a service, which may be delegated

**Specified by:**
- hasService

in interface

BeanContextServices

**Parameters:**
- serviceClass

- the service in question

**Returns:**
- true if the service is available

---

#### public
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

obtain a service which may be delegated

**Specified by:**
- getService

in interface

BeanContextServices

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

#### public void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)

release a service

**Specified by:**
- releaseService

in interface

BeanContextServices

**Parameters:**
- child

- the

BeanContextChild
- requestor

- the requestor
- service

- the service

---

#### public
Iterator
<
Object
> getCurrentServiceClasses()

Description copied from interface:

BeanContextServices

**Specified by:**
- getCurrentServiceClasses

in interface

BeanContextServices

**Returns:**
- an iterator for all the currently registered service classes.

---

#### public
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)

Description copied from interface:

BeanContextServices

**Specified by:**
- getCurrentServiceSelectors

in interface

BeanContextServices

**Parameters:**
- serviceClass

- the specified service

**Returns:**
- an iterator for all the currently available service selectors
(if any) available for the specified service.

---

#### public void serviceAvailable​(
BeanContextServiceAvailableEvent
bcssae)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:**
- serviceAvailable

in interface

BeanContextServicesListener

**Overrides:**
- serviceAvailable

in class

BeanContextChildSupport

**Parameters:**
- bcssae

- The BeanContextServiceAvailableEvent fired as a
result of a service becoming available

---

#### public void serviceRevoked​(
BeanContextServiceRevokedEvent
bcssre)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:**
- serviceRevoked

in interface

BeanContextServiceRevokedListener

**Overrides:**
- serviceRevoked

in class

BeanContextChildSupport

**Parameters:**
- bcssre

- The

BeanContextServiceRevokedEvent

fired as a
result of a service being revoked

---

#### protected static final
BeanContextServicesListener
getChildBeanContextServicesListener​(
Object
child)

Gets the

BeanContextServicesListener

(if any) of the specified
child.

**Parameters:**
- child

- the specified child

**Returns:**
- the BeanContextServicesListener (if any) of the specified child

---

#### protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

This subclass uses this hook to immediately revoke any services
being used by this child if it is a BeanContextChild.

subclasses may envelope this method in order to implement their
own child removal side-effects.

**Overrides:**
- childJustRemovedHook

in class

BeanContextSupport

**Parameters:**
- child

- the child
- bcsc

- the BCSChild

---

#### protected void releaseBeanContextResources()

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

This method revokes any services obtained from its parent.

subclasses may envelope this method to implement their own semantics.

**Overrides:**
- releaseBeanContextResources

in class

BeanContextChildSupport

---

#### protected void initializeBeanContextResources()

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

subclasses may envelope this method to implement their own semantics.

**Overrides:**
- initializeBeanContextResources

in class

BeanContextChildSupport

---

#### protected final void fireServiceAdded​(
Class
<?> serviceClass)

Fires a

BeanContextServiceEvent

notifying of a new service.

**Parameters:**
- serviceClass

- the service class

---

#### protected final void fireServiceAdded​(
BeanContextServiceAvailableEvent
bcssae)

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

**Parameters:**
- bcssae

- the

BeanContextServiceAvailableEvent

---

#### protected final void fireServiceRevoked​(
BeanContextServiceRevokedEvent
bcsre)

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

**Parameters:**
- bcsre

- the

BeanContextServiceRevokedEvent

---

#### protected final void fireServiceRevoked​(
Class
<?> serviceClass,
boolean revokeNow)

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

**Parameters:**
- serviceClass

- the service class
- revokeNow

- whether or not the event should be revoked now

---

#### protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException

called from BeanContextSupport writeObject before it serializes the
children ...

This class will serialize any Serializable BeanContextServiceProviders
herein.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:**
- bcsPreSerializationHook

in class

BeanContextSupport

**Parameters:**
- oos

- the

ObjectOutputStream

to use during serialization

**Throws:**
- IOException

- if serialization failed

---

#### protected void bcsPreDeserializationHook​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException

called from BeanContextSupport readObject before it deserializes the
children ...

This class will deserialize any Serializable BeanContextServiceProviders
serialized earlier thus making them available to the children when they
deserialized.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:**
- bcsPreDeserializationHook

in class

BeanContextSupport

**Parameters:**
- ois

- the

ObjectInputStream

to use during deserialization

**Throws:**
- IOException

- if deserialization failed
- ClassNotFoundException

- if needed classes are not found

---

### Additional Sections

#### Class BeanContextServicesSupport

java.lang.Object

- java.beans.beancontext.BeanContextChildSupport
- - java.beans.beancontext.BeanContextSupport
- - java.beans.beancontext.BeanContextServicesSupport

java.beans.beancontext.BeanContextChildSupport

- java.beans.beancontext.BeanContextSupport
- - java.beans.beancontext.BeanContextServicesSupport

java.beans.beancontext.BeanContextSupport

- java.beans.beancontext.BeanContextServicesSupport

java.beans.beancontext.BeanContextServicesSupport

**All Implemented Interfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

,

BeanContextServices

,

BeanContextServicesListener

,

DesignMode

,

PropertyChangeListener

,

VetoableChangeListener

,

Visibility

,

Serializable

,

Iterable

,

Collection

,

EventListener

```java
public class
BeanContextServicesSupport

extends
BeanContextSupport

implements
BeanContextServices
```

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContextServices interface.

Since this class directly implements the BeanContextServices interface,
the class can, and is intended to be used either by subclassing this
implementation, or via delegation of an instance of this class
from another through the BeanContextProxy interface.

**Since:** 1.2
**See Also:** Serialized Form

public class

BeanContextServicesSupport

extends

BeanContextSupport

implements

BeanContextServices

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContextServices interface.

Since this class directly implements the BeanContextServices interface,
the class can, and is intended to be used either by subclassing this
implementation, or via delegation of an instance of this class
from another through the BeanContextProxy interface.

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContextServices interface.

Since this class directly implements the BeanContextServices interface,
the class can, and is intended to be used either by subclassing this
implementation, or via delegation of an instance of this class
from another through the BeanContextProxy interface.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BeanContextServicesSupport.BCSSChild

protected class

BeanContextServicesSupport.BCSSProxyServiceProvider

protected static class

BeanContextServicesSupport.BCSSServiceProvider

subclasses may subclass this nested class to add behaviors for
each BeanContextServicesProvider.

- Nested classes/interfaces declared in class java.beans.beancontext.

BeanContextSupport

BeanContextSupport.BCSChild

,

BeanContextSupport.BCSIterator

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ArrayList

<

BeanContextServicesListener

>

bcsListeners

List of

BeanContextServicesListener

objects.

protected

BeanContextServicesSupport.BCSSProxyServiceProvider

proxy

Delegate for the

BeanContextServiceProvider

.

protected int

serializable

The number of instances of a serializable

BeanContextServceProvider

.

protected

HashMap

<

Object

,​

BeanContextServicesSupport.BCSSServiceProvider

>

services

all accesses to the

protected transient HashMap services

field should be synchronized on that object

- Fields declared in class java.beans.beancontext.

BeanContextSupport

bcmListeners

,

children

,

designTime

,

locale

,

okToUseGui

- Fields declared in class java.beans.beancontext.

BeanContextChildSupport

beanContext

,

beanContextChildPeer

,

pcSupport

,

rejectedSetBCOnce

,

vcSupport

- Fields declared in interface java.beans.beancontext.

BeanContext

globalHierarchyLock

- Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BeanContextServicesSupport

()

Create an instance that is not a delegate of another object

BeanContextServicesSupport

​(

BeanContextServices

peer)

Create an instance with a peer

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextServicesSupport instance

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

add a BeanContextServicesListener

boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp)

add a service

protected boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean fireEvent)

add a service

protected void

bcsPreDeserializationHook

​(

ObjectInputStream

ois)

called from BeanContextSupport readObject before it deserializes the
children ...

protected void

bcsPreSerializationHook

​(

ObjectOutputStream

oos)

called from BeanContextSupport writeObject before it serializes the
children ...

protected void

childJustRemovedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

protected

BeanContextSupport.BCSChild

createBCSChild

​(

Object

targetChild,

Object

peer)

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

protected

BeanContextServicesSupport.BCSSServiceProvider

createBCSSServiceProvider

​(

Class

<?> sc,

BeanContextServiceProvider

bcsp)

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

protected void

fireServiceAdded

​(

BeanContextServiceAvailableEvent

bcssae)

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

protected void

fireServiceAdded

​(

Class

<?> serviceClass)

Fires a

BeanContextServiceEvent

notifying of a new service.

protected void

fireServiceRevoked

​(

BeanContextServiceRevokedEvent

bcsre)

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

protected void

fireServiceRevoked

​(

Class

<?> serviceClass,
boolean revokeNow)

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

BeanContextServices

getBeanContextServicesPeer

()

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

protected static

BeanContextServicesListener

getChildBeanContextServicesListener

​(

Object

child)

Gets the

BeanContextServicesListener

(if any) of the specified
child.

Iterator

<

Object

>

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

obtain a service which may be delegated

boolean

hasService

​(

Class

<?> serviceClass)

has a service, which may be delegated

void

initialize

()

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

protected void

initializeBeanContextResources

()

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

protected void

releaseBeanContextResources

()

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

void

releaseService

​(

BeanContextChild

child,

Object

requestor,

Object

service)

release a service

void

removeBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

remove a BeanContextServicesListener

void

revokeService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean revokeCurrentServicesNow)

remove a service

void

serviceAvailable

​(

BeanContextServiceAvailableEvent

bcssae)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

void

serviceRevoked

​(

BeanContextServiceRevokedEvent

bcssre)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

- Methods declared in class java.beans.beancontext.

BeanContextSupport

add

,

addAll

,

addBeanContextMembershipListener

,

avoidingGui

,

bcsChildren

,

childDeserializedHook

,

childJustAddedHook

,

classEquals

,

clear

,

contains

,

containsAll

,

containsKey

,

copyChildren

,

deserialize

,

dontUseGui

,

fireChildrenAdded

,

fireChildrenRemoved

,

getBeanContextPeer

,

getChildBeanContextChild

,

getChildBeanContextMembershipListener

,

getChildPropertyChangeListener

,

getChildSerializable

,

getChildVetoableChangeListener

,

getChildVisibility

,

getLocale

,

getResource

,

getResourceAsStream

,

instantiateChild

,

isDesignTime

,

isEmpty

,

isSerializing

,

iterator

,

needsGui

,

okToUseGui

,

propertyChange

,

readChildren

,

remove

,

remove

,

removeAll

,

removeBeanContextMembershipListener

,

retainAll

,

serialize

,

setDesignTime

,

setLocale

,

size

,

toArray

,

toArray

,

validatePendingAdd

,

validatePendingRemove

,

vetoableChange

,

writeChildren

- Methods declared in class java.beans.beancontext.

BeanContextChildSupport

addPropertyChangeListener

,

addVetoableChangeListener

,

firePropertyChange

,

fireVetoableChange

,

getBeanContext

,

getBeanContextChildPeer

,

isDelegated

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

,

validatePendingSetBeanContext

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BeanContextServicesSupport.BCSSChild

protected class

BeanContextServicesSupport.BCSSProxyServiceProvider

protected static class

BeanContextServicesSupport.BCSSServiceProvider

subclasses may subclass this nested class to add behaviors for
each BeanContextServicesProvider.

- Nested classes/interfaces declared in class java.beans.beancontext.

BeanContextSupport

BeanContextSupport.BCSChild

,

BeanContextSupport.BCSIterator

---

#### Nested Class Summary

subclasses may subclass this nested class to add behaviors for
each BeanContextServicesProvider.

Nested classes/interfaces declared in class java.beans.beancontext.

BeanContextSupport

BeanContextSupport.BCSChild

,

BeanContextSupport.BCSIterator

---

#### Nested classes/interfaces declared in class java.beans.beancontext. BeanContextSupport

Field Summary

Fields

Modifier and Type

Field

Description

protected

ArrayList

<

BeanContextServicesListener

>

bcsListeners

List of

BeanContextServicesListener

objects.

protected

BeanContextServicesSupport.BCSSProxyServiceProvider

proxy

Delegate for the

BeanContextServiceProvider

.

protected int

serializable

The number of instances of a serializable

BeanContextServceProvider

.

protected

HashMap

<

Object

,​

BeanContextServicesSupport.BCSSServiceProvider

>

services

all accesses to the

protected transient HashMap services

field should be synchronized on that object

- Fields declared in class java.beans.beancontext.

BeanContextSupport

bcmListeners

,

children

,

designTime

,

locale

,

okToUseGui

- Fields declared in class java.beans.beancontext.

BeanContextChildSupport

beanContext

,

beanContextChildPeer

,

pcSupport

,

rejectedSetBCOnce

,

vcSupport

- Fields declared in interface java.beans.beancontext.

BeanContext

globalHierarchyLock

- Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

---

#### Field Summary

List of

BeanContextServicesListener

objects.

Delegate for the

BeanContextServiceProvider

.

The number of instances of a serializable

BeanContextServceProvider

.

all accesses to the

protected transient HashMap services

field should be synchronized on that object

Fields declared in class java.beans.beancontext.

BeanContextSupport

bcmListeners

,

children

,

designTime

,

locale

,

okToUseGui

---

#### Fields declared in class java.beans.beancontext. BeanContextSupport

Fields declared in class java.beans.beancontext.

BeanContextChildSupport

beanContext

,

beanContextChildPeer

,

pcSupport

,

rejectedSetBCOnce

,

vcSupport

---

#### Fields declared in class java.beans.beancontext. BeanContextChildSupport

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

Constructor Summary

Constructors

Constructor

Description

BeanContextServicesSupport

()

Create an instance that is not a delegate of another object

BeanContextServicesSupport

​(

BeanContextServices

peer)

Create an instance with a peer

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextServicesSupport

​(

BeanContextServices

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextServicesSupport instance

---

#### Constructor Summary

Create an instance that is not a delegate of another object

Create an instance with a peer

Create an instance using the specified locale

Create an instance using the specified Locale and design mode.

Construct a BeanContextServicesSupport instance

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

add a BeanContextServicesListener

boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp)

add a service

protected boolean

addService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean fireEvent)

add a service

protected void

bcsPreDeserializationHook

​(

ObjectInputStream

ois)

called from BeanContextSupport readObject before it deserializes the
children ...

protected void

bcsPreSerializationHook

​(

ObjectOutputStream

oos)

called from BeanContextSupport writeObject before it serializes the
children ...

protected void

childJustRemovedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

protected

BeanContextSupport.BCSChild

createBCSChild

​(

Object

targetChild,

Object

peer)

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

protected

BeanContextServicesSupport.BCSSServiceProvider

createBCSSServiceProvider

​(

Class

<?> sc,

BeanContextServiceProvider

bcsp)

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

protected void

fireServiceAdded

​(

BeanContextServiceAvailableEvent

bcssae)

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

protected void

fireServiceAdded

​(

Class

<?> serviceClass)

Fires a

BeanContextServiceEvent

notifying of a new service.

protected void

fireServiceRevoked

​(

BeanContextServiceRevokedEvent

bcsre)

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

protected void

fireServiceRevoked

​(

Class

<?> serviceClass,
boolean revokeNow)

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

BeanContextServices

getBeanContextServicesPeer

()

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

protected static

BeanContextServicesListener

getChildBeanContextServicesListener

​(

Object

child)

Gets the

BeanContextServicesListener

(if any) of the specified
child.

Iterator

<

Object

>

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

obtain a service which may be delegated

boolean

hasService

​(

Class

<?> serviceClass)

has a service, which may be delegated

void

initialize

()

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

protected void

initializeBeanContextResources

()

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

protected void

releaseBeanContextResources

()

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

void

releaseService

​(

BeanContextChild

child,

Object

requestor,

Object

service)

release a service

void

removeBeanContextServicesListener

​(

BeanContextServicesListener

bcsl)

remove a BeanContextServicesListener

void

revokeService

​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean revokeCurrentServicesNow)

remove a service

void

serviceAvailable

​(

BeanContextServiceAvailableEvent

bcssae)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

void

serviceRevoked

​(

BeanContextServiceRevokedEvent

bcssre)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

- Methods declared in class java.beans.beancontext.

BeanContextSupport

add

,

addAll

,

addBeanContextMembershipListener

,

avoidingGui

,

bcsChildren

,

childDeserializedHook

,

childJustAddedHook

,

classEquals

,

clear

,

contains

,

containsAll

,

containsKey

,

copyChildren

,

deserialize

,

dontUseGui

,

fireChildrenAdded

,

fireChildrenRemoved

,

getBeanContextPeer

,

getChildBeanContextChild

,

getChildBeanContextMembershipListener

,

getChildPropertyChangeListener

,

getChildSerializable

,

getChildVetoableChangeListener

,

getChildVisibility

,

getLocale

,

getResource

,

getResourceAsStream

,

instantiateChild

,

isDesignTime

,

isEmpty

,

isSerializing

,

iterator

,

needsGui

,

okToUseGui

,

propertyChange

,

readChildren

,

remove

,

remove

,

removeAll

,

removeBeanContextMembershipListener

,

retainAll

,

serialize

,

setDesignTime

,

setLocale

,

size

,

toArray

,

toArray

,

validatePendingAdd

,

validatePendingRemove

,

vetoableChange

,

writeChildren

- Methods declared in class java.beans.beancontext.

BeanContextChildSupport

addPropertyChangeListener

,

addVetoableChangeListener

,

firePropertyChange

,

fireVetoableChange

,

getBeanContext

,

getBeanContextChildPeer

,

isDelegated

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

,

validatePendingSetBeanContext

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

add a BeanContextServicesListener

add a service

called from BeanContextSupport readObject before it deserializes the
children ...

called from BeanContextSupport writeObject before it serializes the
children ...

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

Fires a

BeanContextServiceEvent

notifying of a new service.

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

Gets the

BeanContextServicesListener

(if any) of the specified
child.

Gets the currently available services for this context.

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

obtain a service which may be delegated

has a service, which may be delegated

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

release a service

remove a BeanContextServicesListener

remove a service

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

Methods declared in class java.beans.beancontext.

BeanContextSupport

add

,

addAll

,

addBeanContextMembershipListener

,

avoidingGui

,

bcsChildren

,

childDeserializedHook

,

childJustAddedHook

,

classEquals

,

clear

,

contains

,

containsAll

,

containsKey

,

copyChildren

,

deserialize

,

dontUseGui

,

fireChildrenAdded

,

fireChildrenRemoved

,

getBeanContextPeer

,

getChildBeanContextChild

,

getChildBeanContextMembershipListener

,

getChildPropertyChangeListener

,

getChildSerializable

,

getChildVetoableChangeListener

,

getChildVisibility

,

getLocale

,

getResource

,

getResourceAsStream

,

instantiateChild

,

isDesignTime

,

isEmpty

,

isSerializing

,

iterator

,

needsGui

,

okToUseGui

,

propertyChange

,

readChildren

,

remove

,

remove

,

removeAll

,

removeBeanContextMembershipListener

,

retainAll

,

serialize

,

setDesignTime

,

setLocale

,

size

,

toArray

,

toArray

,

validatePendingAdd

,

validatePendingRemove

,

vetoableChange

,

writeChildren

---

#### Methods declared in class java.beans.beancontext. BeanContextSupport

Methods declared in class java.beans.beancontext.

BeanContextChildSupport

addPropertyChangeListener

,

addVetoableChangeListener

,

firePropertyChange

,

fireVetoableChange

,

getBeanContext

,

getBeanContextChildPeer

,

isDelegated

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

setBeanContext

,

validatePendingSetBeanContext

---

#### Methods declared in class java.beans.beancontext. BeanContextChildSupport

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

============ FIELD DETAIL ===========

- Field Detail

- services

```java
protected transient
HashMap
<
Object
,​
BeanContextServicesSupport.BCSSServiceProvider
> services
```

all accesses to the

protected transient HashMap services

field should be synchronized on that object

- serializable

```java
protected transient int serializable
```

The number of instances of a serializable

BeanContextServceProvider

.

- proxy

```java
protected transient
BeanContextServicesSupport.BCSSProxyServiceProvider
proxy
```

Delegate for the

BeanContextServiceProvider

.

- bcsListeners

```java
protected transient
ArrayList
<
BeanContextServicesListener
> bcsListeners
```

List of

BeanContextServicesListener

objects.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextServicesSupport instance

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dTime

- The initial state, true if in design mode, false if runtime.
**Parameters:** visible

- The initial visibility.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dtime

- The initial state, true if in design mode, false if runtime.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer)
```

Create an instance with a peer

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer

- BeanContextServicesSupport

```java
public BeanContextServicesSupport()
```

Create an instance that is not a delegate of another object

============ METHOD DETAIL ==========

- Method Detail

- initialize

```java
public void initialize()
```

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

subclasses may envelope this method, but should not override it or
call it directly.

**Overrides:** initialize

in class

BeanContextSupport

- getBeanContextServicesPeer

```java
public
BeanContextServices
getBeanContextServicesPeer()
```

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

**Returns:** the instance of

BeanContext

this object is providing the implementation for.

- createBCSChild

```java
protected
BeanContextSupport.BCSChild
createBCSChild​(
Object
targetChild,

Object
peer)
```

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

**Overrides:** createBCSChild

in class

BeanContextSupport
**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the targetChild and peer are related by BeanContextProxy
**Returns:** Subtype-specific subclass of Child without overriding collection methods

- createBCSSServiceProvider

```java
protected
BeanContextServicesSupport.BCSSServiceProvider
createBCSSServiceProvider​(
Class
<?> sc,

BeanContextServiceProvider
bcsp)
```

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

**Parameters:** sc

- the class
**Parameters:** bcsp

- the service provider
**Returns:** a service provider without overriding addService()

- addBeanContextServicesListener

```java
public void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

add a BeanContextServicesListener

**Specified by:** addBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to add
**Throws:** NullPointerException

- if the argument is null

- removeBeanContextServicesListener

```java
public void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

remove a BeanContextServicesListener

**Specified by:** removeBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

- addService

```java
public boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp)
```

add a service

**Specified by:** addService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Returns:** true if the service was successful added, false otherwise

- addService

```java
protected boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean fireEvent)
```

add a service

**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** fireEvent

- whether or not an event should be fired
**Returns:** true if the service was successfully added

- revokeService

```java
public void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean revokeCurrentServicesNow)
```

remove a service

**Specified by:** revokeService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** revokeCurrentServicesNow

- whether or not to revoke the service

- hasService

```java
public boolean hasService​(
Class
<?> serviceClass)
```

has a service, which may be delegated

**Specified by:** hasService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

- getService

```java
public
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

obtain a service which may be delegated

**Specified by:** getService

in interface

BeanContextServices
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
public void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

release a service

**Specified by:** releaseService

in interface

BeanContextServices
**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

- getCurrentServiceClasses

```java
public
Iterator
<
Object
> getCurrentServiceClasses()
```

Description copied from interface:

BeanContextServices

Gets the currently available services for this context.

**Specified by:** getCurrentServiceClasses

in interface

BeanContextServices
**Returns:** an iterator for all the currently registered service classes.

- getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Description copied from interface:

BeanContextServices

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Specified by:** getCurrentServiceSelectors

in interface

BeanContextServices
**Parameters:** serviceClass

- the specified service
**Returns:** an iterator for all the currently available service selectors
(if any) available for the specified service.

- serviceAvailable

```java
public void serviceAvailable​(
BeanContextServiceAvailableEvent
bcssae)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceAvailable

in interface

BeanContextServicesListener
**Overrides:** serviceAvailable

in class

BeanContextChildSupport
**Parameters:** bcssae

- The BeanContextServiceAvailableEvent fired as a
result of a service becoming available

- serviceRevoked

```java
public void serviceRevoked​(
BeanContextServiceRevokedEvent
bcssre)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceRevoked

in interface

BeanContextServiceRevokedListener
**Overrides:** serviceRevoked

in class

BeanContextChildSupport
**Parameters:** bcssre

- The

BeanContextServiceRevokedEvent

fired as a
result of a service being revoked

- getChildBeanContextServicesListener

```java
protected static final
BeanContextServicesListener
getChildBeanContextServicesListener​(
Object
child)
```

Gets the

BeanContextServicesListener

(if any) of the specified
child.

**Parameters:** child

- the specified child
**Returns:** the BeanContextServicesListener (if any) of the specified child

- childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

This subclass uses this hook to immediately revoke any services
being used by this child if it is a BeanContextChild.

subclasses may envelope this method in order to implement their
own child removal side-effects.

**Overrides:** childJustRemovedHook

in class

BeanContextSupport
**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- releaseBeanContextResources

```java
protected void releaseBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

This method revokes any services obtained from its parent.

subclasses may envelope this method to implement their own semantics.

**Overrides:** releaseBeanContextResources

in class

BeanContextChildSupport

- initializeBeanContextResources

```java
protected void initializeBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

subclasses may envelope this method to implement their own semantics.

**Overrides:** initializeBeanContextResources

in class

BeanContextChildSupport

- fireServiceAdded

```java
protected final void fireServiceAdded​(
Class
<?> serviceClass)
```

Fires a

BeanContextServiceEvent

notifying of a new service.

**Parameters:** serviceClass

- the service class

- fireServiceAdded

```java
protected final void fireServiceAdded​(
BeanContextServiceAvailableEvent
bcssae)
```

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

**Parameters:** bcssae

- the

BeanContextServiceAvailableEvent

- fireServiceRevoked

```java
protected final void fireServiceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

- fireServiceRevoked

```java
protected final void fireServiceRevoked​(
Class
<?> serviceClass,
boolean revokeNow)
```

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

**Parameters:** serviceClass

- the service class
**Parameters:** revokeNow

- whether or not the event should be revoked now

- bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called from BeanContextSupport writeObject before it serializes the
children ...

This class will serialize any Serializable BeanContextServiceProviders
herein.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreSerializationHook

in class

BeanContextSupport
**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

- bcsPreDeserializationHook

```java
protected void bcsPreDeserializationHook​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

called from BeanContextSupport readObject before it deserializes the
children ...

This class will deserialize any Serializable BeanContextServiceProviders
serialized earlier thus making them available to the children when they
deserialized.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreDeserializationHook

in class

BeanContextSupport
**Parameters:** ois

- the

ObjectInputStream

to use during deserialization
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

Field Detail

- services

```java
protected transient
HashMap
<
Object
,​
BeanContextServicesSupport.BCSSServiceProvider
> services
```

all accesses to the

protected transient HashMap services

field should be synchronized on that object

- serializable

```java
protected transient int serializable
```

The number of instances of a serializable

BeanContextServceProvider

.

- proxy

```java
protected transient
BeanContextServicesSupport.BCSSProxyServiceProvider
proxy
```

Delegate for the

BeanContextServiceProvider

.

- bcsListeners

```java
protected transient
ArrayList
<
BeanContextServicesListener
> bcsListeners
```

List of

BeanContextServicesListener

objects.

---

#### Field Detail

services

```java
protected transient
HashMap
<
Object
,​
BeanContextServicesSupport.BCSSServiceProvider
> services
```

all accesses to the

protected transient HashMap services

field should be synchronized on that object

---

#### services

protected transient

HashMap

<

Object

,​

BeanContextServicesSupport.BCSSServiceProvider

> services

all accesses to the

protected transient HashMap services

field should be synchronized on that object

serializable

```java
protected transient int serializable
```

The number of instances of a serializable

BeanContextServceProvider

.

---

#### serializable

protected transient int serializable

The number of instances of a serializable

BeanContextServceProvider

.

proxy

```java
protected transient
BeanContextServicesSupport.BCSSProxyServiceProvider
proxy
```

Delegate for the

BeanContextServiceProvider

.

---

#### proxy

protected transient

BeanContextServicesSupport.BCSSProxyServiceProvider

proxy

Delegate for the

BeanContextServiceProvider

.

bcsListeners

```java
protected transient
ArrayList
<
BeanContextServicesListener
> bcsListeners
```

List of

BeanContextServicesListener

objects.

---

#### bcsListeners

protected transient

ArrayList

<

BeanContextServicesListener

> bcsListeners

List of

BeanContextServicesListener

objects.

Constructor Detail

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextServicesSupport instance

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dTime

- The initial state, true if in design mode, false if runtime.
**Parameters:** visible

- The initial visibility.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dtime

- The initial state, true if in design mode, false if runtime.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.

- BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer)
```

Create an instance with a peer

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer

- BeanContextServicesSupport

```java
public BeanContextServicesSupport()
```

Create an instance that is not a delegate of another object

---

#### Constructor Detail

BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextServicesSupport instance

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dTime

- The initial state, true if in design mode, false if runtime.
**Parameters:** visible

- The initial visibility.

---

#### BeanContextServicesSupport

public BeanContextServicesSupport​(

BeanContextServices

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextServicesSupport instance

BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.
**Parameters:** dtime

- The initial state, true if in design mode, false if runtime.

---

#### BeanContextServicesSupport

public BeanContextServicesSupport​(

BeanContextServices

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext.

---

#### BeanContextServicesSupport

public BeanContextServicesSupport​(

BeanContextServices

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextServicesSupport

```java
public BeanContextServicesSupport​(
BeanContextServices
peer)
```

Create an instance with a peer

**Parameters:** peer

- The peer BeanContext we are supplying an implementation for, if null the this object is its own peer

---

#### BeanContextServicesSupport

public BeanContextServicesSupport​(

BeanContextServices

peer)

Create an instance with a peer

BeanContextServicesSupport

```java
public BeanContextServicesSupport()
```

Create an instance that is not a delegate of another object

---

#### BeanContextServicesSupport

public BeanContextServicesSupport()

Create an instance that is not a delegate of another object

Method Detail

- initialize

```java
public void initialize()
```

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

subclasses may envelope this method, but should not override it or
call it directly.

**Overrides:** initialize

in class

BeanContextSupport

- getBeanContextServicesPeer

```java
public
BeanContextServices
getBeanContextServicesPeer()
```

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

**Returns:** the instance of

BeanContext

this object is providing the implementation for.

- createBCSChild

```java
protected
BeanContextSupport.BCSChild
createBCSChild​(
Object
targetChild,

Object
peer)
```

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

**Overrides:** createBCSChild

in class

BeanContextSupport
**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the targetChild and peer are related by BeanContextProxy
**Returns:** Subtype-specific subclass of Child without overriding collection methods

- createBCSSServiceProvider

```java
protected
BeanContextServicesSupport.BCSSServiceProvider
createBCSSServiceProvider​(
Class
<?> sc,

BeanContextServiceProvider
bcsp)
```

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

**Parameters:** sc

- the class
**Parameters:** bcsp

- the service provider
**Returns:** a service provider without overriding addService()

- addBeanContextServicesListener

```java
public void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

add a BeanContextServicesListener

**Specified by:** addBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to add
**Throws:** NullPointerException

- if the argument is null

- removeBeanContextServicesListener

```java
public void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

remove a BeanContextServicesListener

**Specified by:** removeBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

- addService

```java
public boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp)
```

add a service

**Specified by:** addService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Returns:** true if the service was successful added, false otherwise

- addService

```java
protected boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean fireEvent)
```

add a service

**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** fireEvent

- whether or not an event should be fired
**Returns:** true if the service was successfully added

- revokeService

```java
public void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean revokeCurrentServicesNow)
```

remove a service

**Specified by:** revokeService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** revokeCurrentServicesNow

- whether or not to revoke the service

- hasService

```java
public boolean hasService​(
Class
<?> serviceClass)
```

has a service, which may be delegated

**Specified by:** hasService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

- getService

```java
public
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

obtain a service which may be delegated

**Specified by:** getService

in interface

BeanContextServices
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
public void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

release a service

**Specified by:** releaseService

in interface

BeanContextServices
**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

- getCurrentServiceClasses

```java
public
Iterator
<
Object
> getCurrentServiceClasses()
```

Description copied from interface:

BeanContextServices

Gets the currently available services for this context.

**Specified by:** getCurrentServiceClasses

in interface

BeanContextServices
**Returns:** an iterator for all the currently registered service classes.

- getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Description copied from interface:

BeanContextServices

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Specified by:** getCurrentServiceSelectors

in interface

BeanContextServices
**Parameters:** serviceClass

- the specified service
**Returns:** an iterator for all the currently available service selectors
(if any) available for the specified service.

- serviceAvailable

```java
public void serviceAvailable​(
BeanContextServiceAvailableEvent
bcssae)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceAvailable

in interface

BeanContextServicesListener
**Overrides:** serviceAvailable

in class

BeanContextChildSupport
**Parameters:** bcssae

- The BeanContextServiceAvailableEvent fired as a
result of a service becoming available

- serviceRevoked

```java
public void serviceRevoked​(
BeanContextServiceRevokedEvent
bcssre)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceRevoked

in interface

BeanContextServiceRevokedListener
**Overrides:** serviceRevoked

in class

BeanContextChildSupport
**Parameters:** bcssre

- The

BeanContextServiceRevokedEvent

fired as a
result of a service being revoked

- getChildBeanContextServicesListener

```java
protected static final
BeanContextServicesListener
getChildBeanContextServicesListener​(
Object
child)
```

Gets the

BeanContextServicesListener

(if any) of the specified
child.

**Parameters:** child

- the specified child
**Returns:** the BeanContextServicesListener (if any) of the specified child

- childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

This subclass uses this hook to immediately revoke any services
being used by this child if it is a BeanContextChild.

subclasses may envelope this method in order to implement their
own child removal side-effects.

**Overrides:** childJustRemovedHook

in class

BeanContextSupport
**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- releaseBeanContextResources

```java
protected void releaseBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

This method revokes any services obtained from its parent.

subclasses may envelope this method to implement their own semantics.

**Overrides:** releaseBeanContextResources

in class

BeanContextChildSupport

- initializeBeanContextResources

```java
protected void initializeBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

subclasses may envelope this method to implement their own semantics.

**Overrides:** initializeBeanContextResources

in class

BeanContextChildSupport

- fireServiceAdded

```java
protected final void fireServiceAdded​(
Class
<?> serviceClass)
```

Fires a

BeanContextServiceEvent

notifying of a new service.

**Parameters:** serviceClass

- the service class

- fireServiceAdded

```java
protected final void fireServiceAdded​(
BeanContextServiceAvailableEvent
bcssae)
```

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

**Parameters:** bcssae

- the

BeanContextServiceAvailableEvent

- fireServiceRevoked

```java
protected final void fireServiceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

- fireServiceRevoked

```java
protected final void fireServiceRevoked​(
Class
<?> serviceClass,
boolean revokeNow)
```

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

**Parameters:** serviceClass

- the service class
**Parameters:** revokeNow

- whether or not the event should be revoked now

- bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called from BeanContextSupport writeObject before it serializes the
children ...

This class will serialize any Serializable BeanContextServiceProviders
herein.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreSerializationHook

in class

BeanContextSupport
**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

- bcsPreDeserializationHook

```java
protected void bcsPreDeserializationHook​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

called from BeanContextSupport readObject before it deserializes the
children ...

This class will deserialize any Serializable BeanContextServiceProviders
serialized earlier thus making them available to the children when they
deserialized.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreDeserializationHook

in class

BeanContextSupport
**Parameters:** ois

- the

ObjectInputStream

to use during deserialization
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

---

#### Method Detail

initialize

```java
public void initialize()
```

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

subclasses may envelope this method, but should not override it or
call it directly.

**Overrides:** initialize

in class

BeanContextSupport

---

#### initialize

public void initialize()

called by BeanContextSupport superclass during construction and
deserialization to initialize subclass transient state.

subclasses may envelope this method, but should not override it or
call it directly.

getBeanContextServicesPeer

```java
public
BeanContextServices
getBeanContextServicesPeer()
```

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

**Returns:** the instance of

BeanContext

this object is providing the implementation for.

---

#### getBeanContextServicesPeer

public

BeanContextServices

getBeanContextServicesPeer()

Gets the

BeanContextServices

associated with this

BeanContextServicesSupport

.

createBCSChild

```java
protected
BeanContextSupport.BCSChild
createBCSChild​(
Object
targetChild,

Object
peer)
```

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

**Overrides:** createBCSChild

in class

BeanContextSupport
**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the targetChild and peer are related by BeanContextProxy
**Returns:** Subtype-specific subclass of Child without overriding collection methods

---

#### createBCSChild

protected

BeanContextSupport.BCSChild

createBCSChild​(

Object

targetChild,

Object

peer)

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

createBCSSServiceProvider

```java
protected
BeanContextServicesSupport.BCSSServiceProvider
createBCSSServiceProvider​(
Class
<?> sc,

BeanContextServiceProvider
bcsp)
```

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

**Parameters:** sc

- the class
**Parameters:** bcsp

- the service provider
**Returns:** a service provider without overriding addService()

---

#### createBCSSServiceProvider

protected

BeanContextServicesSupport.BCSSServiceProvider

createBCSSServiceProvider​(

Class

<?> sc,

BeanContextServiceProvider

bcsp)

subclasses can override this method to create new subclasses of
BCSSServiceProvider without having to override addService() in
order to instantiate.

addBeanContextServicesListener

```java
public void addBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

add a BeanContextServicesListener

**Specified by:** addBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to add
**Throws:** NullPointerException

- if the argument is null

---

#### addBeanContextServicesListener

public void addBeanContextServicesListener​(

BeanContextServicesListener

bcsl)

add a BeanContextServicesListener

removeBeanContextServicesListener

```java
public void removeBeanContextServicesListener​(
BeanContextServicesListener
bcsl)
```

remove a BeanContextServicesListener

**Specified by:** removeBeanContextServicesListener

in interface

BeanContextServices
**Parameters:** bcsl

- the

BeanContextServicesListener

to remove from this context

---

#### removeBeanContextServicesListener

public void removeBeanContextServicesListener​(

BeanContextServicesListener

bcsl)

remove a BeanContextServicesListener

addService

```java
public boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp)
```

add a service

**Specified by:** addService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Returns:** true if the service was successful added, false otherwise

---

#### addService

public boolean addService​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp)

add a service

addService

```java
protected boolean addService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean fireEvent)
```

add a service

**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** fireEvent

- whether or not an event should be fired
**Returns:** true if the service was successfully added

---

#### addService

protected boolean addService​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean fireEvent)

add a service

revokeService

```java
public void revokeService​(
Class
<?> serviceClass,

BeanContextServiceProvider
bcsp,
boolean revokeCurrentServicesNow)
```

remove a service

**Specified by:** revokeService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service class
**Parameters:** bcsp

- the service provider
**Parameters:** revokeCurrentServicesNow

- whether or not to revoke the service

---

#### revokeService

public void revokeService​(

Class

<?> serviceClass,

BeanContextServiceProvider

bcsp,
boolean revokeCurrentServicesNow)

remove a service

hasService

```java
public boolean hasService​(
Class
<?> serviceClass)
```

has a service, which may be delegated

**Specified by:** hasService

in interface

BeanContextServices
**Parameters:** serviceClass

- the service in question
**Returns:** true if the service is available

---

#### hasService

public boolean hasService​(

Class

<?> serviceClass)

has a service, which may be delegated

getService

```java
public
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

obtain a service which may be delegated

**Specified by:** getService

in interface

BeanContextServices
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

public

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

obtain a service which may be delegated

releaseService

```java
public void releaseService​(
BeanContextChild
child,

Object
requestor,

Object
service)
```

release a service

**Specified by:** releaseService

in interface

BeanContextServices
**Parameters:** child

- the

BeanContextChild
**Parameters:** requestor

- the requestor
**Parameters:** service

- the service

---

#### releaseService

public void releaseService​(

BeanContextChild

child,

Object

requestor,

Object

service)

release a service

getCurrentServiceClasses

```java
public
Iterator
<
Object
> getCurrentServiceClasses()
```

Description copied from interface:

BeanContextServices

Gets the currently available services for this context.

**Specified by:** getCurrentServiceClasses

in interface

BeanContextServices
**Returns:** an iterator for all the currently registered service classes.

---

#### getCurrentServiceClasses

public

Iterator

<

Object

> getCurrentServiceClasses()

Description copied from interface:

BeanContextServices

Gets the currently available services for this context.

getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors​(
Class
<?> serviceClass)
```

Description copied from interface:

BeanContextServices

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

**Specified by:** getCurrentServiceSelectors

in interface

BeanContextServices
**Parameters:** serviceClass

- the specified service
**Returns:** an iterator for all the currently available service selectors
(if any) available for the specified service.

---

#### getCurrentServiceSelectors

public

Iterator

<?> getCurrentServiceSelectors​(

Class

<?> serviceClass)

Description copied from interface:

BeanContextServices

Gets the list of service dependent service parameters
(Service Selectors) for the specified service, by
calling getCurrentServiceSelectors() on the
underlying BeanContextServiceProvider.

serviceAvailable

```java
public void serviceAvailable​(
BeanContextServiceAvailableEvent
bcssae)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceAvailable

in interface

BeanContextServicesListener
**Overrides:** serviceAvailable

in class

BeanContextChildSupport
**Parameters:** bcssae

- The BeanContextServiceAvailableEvent fired as a
result of a service becoming available

---

#### serviceAvailable

public void serviceAvailable​(

BeanContextServiceAvailableEvent

bcssae)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

serviceRevoked

```java
public void serviceRevoked​(
BeanContextServiceRevokedEvent
bcssre)
```

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

**Specified by:** serviceRevoked

in interface

BeanContextServiceRevokedListener
**Overrides:** serviceRevoked

in class

BeanContextChildSupport
**Parameters:** bcssre

- The

BeanContextServiceRevokedEvent

fired as a
result of a service being revoked

---

#### serviceRevoked

public void serviceRevoked​(

BeanContextServiceRevokedEvent

bcssre)

BeanContextServicesListener callback, propagates event to all
currently registered listeners and BeanContextServices children,
if this BeanContextService does not already implement this service
itself.

subclasses may override or envelope this method to implement their
own propagation semantics.

getChildBeanContextServicesListener

```java
protected static final
BeanContextServicesListener
getChildBeanContextServicesListener​(
Object
child)
```

Gets the

BeanContextServicesListener

(if any) of the specified
child.

**Parameters:** child

- the specified child
**Returns:** the BeanContextServicesListener (if any) of the specified child

---

#### getChildBeanContextServicesListener

protected static final

BeanContextServicesListener

getChildBeanContextServicesListener​(

Object

child)

Gets the

BeanContextServicesListener

(if any) of the specified
child.

childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

This subclass uses this hook to immediately revoke any services
being used by this child if it is a BeanContextChild.

subclasses may envelope this method in order to implement their
own child removal side-effects.

**Overrides:** childJustRemovedHook

in class

BeanContextSupport
**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

---

#### childJustRemovedHook

protected void childJustRemovedHook​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

called from superclass child removal operations after a child
has been successfully removed. called with child synchronized.

This subclass uses this hook to immediately revoke any services
being used by this child if it is a BeanContextChild.

subclasses may envelope this method in order to implement their
own child removal side-effects.

releaseBeanContextResources

```java
protected void releaseBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

This method revokes any services obtained from its parent.

subclasses may envelope this method to implement their own semantics.

**Overrides:** releaseBeanContextResources

in class

BeanContextChildSupport

---

#### releaseBeanContextResources

protected void releaseBeanContextResources()

called from setBeanContext to notify a BeanContextChild
to release resources obtained from the nesting BeanContext.

This method revokes any services obtained from its parent.

subclasses may envelope this method to implement their own semantics.

initializeBeanContextResources

```java
protected void initializeBeanContextResources()
```

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

subclasses may envelope this method to implement their own semantics.

**Overrides:** initializeBeanContextResources

in class

BeanContextChildSupport

---

#### initializeBeanContextResources

protected void initializeBeanContextResources()

called from setBeanContext to notify a BeanContextChild
to allocate resources obtained from the nesting BeanContext.

subclasses may envelope this method to implement their own semantics.

fireServiceAdded

```java
protected final void fireServiceAdded​(
Class
<?> serviceClass)
```

Fires a

BeanContextServiceEvent

notifying of a new service.

**Parameters:** serviceClass

- the service class

---

#### fireServiceAdded

protected final void fireServiceAdded​(

Class

<?> serviceClass)

Fires a

BeanContextServiceEvent

notifying of a new service.

fireServiceAdded

```java
protected final void fireServiceAdded​(
BeanContextServiceAvailableEvent
bcssae)
```

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

**Parameters:** bcssae

- the

BeanContextServiceAvailableEvent

---

#### fireServiceAdded

protected final void fireServiceAdded​(

BeanContextServiceAvailableEvent

bcssae)

Fires a

BeanContextServiceAvailableEvent

indicating that a new
service has become available.

fireServiceRevoked

```java
protected final void fireServiceRevoked​(
BeanContextServiceRevokedEvent
bcsre)
```

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

**Parameters:** bcsre

- the

BeanContextServiceRevokedEvent

---

#### fireServiceRevoked

protected final void fireServiceRevoked​(

BeanContextServiceRevokedEvent

bcsre)

Fires a

BeanContextServiceEvent

notifying of a service being revoked.

fireServiceRevoked

```java
protected final void fireServiceRevoked​(
Class
<?> serviceClass,
boolean revokeNow)
```

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

**Parameters:** serviceClass

- the service class
**Parameters:** revokeNow

- whether or not the event should be revoked now

---

#### fireServiceRevoked

protected final void fireServiceRevoked​(

Class

<?> serviceClass,
boolean revokeNow)

Fires a

BeanContextServiceRevokedEvent

indicating that a particular service is
no longer available.

bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called from BeanContextSupport writeObject before it serializes the
children ...

This class will serialize any Serializable BeanContextServiceProviders
herein.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreSerializationHook

in class

BeanContextSupport
**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

---

#### bcsPreSerializationHook

protected void bcsPreSerializationHook​(

ObjectOutputStream

oos)
throws

IOException

called from BeanContextSupport writeObject before it serializes the
children ...

This class will serialize any Serializable BeanContextServiceProviders
herein.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

bcsPreDeserializationHook

```java
protected void bcsPreDeserializationHook​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

called from BeanContextSupport readObject before it deserializes the
children ...

This class will deserialize any Serializable BeanContextServiceProviders
serialized earlier thus making them available to the children when they
deserialized.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

**Overrides:** bcsPreDeserializationHook

in class

BeanContextSupport
**Parameters:** ois

- the

ObjectInputStream

to use during deserialization
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

---

#### bcsPreDeserializationHook

protected void bcsPreDeserializationHook​(

ObjectInputStream

ois)
throws

IOException

,

ClassNotFoundException

called from BeanContextSupport readObject before it deserializes the
children ...

This class will deserialize any Serializable BeanContextServiceProviders
serialized earlier thus making them available to the children when they
deserialized.

subclasses may envelope this method to insert their own serialization
processing that has to occur prior to serialization of the children

---

