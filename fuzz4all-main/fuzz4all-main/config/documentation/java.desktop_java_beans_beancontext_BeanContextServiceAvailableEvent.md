# Class BeanContextServiceAvailableEvent

**Source:** `java.desktop\java\beans\beancontext\BeanContextServiceAvailableEvent.html`

### Class Description

```java
public class
BeanContextServiceAvailableEvent

extends
BeanContextEvent
```

This event type is used by the BeanContextServicesListener in order to
identify the service being registered.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Class
<?> serviceClass

A

Class

reference to the newly available service

---

### Constructor Details

#### public BeanContextServiceAvailableEvent​(
BeanContextServices
bcs,

Class
<?> sc)

Construct a

BeanContextAvailableServiceEvent

.

**Parameters:**
- bcs

- The context in which the service has become available
- sc

- A

Class

reference to the newly available service

---

### Method Details

#### public
BeanContextServices
getSourceAsBeanContextServices()

Gets the source as a reference of type

BeanContextServices

.

**Returns:**
- The context in which the service has become available

---

#### public
Class
<?> getServiceClass()

Gets the service class that is the subject of this notification.

**Returns:**
- A

Class

reference to the newly available service

---

#### public
Iterator
<?> getCurrentServiceSelectors()

Gets the list of service dependent selectors.

**Returns:**
- the current selectors available from the service

---

### Additional Sections

#### Class BeanContextServiceAvailableEvent

java.lang.Object

- java.util.EventObject
- - java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextServiceAvailableEvent

java.util.EventObject

- java.beans.beancontext.BeanContextEvent
- - java.beans.beancontext.BeanContextServiceAvailableEvent

java.beans.beancontext.BeanContextEvent

- java.beans.beancontext.BeanContextServiceAvailableEvent

java.beans.beancontext.BeanContextServiceAvailableEvent

**All Implemented Interfaces:** Serializable

```java
public class
BeanContextServiceAvailableEvent

extends
BeanContextEvent
```

This event type is used by the BeanContextServicesListener in order to
identify the service being registered.

**See Also:** Serialized Form

public class

BeanContextServiceAvailableEvent

extends

BeanContextEvent

This event type is used by the BeanContextServicesListener in order to
identify the service being registered.

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

reference to the newly available service

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

BeanContextServiceAvailableEvent

​(

BeanContextServices

bcs,

Class

<?> sc)

Construct a

BeanContextAvailableServiceEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Iterator

<?>

getCurrentServiceSelectors

()

Gets the list of service dependent selectors.

Class

<?>

getServiceClass

()

Gets the service class that is the subject of this notification.

BeanContextServices

getSourceAsBeanContextServices

()

Gets the source as a reference of type

BeanContextServices

.

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

reference to the newly available service

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

reference to the newly available service

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

BeanContextServiceAvailableEvent

​(

BeanContextServices

bcs,

Class

<?> sc)

Construct a

BeanContextAvailableServiceEvent

.

---

#### Constructor Summary

Construct a

BeanContextAvailableServiceEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Iterator

<?>

getCurrentServiceSelectors

()

Gets the list of service dependent selectors.

Class

<?>

getServiceClass

()

Gets the service class that is the subject of this notification.

BeanContextServices

getSourceAsBeanContextServices

()

Gets the source as a reference of type

BeanContextServices

.

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

Gets the list of service dependent selectors.

Gets the service class that is the subject of this notification.

Gets the source as a reference of type

BeanContextServices

.

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

reference to the newly available service

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextServiceAvailableEvent

```java
public BeanContextServiceAvailableEvent​(
BeanContextServices
bcs,

Class
<?> sc)
```

Construct a

BeanContextAvailableServiceEvent

.

**Parameters:** bcs

- The context in which the service has become available
**Parameters:** sc

- A

Class

reference to the newly available service

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

.

**Returns:** The context in which the service has become available

- getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification.

**Returns:** A

Class

reference to the newly available service

- getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors()
```

Gets the list of service dependent selectors.

**Returns:** the current selectors available from the service

Field Detail

- serviceClass

```java
protected
Class
<?> serviceClass
```

A

Class

reference to the newly available service

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

reference to the newly available service

---

#### serviceClass

protected

Class

<?> serviceClass

A

Class

reference to the newly available service

Constructor Detail

- BeanContextServiceAvailableEvent

```java
public BeanContextServiceAvailableEvent​(
BeanContextServices
bcs,

Class
<?> sc)
```

Construct a

BeanContextAvailableServiceEvent

.

**Parameters:** bcs

- The context in which the service has become available
**Parameters:** sc

- A

Class

reference to the newly available service

---

#### Constructor Detail

BeanContextServiceAvailableEvent

```java
public BeanContextServiceAvailableEvent​(
BeanContextServices
bcs,

Class
<?> sc)
```

Construct a

BeanContextAvailableServiceEvent

.

**Parameters:** bcs

- The context in which the service has become available
**Parameters:** sc

- A

Class

reference to the newly available service

---

#### BeanContextServiceAvailableEvent

public BeanContextServiceAvailableEvent​(

BeanContextServices

bcs,

Class

<?> sc)

Construct a

BeanContextAvailableServiceEvent

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

.

**Returns:** The context in which the service has become available

- getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification.

**Returns:** A

Class

reference to the newly available service

- getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors()
```

Gets the list of service dependent selectors.

**Returns:** the current selectors available from the service

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

.

**Returns:** The context in which the service has become available

---

#### getSourceAsBeanContextServices

public

BeanContextServices

getSourceAsBeanContextServices()

Gets the source as a reference of type

BeanContextServices

.

getServiceClass

```java
public
Class
<?> getServiceClass()
```

Gets the service class that is the subject of this notification.

**Returns:** A

Class

reference to the newly available service

---

#### getServiceClass

public

Class

<?> getServiceClass()

Gets the service class that is the subject of this notification.

getCurrentServiceSelectors

```java
public
Iterator
<?> getCurrentServiceSelectors()
```

Gets the list of service dependent selectors.

**Returns:** the current selectors available from the service

---

#### getCurrentServiceSelectors

public

Iterator

<?> getCurrentServiceSelectors()

Gets the list of service dependent selectors.

---

