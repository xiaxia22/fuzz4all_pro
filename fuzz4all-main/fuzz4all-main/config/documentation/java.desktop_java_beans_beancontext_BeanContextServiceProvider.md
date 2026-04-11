# Interface BeanContextServiceProvider

**Source:** `java.desktop\java\beans\beancontext\BeanContextServiceProvider.html`

### Class Description

```java
public interface
BeanContextServiceProvider
```

One of the primary functions of a BeanContext is to act a as rendezvous
between JavaBeans, and BeanContextServiceProviders.

A JavaBean nested within a BeanContext, may ask that BeanContext to
provide an instance of a "service", based upon a reference to a Java
Class object that represents that service.

If such a service has been registered with the context, or one of its
nesting context's, in the case where a context delegate to its context
to satisfy a service request, then the BeanContextServiceProvider associated with
the service is asked to provide an instance of that service.

The ServcieProvider may always return the same instance, or it may
construct a new instance for each request.

**All Known Implementing Classes:** BeanContextServicesSupport.BCSSProxyServiceProvider

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getService​(
BeanContextServices
bcs,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector)

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

**Parameters:**
- bcs

- The

BeanContextServices

associated with this
particular request. This parameter enables the

BeanContextServiceProvider

to distinguish service
requests from multiple sources.
- requestor

- The object requesting the service
- serviceClass

- The service requested
- serviceSelector

- the service dependent parameter
for a particular service, or

null

if not applicable.

**Returns:**
- a reference to the requested service

---

#### void releaseService​(
BeanContextServices
bcs,

Object
requestor,

Object
service)

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

**Parameters:**
- bcs

- the

BeanContextServices

associated with this
particular release request
- requestor

- the object requesting the service to be released
- service

- the service that is to be released

---

#### Iterator
<?> getCurrentServiceSelectors​(
BeanContextServices
bcs,

Class
<?> serviceClass)

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.
A service selector is a service specific parameter,
typical examples of which could include: a
parameter to a constructor for the service implementation class,
a value for a particular service's property, or a key into a
map of existing implementations.

**Parameters:**
- bcs

- the

BeanContextServices

for this request
- serviceClass

- the specified service

**Returns:**
- the current service selectors for the specified serviceClass

---

### Additional Sections

#### Interface BeanContextServiceProvider

**All Known Implementing Classes:** BeanContextServicesSupport.BCSSProxyServiceProvider

```java
public interface
BeanContextServiceProvider
```

One of the primary functions of a BeanContext is to act a as rendezvous
between JavaBeans, and BeanContextServiceProviders.

A JavaBean nested within a BeanContext, may ask that BeanContext to
provide an instance of a "service", based upon a reference to a Java
Class object that represents that service.

If such a service has been registered with the context, or one of its
nesting context's, in the case where a context delegate to its context
to satisfy a service request, then the BeanContextServiceProvider associated with
the service is asked to provide an instance of that service.

The ServcieProvider may always return the same instance, or it may
construct a new instance for each request.

public interface

BeanContextServiceProvider

One of the primary functions of a BeanContext is to act a as rendezvous
between JavaBeans, and BeanContextServiceProviders.

A JavaBean nested within a BeanContext, may ask that BeanContext to
provide an instance of a "service", based upon a reference to a Java
Class object that represents that service.

If such a service has been registered with the context, or one of its
nesting context's, in the case where a context delegate to its context
to satisfy a service request, then the BeanContextServiceProvider associated with
the service is asked to provide an instance of that service.

The ServcieProvider may always return the same instance, or it may
construct a new instance for each request.

One of the primary functions of a BeanContext is to act a as rendezvous
between JavaBeans, and BeanContextServiceProviders.

A JavaBean nested within a BeanContext, may ask that BeanContext to
provide an instance of a "service", based upon a reference to a Java
Class object that represents that service.

If such a service has been registered with the context, or one of its
nesting context's, in the case where a context delegate to its context
to satisfy a service request, then the BeanContextServiceProvider associated with
the service is asked to provide an instance of that service.

The ServcieProvider may always return the same instance, or it may
construct a new instance for each request.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<?>

getCurrentServiceSelectors

​(

BeanContextServices

bcs,

Class

<?> serviceClass)

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.

Object

getService

​(

BeanContextServices

bcs,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector)

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

void

releaseService

​(

BeanContextServices

bcs,

Object

requestor,

Object

service)

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<?>

getCurrentServiceSelectors

​(

BeanContextServices

bcs,

Class

<?> serviceClass)

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.

Object

getService

​(

BeanContextServices

bcs,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector)

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

void

releaseService

​(

BeanContextServices

bcs,

Object

requestor,

Object

service)

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

---

#### Method Summary

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

============ METHOD DETAIL ==========

- Method Detail

- getService

