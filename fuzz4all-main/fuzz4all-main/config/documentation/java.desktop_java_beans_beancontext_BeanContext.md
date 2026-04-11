# Interface BeanContext

**Source:** `java.desktop\java\beans\beancontext\BeanContext.html`

### Class Description

```java
public interface
BeanContext

extends
BeanContextChild
,
Collection
,
DesignMode
,
Visibility
```

The BeanContext acts a logical hierarchical container for JavaBeans.

**All Superinterfaces:** BeanContextChild

,

Collection

,

DesignMode

,

Iterable

,

Visibility

---

### Field Details

#### static final
Object
globalHierarchyLock

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

---

### Constructor Details

*No entries found.*

### Method Details

#### Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException

Instantiate the javaBean named as a
child of this

BeanContext

.
The implementation of the JavaBean is
derived from the value of the beanName parameter,
and is defined by the

java.beans.Beans.instantiate()

method.

**Parameters:**
- beanName

- The name of the JavaBean to instantiate
as a child of this

BeanContext

**Returns:**
- a javaBean named as a child of this

BeanContext

**Throws:**
- IOException

- if an IO problem occurs
- ClassNotFoundException

- if the class identified
by the beanName parameter is not found

---

#### InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:**
- name

- the resource name
- bcc

- the specified child

**Returns:**
- an

InputStream

for reading the resource,
or

null

if the resource could not
be found.

**Throws:**
- IllegalArgumentException

- if
the resource is not valid

---

#### URL
getResource​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:**
- name

- the resource name
- bcc

- the specified child

**Returns:**
- a

URL

for the named
resource for the specified child

**Throws:**
- IllegalArgumentException

- if the resource is not valid

---

#### void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

**Parameters:**
- bcml

- the BeanContextMembershipListener to be added

---

#### void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

**Parameters:**
- bcml

- the

BeanContextMembershipListener

to be removed

---

### Additional Sections

#### Interface BeanContext

**All Superinterfaces:** BeanContextChild

,

Collection

,

DesignMode

,

Iterable

,

Visibility

**All Known Subinterfaces:** BeanContextServices

**All Known Implementing Classes:** BeanContextServicesSupport

,

BeanContextSupport

```java
public interface
BeanContext

extends
BeanContextChild
,
Collection
,
DesignMode
,
Visibility
```

The BeanContext acts a logical hierarchical container for JavaBeans.

**Since:** 1.2
**See Also:** Beans

,

BeanContextChild

,

BeanContextMembershipListener

,

PropertyChangeEvent

,

DesignMode

,

Visibility

,

Collection

public interface

BeanContext

extends

BeanContextChild

,

Collection

,

DesignMode

,

Visibility

The BeanContext acts a logical hierarchical container for JavaBeans.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Object

globalHierarchyLock

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

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

addBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

URL

getResource

​(

String

name,

BeanContextChild

bcc)

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

InputStream

getResourceAsStream

​(

String

name,

BeanContextChild

bcc)

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

Object

instantiateChild

​(

String

beanName)

Instantiate the javaBean named as a
child of this

BeanContext

.

void

removeBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

Object

globalHierarchyLock

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

- Fields declared in interface java.beans.

DesignMode

PROPERTYNAME

---

#### Field Summary

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

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

addBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

URL

getResource

​(

String

name,

BeanContextChild

bcc)

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

InputStream

getResourceAsStream

​(

String

name,

BeanContextChild

bcc)

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

Object

instantiateChild

​(

String

beanName)

Instantiate the javaBean named as a
child of this

BeanContext

.

void

removeBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

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

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

Instantiate the javaBean named as a
child of this

BeanContext

.

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

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

- globalHierarchyLock

```java
static final
Object
globalHierarchyLock
```

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

============ METHOD DETAIL ==========

- Method Detail

- instantiateChild

```java
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

Instantiate the javaBean named as a
child of this

BeanContext

.
The implementation of the JavaBean is
derived from the value of the beanName parameter,
and is defined by the

java.beans.Beans.instantiate()

method.

**Parameters:** beanName

- The name of the JavaBean to instantiate
as a child of this

BeanContext
**Returns:** a javaBean named as a child of this

BeanContext
**Throws:** IOException

- if an IO problem occurs
**Throws:** ClassNotFoundException

- if the class identified
by the beanName parameter is not found

- getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** an

InputStream

for reading the resource,
or

null

if the resource could not
be found.
**Throws:** IllegalArgumentException

- if
the resource is not valid

- getResource

```java
URL
getResource​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** a

URL

for the named
resource for the specified child
**Throws:** IllegalArgumentException

- if the resource is not valid

- addBeanContextMembershipListener

```java
void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

**Parameters:** bcml

- the BeanContextMembershipListener to be added

- removeBeanContextMembershipListener

```java
void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

**Parameters:** bcml

- the

BeanContextMembershipListener

to be removed

Field Detail

- globalHierarchyLock

```java
static final
Object
globalHierarchyLock
```

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

---

#### Field Detail

globalHierarchyLock

```java
static final
Object
globalHierarchyLock
```

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

---

#### globalHierarchyLock

static final

Object

globalHierarchyLock

This global lock is used by both

BeanContext

and

BeanContextServices

implementors
to serialize changes in a

BeanContext

hierarchy and any service requests etc.

Method Detail

- instantiateChild

```java
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

Instantiate the javaBean named as a
child of this

BeanContext

.
The implementation of the JavaBean is
derived from the value of the beanName parameter,
and is defined by the

java.beans.Beans.instantiate()

method.

**Parameters:** beanName

- The name of the JavaBean to instantiate
as a child of this

BeanContext
**Returns:** a javaBean named as a child of this

BeanContext
**Throws:** IOException

- if an IO problem occurs
**Throws:** ClassNotFoundException

- if the class identified
by the beanName parameter is not found

- getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** an

InputStream

for reading the resource,
or

null

if the resource could not
be found.
**Throws:** IllegalArgumentException

- if
the resource is not valid

- getResource

```java
URL
getResource​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** a

URL

for the named
resource for the specified child
**Throws:** IllegalArgumentException

- if the resource is not valid

- addBeanContextMembershipListener

```java
void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

**Parameters:** bcml

- the BeanContextMembershipListener to be added

- removeBeanContextMembershipListener

```java
void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

**Parameters:** bcml

- the

BeanContextMembershipListener

to be removed

---

#### Method Detail

instantiateChild

```java
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

Instantiate the javaBean named as a
child of this

BeanContext

.
The implementation of the JavaBean is
derived from the value of the beanName parameter,
and is defined by the

java.beans.Beans.instantiate()

method.

**Parameters:** beanName

- The name of the JavaBean to instantiate
as a child of this

BeanContext
**Returns:** a javaBean named as a child of this

BeanContext
**Throws:** IOException

- if an IO problem occurs
**Throws:** ClassNotFoundException

- if the class identified
by the beanName parameter is not found

---

#### instantiateChild

Object

instantiateChild​(

String

beanName)
throws

IOException

,

ClassNotFoundException

Instantiate the javaBean named as a
child of this

BeanContext

.
The implementation of the JavaBean is
derived from the value of the beanName parameter,
and is defined by the

java.beans.Beans.instantiate()

method.

getResourceAsStream

```java
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** an

InputStream

for reading the resource,
or

null

if the resource could not
be found.
**Throws:** IllegalArgumentException

- if
the resource is not valid

---

#### getResourceAsStream

InputStream

getResourceAsStream​(

String

name,

BeanContextChild

bcc)
throws

IllegalArgumentException

Analagous to

java.lang.ClassLoader.getResourceAsStream()

,
this method allows a

BeanContext

implementation
to interpose behavior between the child

Component

and underlying

ClassLoader

.

getResource

```java
URL
getResource​(
String
name,

BeanContextChild
bcc)
throws
IllegalArgumentException
```

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

**Parameters:** name

- the resource name
**Parameters:** bcc

- the specified child
**Returns:** a

URL

for the named
resource for the specified child
**Throws:** IllegalArgumentException

- if the resource is not valid

---

#### getResource

URL

getResource​(

String

name,

BeanContextChild

bcc)
throws

IllegalArgumentException

Analagous to

java.lang.ClassLoader.getResource()

, this
method allows a

BeanContext

implementation to interpose
behavior between the child

Component

and underlying

ClassLoader

.

addBeanContextMembershipListener

```java
void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

**Parameters:** bcml

- the BeanContextMembershipListener to be added

---

#### addBeanContextMembershipListener

void addBeanContextMembershipListener​(

BeanContextMembershipListener

bcml)

Adds the specified

BeanContextMembershipListener

to receive

BeanContextMembershipEvents

from
this

BeanContext

whenever it adds
or removes a child

Component

(s).

removeBeanContextMembershipListener

```java
void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

**Parameters:** bcml

- the

BeanContextMembershipListener

to be removed

---

#### removeBeanContextMembershipListener

void removeBeanContextMembershipListener​(

BeanContextMembershipListener

bcml)

Removes the specified

BeanContextMembershipListener

so that it no longer receives

BeanContextMembershipEvent

s
when the child

Component

(s) are added or removed.

---