```java
Object
getService​(
BeanContextServices
bcs,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector)
```

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

**Parameters:** bcs

- The

BeanContextServices

associated with this
particular request. This parameter enables the

BeanContextServiceProvider

to distinguish service
requests from multiple sources.
**Parameters:** requestor

- The object requesting the service
**Parameters:** serviceClass

- The service requested
**Parameters:** serviceSelector

- the service dependent parameter
for a particular service, or

null

if not applicable.
**Returns:** a reference to the requested service

- releaseService

```java
void releaseService​(
BeanContextServices
bcs,

Object
requestor,

Object
service)
```

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

**Parameters:** bcs

- the

BeanContextServices

associated with this
particular release request
**Parameters:** requestor

- the object requesting the service to be released
**Parameters:** service

- the service that is to be released

- getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
BeanContextServices
bcs,

Class
<?> serviceClass)
```

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.
A service selector is a service specific parameter,
typical examples of which could include: a
parameter to a constructor for the service implementation class,
a value for a particular service's property, or a key into a
map of existing implementations.

**Parameters:** bcs

- the

BeanContextServices

for this request
**Parameters:** serviceClass

- the specified service
**Returns:** the current service selectors for the specified serviceClass

Method Detail

- getService

```java
Object
getService​(
BeanContextServices
bcs,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector)
```

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

**Parameters:** bcs

- The

BeanContextServices

associated with this
particular request. This parameter enables the

BeanContextServiceProvider

to distinguish service
requests from multiple sources.
**Parameters:** requestor

- The object requesting the service
**Parameters:** serviceClass

- The service requested
**Parameters:** serviceSelector

- the service dependent parameter
for a particular service, or

null

if not applicable.
**Returns:** a reference to the requested service

- releaseService

```java
void releaseService​(
BeanContextServices
bcs,

Object
requestor,

Object
service)
```

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

**Parameters:** bcs

- the

BeanContextServices

associated with this
particular release request
**Parameters:** requestor

- the object requesting the service to be released
**Parameters:** service

- the service that is to be released

- getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
BeanContextServices
bcs,

Class
<?> serviceClass)
```

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.
A service selector is a service specific parameter,
typical examples of which could include: a
parameter to a constructor for the service implementation class,
a value for a particular service's property, or a key into a
map of existing implementations.

**Parameters:** bcs

- the

BeanContextServices

for this request
**Parameters:** serviceClass

- the specified service
**Returns:** the current service selectors for the specified serviceClass

---

#### Method Detail

getService

```java
Object
getService​(
BeanContextServices
bcs,

Object
requestor,

Class
<?> serviceClass,

Object
serviceSelector)
```

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

**Parameters:** bcs

- The

BeanContextServices

associated with this
particular request. This parameter enables the

BeanContextServiceProvider

to distinguish service
requests from multiple sources.
**Parameters:** requestor

- The object requesting the service
**Parameters:** serviceClass

- The service requested
**Parameters:** serviceSelector

- the service dependent parameter
for a particular service, or

null

if not applicable.
**Returns:** a reference to the requested service

---

#### getService

Object

getService​(

BeanContextServices

bcs,

Object

requestor,

Class

<?> serviceClass,

Object

serviceSelector)

Invoked by

BeanContextServices

, this method
requests an instance of a
service from this

BeanContextServiceProvider

.

releaseService

```java
void releaseService​(
BeanContextServices
bcs,

Object
requestor,

Object
service)
```

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

**Parameters:** bcs

- the

BeanContextServices

associated with this
particular release request
**Parameters:** requestor

- the object requesting the service to be released
**Parameters:** service

- the service that is to be released

---

#### releaseService

void releaseService​(

BeanContextServices

bcs,

Object

requestor,

Object

service)

Invoked by

BeanContextServices

,
this method releases a nested

BeanContextChild

's
(or any arbitrary object associated with a

BeanContextChild

) reference to the specified service.

getCurrentServiceSelectors

```java
Iterator
<?> getCurrentServiceSelectors​(
BeanContextServices
bcs,

Class
<?> serviceClass)
```

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.
A service selector is a service specific parameter,
typical examples of which could include: a
parameter to a constructor for the service implementation class,
a value for a particular service's property, or a key into a
map of existing implementations.

**Parameters:** bcs

- the

BeanContextServices

for this request
**Parameters:** serviceClass

- the specified service
**Returns:** the current service selectors for the specified serviceClass

---

#### getCurrentServiceSelectors

Iterator

<?> getCurrentServiceSelectors​(

BeanContextServices

bcs,

Class

<?> serviceClass)

Invoked by

BeanContextServices

, this method
gets the current service selectors for the specified service.
A service selector is a service specific parameter,
typical examples of which could include: a
parameter to a constructor for the service implementation class,
a value for a particular service's property, or a key into a
map of existing implementations.

---

