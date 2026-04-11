# Class BeanContextSupport

**Source:** `java.desktop\java\beans\beancontext\BeanContextSupport.html`

### Class Description

```java
public class
BeanContextSupport

extends
BeanContextChildSupport

implements
BeanContext
,
Serializable
,
PropertyChangeListener
,
VetoableChangeListener
```

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContext interface.

Since this class directly implements the BeanContext interface, the class
can, and is intended to be used either by subclassing this implementation,
or via ad-hoc delegation of an instance of this class from another.

**All Implemented Interfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

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
BeanContextSupport.BCSChild
> children

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

---

#### protected transient
ArrayList
<
BeanContextMembershipListener
> bcmListeners

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

---

#### protected
Locale
locale

The current locale of this BeanContext.

---

#### protected boolean okToUseGui

A

boolean

indicating if this
instance may now render a GUI.

---

#### protected boolean designTime

A

boolean

indicating whether or not
this object is currently in design time mode.

---

### Constructor Details

#### public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dTime,
boolean visible)

Construct a BeanContextSupport instance

**Parameters:**
- peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object is its own peer
- lcle

- The current Locale for this BeanContext. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
- dTime

- The initial state,

true

if in design mode,

false

if runtime.
- visible

- The initial visibility.

**See Also:**
- Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

**Parameters:**
- peer

- The peer

BeanContext

we
are supplying an implementation for,
or

null

if this object is its own peer
- lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
- dtime

- The initial state,

true

if in design mode,

false

if runtime.

**See Also:**
- Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### public BeanContextSupport​(
BeanContext
peer,

Locale
lcle)

Create an instance using the specified locale

**Parameters:**
- peer

- The peer BeanContext we are
supplying an implementation for,
or

null

if this object
is its own peer
- lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

,
the default locale
is assigned to the

BeanContext

instance.

**See Also:**
- Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### public BeanContextSupport​(
BeanContext
peer)

Create an instance using with a default locale

**Parameters:**
- peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object
is its own peer

---

#### public BeanContextSupport()

Create an instance that is not a delegate of another object

---

### Method Details

#### public
BeanContext
getBeanContextPeer()

Gets the instance of

BeanContext

that
this object is providing the implementation for.

**Returns:**
- the BeanContext instance

---

#### public
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

**Specified by:**
- instantiateChild

in interface

BeanContext

**Parameters:**
- beanName

- the name of the Bean to instantiate within this BeanContext

**Returns:**
- the new object

**Throws:**
- IOException

- if there is an I/O error when the bean is being deserialized
- ClassNotFoundException

- if the class
identified by the beanName parameter is not found

---

#### public int size()

Gets the number of children currently nested in
this BeanContext.

**Specified by:**
- size

in interface

Collection

**Returns:**
- number of children

---

#### public boolean isEmpty()

Reports whether or not this

BeanContext

is empty.
A

BeanContext

is considered
empty when it contains zero
nested children.

**Specified by:**
- isEmpty

in interface

Collection

**Returns:**
- if there are not children

---

#### public boolean contains​(
Object
o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Specified by:**
- contains

in interface

Collection

**Parameters:**
- o

- the Object in question

**Returns:**
- if this object is a child

---

#### public boolean containsKey​(
Object
o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Parameters:**
- o

- the Object in question

**Returns:**
- if this object is a child

---

#### public
Iterator
<
Object
> iterator()

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

**Specified by:**
- iterator

in interface

Collection
- iterator

in interface

Iterable

**Returns:**
- an

Iterator

of the nested children

---

#### public
Object
[] toArray()

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

**Specified by:**
- toArray

in interface

Collection

**Returns:**
- an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

---

#### public
Object
[] toArray​(
Object
[] arry)

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

**Specified by:**
- toArray

in interface

Collection

**Parameters:**
- arry

- The array of object
types that are of interest.

**Returns:**
- an array of children

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

**Parameters:**
- targetChild

- the child to create the Child on behalf of
- peer

- the peer if the tragetChild and the peer are related by an implementation of BeanContextProxy

**Returns:**
- Subtype-specific subclass of Child without overriding collection methods

---

#### public boolean add​(
Object
targetChild)

Adds/nests a child within this

BeanContext

.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

**Specified by:**
- add

in interface

Collection

**Parameters:**
- targetChild

- The child objects to nest
within this

BeanContext

**Returns:**
- true if the child was added successfully.

**See Also:**
- validatePendingAdd(java.lang.Object)

---

#### public boolean remove​(
Object
targetChild)

Removes a child from this BeanContext. If the child object is not
for adding then this method throws an IllegalStateException.

**Specified by:**
- remove

in interface

Collection

**Parameters:**
- targetChild

- The child objects to remove

**Returns:**
- true

if an element was removed as a result of this call

**See Also:**
- validatePendingRemove(java.lang.Object)

---

#### protected boolean remove​(
Object
targetChild,
boolean callChildSetBC)

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

**Parameters:**
- targetChild

- the JavaBean, BeanContext, or Object to be removed
- callChildSetBC

- used to indicate that
the child should be notified that it is no
longer nested in this

BeanContext

.

**Returns:**
- whether or not was present before being removed

---

#### public boolean containsAll​(
Collection
c)

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

**Specified by:**
- containsAll

in interface

Collection

**Parameters:**
- c

- the specified

Collection

**Returns:**
- true

if all objects
in the collection are children of
this

BeanContext

, false if not.

**See Also:**
- Collection.contains(Object)

---

#### public boolean addAll​(
Collection
c)

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:**
- addAll

in interface

Collection

**Parameters:**
- c

- collection containing elements to be added to this collection

**Returns:**
- this implementation unconditionally throws

UnsupportedOperationException

**Throws:**
- UnsupportedOperationException

- thrown unconditionally by this implementation

**See Also:**
- Collection.add(Object)

---

#### public boolean removeAll​(
Collection
c)

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:**
- removeAll

in interface

Collection

**Parameters:**
- c

- collection containing elements to be removed from this collection

**Returns:**
- this implementation unconditionally throws

UnsupportedOperationException

**Throws:**
- UnsupportedOperationException

- thrown unconditionally by this implementation

**See Also:**
- Collection.remove(Object)

,

Collection.contains(Object)

---

#### public boolean retainAll​(
Collection
c)

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:**
- retainAll

in interface

Collection

**Parameters:**
- c

- collection containing elements to be retained in this collection

**Returns:**
- this implementation unconditionally throws

UnsupportedOperationException

**Throws:**
- UnsupportedOperationException

- thrown unconditionally by this implementation

**See Also:**
- Collection.remove(Object)

,

Collection.contains(Object)

---

#### public void clear()

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:**
- clear

in interface

Collection

**Throws:**
- UnsupportedOperationException

- thrown unconditionally by this implementation

---

#### public void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)

Adds a BeanContextMembershipListener

**Specified by:**
- addBeanContextMembershipListener

in interface

BeanContext

**Parameters:**
- bcml

- the BeanContextMembershipListener to add

**Throws:**
- NullPointerException

- if the argument is null

---

#### public void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)

Removes a BeanContextMembershipListener

**Specified by:**
- removeBeanContextMembershipListener

in interface

BeanContext

**Parameters:**
- bcml

- the BeanContextMembershipListener to remove

**Throws:**
- NullPointerException

- if the argument is null

---

#### public
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)

Description copied from interface:

BeanContext

**Specified by:**
- getResourceAsStream

in interface

BeanContext

**Parameters:**
- name

- the name of the resource requested.
- bcc

- the child object making the request.

**Returns:**
- the requested resource as an InputStream

**Throws:**
- NullPointerException

- if the argument is null

---

#### public
URL
getResource​(
String
name,

BeanContextChild
bcc)

Description copied from interface:

BeanContext

**Specified by:**
- getResource

in interface

BeanContext

**Parameters:**
- name

- the name of the resource requested.
- bcc

- the child object making the request.

**Returns:**
- the requested resource as an InputStream

---

#### public void setDesignTime​(boolean dTime)

Sets the new design time value for this

BeanContext

.

**Specified by:**
- setDesignTime

in interface

DesignMode

**Parameters:**
- dTime

- the new designTime value

**See Also:**
- BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

---

#### public boolean isDesignTime()

Reports whether or not this object is in
currently in design time mode.

**Specified by:**
- isDesignTime

in interface

DesignMode

**Returns:**
- true

if in design time mode,

false

if not

---

#### public void setLocale​(
Locale
newLocale)
throws
PropertyVetoException

Sets the locale of this BeanContext.

**Parameters:**
- newLocale

- the new locale. This method call will have
no effect if newLocale is

null

.

**Throws:**
- PropertyVetoException

- if the new value is rejected

---

#### public
Locale
getLocale()

Gets the locale for this

BeanContext

.

**Returns:**
- the current Locale of the

BeanContext

---

#### public boolean needsGui()

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

**Specified by:**
- needsGui

in interface

Visibility

**Returns:**
- true

if the implementor needs a GUI

---

#### public void dontUseGui()

notify this instance that it may no longer render a GUI.

**Specified by:**
- dontUseGui

in interface

Visibility

---

#### public void okToUseGui()

Notify this instance that it may now render a GUI

**Specified by:**
- okToUseGui

in interface

Visibility

---

#### public boolean avoidingGui()

Used to determine if the

BeanContext

child is avoiding using its GUI.

**Specified by:**
- avoidingGui

in interface

Visibility

**Returns:**
- is this instance avoiding using its GUI?

**See Also:**
- Visibility

---

#### public boolean isSerializing()

Is this

BeanContext

in the
process of being serialized?

**Returns:**
- if this

BeanContext

is
currently being serialized

---

#### protected
Iterator
<
BeanContextSupport.BCSChild
> bcsChildren()

Returns an iterator of all children
of this

BeanContext

.

**Returns:**
- an iterator for all the current BCSChild values

---

#### protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

This method may be overridden by subclasses to perform custom
serialization of their state prior to this superclass serializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of writeObject().

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

called by readObject after defaultReadObject() but prior to
deserialization of any children.

This method may be overridden by subclasses to perform custom
deserialization of their state prior to this superclass deserializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of readObject().

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

#### protected void childDeserializedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)

Called by readObject with the newly deserialized child and BCSChild.

**Parameters:**
- child

- the newly deserialized child
- bcsc

- the newly deserialized BCSChild

---

#### protected final void serialize​(
ObjectOutputStream
oos,

Collection
<?> coll)
throws
IOException

Used by writeObject to serialize a Collection.

**Parameters:**
- oos

- the

ObjectOutputStream

to use during serialization
- coll

- the

Collection

to serialize

**Throws:**
- IOException

- if serialization failed

---

#### protected final void deserialize​(
ObjectInputStream
ois,

Collection
coll)
throws
IOException
,

ClassNotFoundException

used by readObject to deserialize a collection.

**Parameters:**
- ois

- the ObjectInputStream to use
- coll

- the Collection

**Throws:**
- IOException

- if deserialization failed
- ClassNotFoundException

- if needed classes are not found

---

#### public final void writeChildren​(
ObjectOutputStream
oos)
throws
IOException

Used to serialize all children of
this

BeanContext

.

**Parameters:**
- oos

- the

ObjectOutputStream

to use during serialization

**Throws:**
- IOException

- if serialization failed

---

#### public final void readChildren​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

**Parameters:**
- ois

- the ObjectInputStream to use

**Throws:**
- IOException

- if deserialization failed
- ClassNotFoundException

- if needed classes are not found

---

#### public void vetoableChange​(
PropertyChangeEvent
pce)
throws
PropertyVetoException

subclasses may envelope to monitor veto child property changes.

**Specified by:**
- vetoableChange

in interface

VetoableChangeListener

**Parameters:**
- pce

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.

**Throws:**
- PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

---

#### public void propertyChange​(
PropertyChangeEvent
pce)

subclasses may envelope to monitor child property changes.

**Specified by:**
- propertyChange

in interface

PropertyChangeListener

**Parameters:**
- pce

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

#### protected boolean validatePendingAdd​(
Object
targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

**Parameters:**
- targetChild

- the child to create the Child on behalf of

**Returns:**
- true iff the child may be added to this BeanContext, otherwise false.

---

#### protected boolean validatePendingRemove​(
Object
targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

**Parameters:**
- targetChild

- the child to create the Child on behalf of

**Returns:**
- true iff the child may be removed from this BeanContext, otherwise false.

---

#### protected void childJustAddedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:**
- child

- the child
- bcsc

- the BCSChild

---

#### protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:**
- child

- the child
- bcsc

- the BCSChild

---

#### protected static final
Visibility
getChildVisibility​(
Object
child)

Gets the Component (if any) associated with the specified child.

**Parameters:**
- child

- the specified child

**Returns:**
- the Component (if any) associated with the specified child.

---

#### protected static final
Serializable
getChildSerializable​(
Object
child)

Gets the Serializable (if any) associated with the specified Child

**Parameters:**
- child

- the specified child

**Returns:**
- the Serializable (if any) associated with the specified Child

---

#### protected static final
PropertyChangeListener
getChildPropertyChangeListener​(
Object
child)

Gets the PropertyChangeListener
(if any) of the specified child

**Parameters:**
- child

- the specified child

**Returns:**
- the PropertyChangeListener (if any) of the specified child

---

#### protected static final
VetoableChangeListener
getChildVetoableChangeListener​(
Object
child)

Gets the VetoableChangeListener
(if any) of the specified child

**Parameters:**
- child

- the specified child

**Returns:**
- the VetoableChangeListener (if any) of the specified child

---

#### protected static final
BeanContextMembershipListener
getChildBeanContextMembershipListener​(
Object
child)

Gets the BeanContextMembershipListener
(if any) of the specified child

**Parameters:**
- child

- the specified child

**Returns:**
- the BeanContextMembershipListener (if any) of the specified child

---

#### protected static final
BeanContextChild
getChildBeanContextChild​(
Object
child)

Gets the BeanContextChild (if any) of the specified child

**Parameters:**
- child

- the specified child

**Returns:**
- the BeanContextChild (if any) of the specified child

**Throws:**
- IllegalArgumentException

- if child implements both BeanContextChild and BeanContextProxy

---

#### protected final void fireChildrenAdded​(
BeanContextMembershipEvent
bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:**
- bcme

- the event to fire

---

#### protected final void fireChildrenRemoved​(
BeanContextMembershipEvent
bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:**
- bcme

- the event to fire

---

#### protected void initialize()

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

This class uses this method to instantiate inner class listeners used
to monitor PropertyChange and VetoableChange events on children.

subclasses may envelope this method to add their own initialization
behavior

---

#### protected final
Object
[] copyChildren()

Gets a copy of the this BeanContext's children.

**Returns:**
- a copy of the current nested children

---

#### protected static final boolean classEquals​(
Class
<?> first,

Class
<?> second)

Tests to see if two class objects,
or their names are equal.

**Parameters:**
- first

- the first object
- second

- the second object

**Returns:**
- true if equal, false if not

---

### Additional Sections

#### Class BeanContextSupport

java.lang.Object

- java.beans.beancontext.BeanContextChildSupport
- - java.beans.beancontext.BeanContextSupport

java.beans.beancontext.BeanContextChildSupport

- java.beans.beancontext.BeanContextSupport

java.beans.beancontext.BeanContextSupport

**All Implemented Interfaces:** BeanContext

,

BeanContextChild

,

BeanContextServiceRevokedListener

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

**Direct Known Subclasses:** BeanContextServicesSupport

```java
public class
BeanContextSupport

extends
BeanContextChildSupport

implements
BeanContext
,
Serializable
,
PropertyChangeListener
,
VetoableChangeListener
```

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContext interface.

Since this class directly implements the BeanContext interface, the class
can, and is intended to be used either by subclassing this implementation,
or via ad-hoc delegation of an instance of this class from another.

**Since:** 1.2
**See Also:** Serialized Form

public class

BeanContextSupport

extends

BeanContextChildSupport

implements

BeanContext

,

Serializable

,

PropertyChangeListener

,

VetoableChangeListener

This helper class provides a utility implementation of the
java.beans.beancontext.BeanContext interface.

Since this class directly implements the BeanContext interface, the class
can, and is intended to be used either by subclassing this implementation,
or via ad-hoc delegation of an instance of this class from another.

Since this class directly implements the BeanContext interface, the class
can, and is intended to be used either by subclassing this implementation,
or via ad-hoc delegation of an instance of this class from another.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BeanContextSupport.BCSChild

protected static class

BeanContextSupport.BCSIterator

protected final subclass that encapsulates an iterator but implements
a noop remove() method.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ArrayList

<

BeanContextMembershipListener

>

bcmListeners

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

protected

HashMap

<

Object

,​

BeanContextSupport.BCSChild

>

children

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

protected boolean

designTime

A

boolean

indicating whether or not
this object is currently in design time mode.

protected

Locale

locale

The current locale of this BeanContext.

protected boolean

okToUseGui

A

boolean

indicating if this
instance may now render a GUI.

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

BeanContextSupport

()

Create an instance that is not a delegate of another object

BeanContextSupport

​(

BeanContext

peer)

Create an instance using with a default locale

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextSupport instance

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Object

targetChild)

Adds/nests a child within this

BeanContext

.

boolean

addAll

​(

Collection

c)

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

void

addBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Adds a BeanContextMembershipListener

boolean

avoidingGui

()

Used to determine if the

BeanContext

child is avoiding using its GUI.

protected

Iterator

<

BeanContextSupport.BCSChild

>

bcsChildren

()

Returns an iterator of all children
of this

BeanContext

.

protected void

bcsPreDeserializationHook

​(

ObjectInputStream

ois)

called by readObject after defaultReadObject() but prior to
deserialization of any children.

protected void

bcsPreSerializationHook

​(

ObjectOutputStream

oos)

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

protected void

childDeserializedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

Called by readObject with the newly deserialized child and BCSChild.

protected void

childJustAddedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred.

protected void

childJustRemovedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred.

protected static boolean

classEquals

​(

Class

<?> first,

Class

<?> second)

Tests to see if two class objects,
or their names are equal.

void

clear

()

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

boolean

contains

​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

boolean

containsAll

​(

Collection

c)

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

boolean

containsKey

​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

protected

Object

[]

copyChildren

()

Gets a copy of the this BeanContext's children.

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

protected void

deserialize

​(

ObjectInputStream

ois,

Collection

coll)

used by readObject to deserialize a collection.

void

dontUseGui

()

notify this instance that it may no longer render a GUI.

protected void

fireChildrenAdded

​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

protected void

fireChildrenRemoved

​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

BeanContext

getBeanContextPeer

()

Gets the instance of

BeanContext

that
this object is providing the implementation for.

protected static

BeanContextChild

getChildBeanContextChild

​(

Object

child)

Gets the BeanContextChild (if any) of the specified child

protected static

BeanContextMembershipListener

getChildBeanContextMembershipListener

​(

Object

child)

Gets the BeanContextMembershipListener
(if any) of the specified child

protected static

PropertyChangeListener

getChildPropertyChangeListener

​(

Object

child)

Gets the PropertyChangeListener
(if any) of the specified child

protected static

Serializable

getChildSerializable

​(

Object

child)

Gets the Serializable (if any) associated with the specified Child

protected static

VetoableChangeListener

getChildVetoableChangeListener

​(

Object

child)

Gets the VetoableChangeListener
(if any) of the specified child

protected static

Visibility

getChildVisibility

​(

Object

child)

Gets the Component (if any) associated with the specified child.

Locale

getLocale

()

Gets the locale for this

BeanContext

.

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

protected void

initialize

()

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

Object

instantiateChild

​(

String

beanName)

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

boolean

isDesignTime

()

Reports whether or not this object is in
currently in design time mode.

boolean

isEmpty

()

Reports whether or not this

BeanContext

is empty.

boolean

isSerializing

()

Is this

BeanContext

in the
process of being serialized?

Iterator

<

Object

>

iterator

()

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

boolean

needsGui

()

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

void

okToUseGui

()

Notify this instance that it may now render a GUI

void

propertyChange

​(

PropertyChangeEvent

pce)

subclasses may envelope to monitor child property changes.

void

readChildren

​(

ObjectInputStream

ois)

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

boolean

remove

​(

Object

targetChild)

Removes a child from this BeanContext.

protected boolean

remove

​(

Object

targetChild,
boolean callChildSetBC)

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

boolean

removeAll

​(

Collection

c)

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

void

removeBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Removes a BeanContextMembershipListener

boolean

retainAll

​(

Collection

c)

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

protected void

serialize

​(

ObjectOutputStream

oos,

Collection

<?> coll)

Used by writeObject to serialize a Collection.

void

setDesignTime

​(boolean dTime)

Sets the new design time value for this

BeanContext

.

void

setLocale

​(

Locale

newLocale)

Sets the locale of this BeanContext.

int

size

()

Gets the number of children currently nested in
this BeanContext.

Object

[]

toArray

()

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

Object

[]

toArray

​(

Object

[] arry)

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

protected boolean

validatePendingAdd

​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

protected boolean

validatePendingRemove

​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

void

vetoableChange

​(

PropertyChangeEvent

pce)

subclasses may envelope to monitor veto child property changes.

void

writeChildren

​(

ObjectOutputStream

oos)

Used to serialize all children of
this

BeanContext

.

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

initializeBeanContextResources

,

isDelegated

,

releaseBeanContextResources

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

serviceAvailable

,

serviceRevoked

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

equals

,

hashCode

,

parallelStream

,

removeIf

,

spliterator

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BeanContextSupport.BCSChild

protected static class

BeanContextSupport.BCSIterator

protected final subclass that encapsulates an iterator but implements
a noop remove() method.

---

#### Nested Class Summary

protected final subclass that encapsulates an iterator but implements
a noop remove() method.

Field Summary

Fields

Modifier and Type

Field

Description

protected

ArrayList

<

BeanContextMembershipListener

>

bcmListeners

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

protected

HashMap

<

Object

,​

BeanContextSupport.BCSChild

>

children

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

protected boolean

designTime

A

boolean

indicating whether or not
this object is currently in design time mode.

protected

Locale

locale

The current locale of this BeanContext.

protected boolean

okToUseGui

A

boolean

indicating if this
instance may now render a GUI.

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

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

A

boolean

indicating whether or not
this object is currently in design time mode.

The current locale of this BeanContext.

A

boolean

indicating if this
instance may now render a GUI.

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

BeanContextSupport

()

Create an instance that is not a delegate of another object

BeanContextSupport

​(

BeanContext

peer)

Create an instance using with a default locale

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextSupport

​(

BeanContext

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextSupport instance

---

#### Constructor Summary

Create an instance that is not a delegate of another object

Create an instance using with a default locale

Create an instance using the specified locale

Create an instance using the specified Locale and design mode.

Construct a BeanContextSupport instance

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

Object

targetChild)

Adds/nests a child within this

BeanContext

.

boolean

addAll

​(

Collection

c)

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

void

addBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Adds a BeanContextMembershipListener

boolean

avoidingGui

()

Used to determine if the

BeanContext

child is avoiding using its GUI.

protected

Iterator

<

BeanContextSupport.BCSChild

>

bcsChildren

()

Returns an iterator of all children
of this

BeanContext

.

protected void

bcsPreDeserializationHook

​(

ObjectInputStream

ois)

called by readObject after defaultReadObject() but prior to
deserialization of any children.

protected void

bcsPreSerializationHook

​(

ObjectOutputStream

oos)

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

protected void

childDeserializedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

Called by readObject with the newly deserialized child and BCSChild.

protected void

childJustAddedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred.

protected void

childJustRemovedHook

​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred.

protected static boolean

classEquals

​(

Class

<?> first,

Class

<?> second)

Tests to see if two class objects,
or their names are equal.

void

clear

()

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

boolean

contains

​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

boolean

containsAll

​(

Collection

c)

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

boolean

containsKey

​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

protected

Object

[]

copyChildren

()

Gets a copy of the this BeanContext's children.

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

protected void

deserialize

​(

ObjectInputStream

ois,

Collection

coll)

used by readObject to deserialize a collection.

void

dontUseGui

()

notify this instance that it may no longer render a GUI.

protected void

fireChildrenAdded

​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

protected void

fireChildrenRemoved

​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

BeanContext

getBeanContextPeer

()

Gets the instance of

BeanContext

that
this object is providing the implementation for.

protected static

BeanContextChild

getChildBeanContextChild

​(

Object

child)

Gets the BeanContextChild (if any) of the specified child

protected static

BeanContextMembershipListener

getChildBeanContextMembershipListener

​(

Object

child)

Gets the BeanContextMembershipListener
(if any) of the specified child

protected static

PropertyChangeListener

getChildPropertyChangeListener

​(

Object

child)

Gets the PropertyChangeListener
(if any) of the specified child

protected static

Serializable

getChildSerializable

​(

Object

child)

Gets the Serializable (if any) associated with the specified Child

protected static

VetoableChangeListener

getChildVetoableChangeListener

​(

Object

child)

Gets the VetoableChangeListener
(if any) of the specified child

protected static

Visibility

getChildVisibility

​(

Object

child)

Gets the Component (if any) associated with the specified child.

Locale

getLocale

()

Gets the locale for this

BeanContext

.

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

protected void

initialize

()

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

Object

instantiateChild

​(

String

beanName)

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

boolean

isDesignTime

()

Reports whether or not this object is in
currently in design time mode.

boolean

isEmpty

()

Reports whether or not this

BeanContext

is empty.

boolean

isSerializing

()

Is this

BeanContext

in the
process of being serialized?

Iterator

<

Object

>

iterator

()

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

boolean

needsGui

()

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

void

okToUseGui

()

Notify this instance that it may now render a GUI

void

propertyChange

​(

PropertyChangeEvent

pce)

subclasses may envelope to monitor child property changes.

void

readChildren

​(

ObjectInputStream

ois)

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

boolean

remove

​(

Object

targetChild)

Removes a child from this BeanContext.

protected boolean

remove

​(

Object

targetChild,
boolean callChildSetBC)

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

boolean

removeAll

​(

Collection

c)

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

void

removeBeanContextMembershipListener

​(

BeanContextMembershipListener

bcml)

Removes a BeanContextMembershipListener

boolean

retainAll

​(

Collection

c)

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

protected void

serialize

​(

ObjectOutputStream

oos,

Collection

<?> coll)

Used by writeObject to serialize a Collection.

void

setDesignTime

​(boolean dTime)

Sets the new design time value for this

BeanContext

.

void

setLocale

​(

Locale

newLocale)

Sets the locale of this BeanContext.

int

size

()

Gets the number of children currently nested in
this BeanContext.

Object

[]

toArray

()

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

Object

[]

toArray

​(

Object

[] arry)

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

protected boolean

validatePendingAdd

​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

protected boolean

validatePendingRemove

​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

void

vetoableChange

​(

PropertyChangeEvent

pce)

subclasses may envelope to monitor veto child property changes.

void

writeChildren

​(

ObjectOutputStream

oos)

Used to serialize all children of
this

BeanContext

.

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

initializeBeanContextResources

,

isDelegated

,

releaseBeanContextResources

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

serviceAvailable

,

serviceRevoked

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

equals

,

hashCode

,

parallelStream

,

removeIf

,

spliterator

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

---

#### Method Summary

Adds/nests a child within this

BeanContext

.

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

Adds a BeanContextMembershipListener

Used to determine if the

BeanContext

child is avoiding using its GUI.

Returns an iterator of all children
of this

BeanContext

.

called by readObject after defaultReadObject() but prior to
deserialization of any children.

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

Called by readObject with the newly deserialized child and BCSChild.

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred.

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred.

Tests to see if two class objects,
or their names are equal.

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

Determines whether or not the specified object
is currently a child of this

BeanContext

.

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

Gets a copy of the this BeanContext's children.

Subclasses can override this method to insert their own subclass
of Child without having to override add() or the other Collection
methods that add children to the set.

used by readObject to deserialize a collection.

notify this instance that it may no longer render a GUI.

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

Gets the instance of

BeanContext

that
this object is providing the implementation for.

Gets the BeanContextChild (if any) of the specified child

Gets the BeanContextMembershipListener
(if any) of the specified child

Gets the PropertyChangeListener
(if any) of the specified child

Gets the Serializable (if any) associated with the specified Child

Gets the VetoableChangeListener
(if any) of the specified child

Gets the Component (if any) associated with the specified child.

Gets the locale for this

BeanContext

.

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

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

Reports whether or not this object is in
currently in design time mode.

Reports whether or not this

BeanContext

is empty.

Is this

BeanContext

in the
process of being serialized?

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

Notify this instance that it may now render a GUI

subclasses may envelope to monitor child property changes.

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

Removes a child from this BeanContext.

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

Removes a BeanContextMembershipListener

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

Used by writeObject to serialize a Collection.

Sets the new design time value for this

BeanContext

.

Sets the locale of this BeanContext.

Gets the number of children currently nested in
this BeanContext.

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

subclasses may envelope to monitor veto child property changes.

Used to serialize all children of
this

BeanContext

.

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

initializeBeanContextResources

,

isDelegated

,

releaseBeanContextResources

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

serviceAvailable

,

serviceRevoked

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

equals

,

hashCode

,

parallelStream

,

removeIf

,

spliterator

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

============ FIELD DETAIL ===========

- Field Detail

- children

```java
protected transient
HashMap
<
Object
,​
BeanContextSupport.BCSChild
> children
```

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

- bcmListeners

```java
protected transient
ArrayList
<
BeanContextMembershipListener
> bcmListeners
```

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

- locale

```java
protected
Locale
locale
```

The current locale of this BeanContext.

- okToUseGui

```java
protected boolean okToUseGui
```

A

boolean

indicating if this
instance may now render a GUI.

- designTime

```java
protected boolean designTime
```

A

boolean

indicating whether or not
this object is currently in design time mode.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextSupport instance

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dTime

- The initial state,

true

if in design mode,

false

if runtime.
**Parameters:** visible

- The initial visibility.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer

BeanContext

we
are supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dtime

- The initial state,

true

if in design mode,

false

if runtime.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are
supplying an implementation for,
or

null

if this object
is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

,
the default locale
is assigned to the

BeanContext

instance.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer)
```

Create an instance using with a default locale

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object
is its own peer

- BeanContextSupport

```java
public BeanContextSupport()
```

Create an instance that is not a delegate of another object

============ METHOD DETAIL ==========

- Method Detail

- getBeanContextPeer

```java
public
BeanContext
getBeanContextPeer()
```

Gets the instance of

BeanContext

that
this object is providing the implementation for.

**Returns:** the BeanContext instance

- instantiateChild

```java
public
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

**Specified by:** instantiateChild

in interface

BeanContext
**Parameters:** beanName

- the name of the Bean to instantiate within this BeanContext
**Returns:** the new object
**Throws:** IOException

- if there is an I/O error when the bean is being deserialized
**Throws:** ClassNotFoundException

- if the class
identified by the beanName parameter is not found

- size

```java
public int size()
```

Gets the number of children currently nested in
this BeanContext.

**Specified by:** size

in interface

Collection
**Returns:** number of children

- isEmpty

```java
public boolean isEmpty()
```

Reports whether or not this

BeanContext

is empty.
A

BeanContext

is considered
empty when it contains zero
nested children.

**Specified by:** isEmpty

in interface

Collection
**Returns:** if there are not children

- contains

```java
public boolean contains​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Specified by:** contains

in interface

Collection
**Parameters:** o

- the Object in question
**Returns:** if this object is a child

- containsKey

```java
public boolean containsKey​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Parameters:** o

- the Object in question
**Returns:** if this object is a child

- iterator

```java
public
Iterator
<
Object
> iterator()
```

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

**Specified by:** iterator

in interface

Collection
**Specified by:** iterator

in interface

Iterable
**Returns:** an

Iterator

of the nested children

- toArray

```java
public
Object
[] toArray()
```

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

**Specified by:** toArray

in interface

Collection
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

- toArray

```java
public
Object
[] toArray​(
Object
[] arry)
```

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

**Specified by:** toArray

in interface

Collection
**Parameters:** arry

- The array of object
types that are of interest.
**Returns:** an array of children

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

**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the tragetChild and the peer are related by an implementation of BeanContextProxy
**Returns:** Subtype-specific subclass of Child without overriding collection methods

- add

```java
public boolean add​(
Object
targetChild)
```

Adds/nests a child within this

BeanContext

.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

**Specified by:** add

in interface

Collection
**Parameters:** targetChild

- The child objects to nest
within this

BeanContext
**Returns:** true if the child was added successfully.
**See Also:** validatePendingAdd(java.lang.Object)

- remove

```java
public boolean remove​(
Object
targetChild)
```

Removes a child from this BeanContext. If the child object is not
for adding then this method throws an IllegalStateException.

**Specified by:** remove

in interface

Collection
**Parameters:** targetChild

- The child objects to remove
**Returns:** true

if an element was removed as a result of this call
**See Also:** validatePendingRemove(java.lang.Object)

- remove

```java
protected boolean remove​(
Object
targetChild,
boolean callChildSetBC)
```

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

**Parameters:** targetChild

- the JavaBean, BeanContext, or Object to be removed
**Parameters:** callChildSetBC

- used to indicate that
the child should be notified that it is no
longer nested in this

BeanContext

.
**Returns:** whether or not was present before being removed

- containsAll

```java
public boolean containsAll​(
Collection
c)
```

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

**Specified by:** containsAll

in interface

Collection
**Parameters:** c

- the specified

Collection
**Returns:** true

if all objects
in the collection are children of
this

BeanContext

, false if not.
**See Also:** Collection.contains(Object)

- addAll

```java
public boolean addAll​(
Collection
c)
```

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** addAll

in interface

Collection
**Parameters:** c

- collection containing elements to be added to this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.add(Object)

- removeAll

```java
public boolean removeAll​(
Collection
c)
```

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** removeAll

in interface

Collection
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- retainAll

```java
public boolean retainAll​(
Collection
c)
```

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** retainAll

in interface

Collection
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- clear

```java
public void clear()
```

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** clear

in interface

Collection
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation

- addBeanContextMembershipListener

```java
public void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds a BeanContextMembershipListener

**Specified by:** addBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to add
**Throws:** NullPointerException

- if the argument is null

- removeBeanContextMembershipListener

```java
public void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes a BeanContextMembershipListener

**Specified by:** removeBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to remove
**Throws:** NullPointerException

- if the argument is null

- getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResourceAsStream

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream
**Throws:** NullPointerException

- if the argument is null

- getResource

```java
public
URL
getResource​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResource

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream

- setDesignTime

```java
public void setDesignTime​(boolean dTime)
```

Sets the new design time value for this

BeanContext

.

**Specified by:** setDesignTime

in interface

DesignMode
**Parameters:** dTime

- the new designTime value
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

- isDesignTime

```java
public boolean isDesignTime()
```

Reports whether or not this object is in
currently in design time mode.

**Specified by:** isDesignTime

in interface

DesignMode
**Returns:** true

if in design time mode,

false

if not

- setLocale

```java
public void setLocale​(
Locale
newLocale)
throws
PropertyVetoException
```

Sets the locale of this BeanContext.

**Parameters:** newLocale

- the new locale. This method call will have
no effect if newLocale is

null

.
**Throws:** PropertyVetoException

- if the new value is rejected

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale for this

BeanContext

.

**Returns:** the current Locale of the

BeanContext

- needsGui

```java
public boolean needsGui()
```

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

**Specified by:** needsGui

in interface

Visibility
**Returns:** true

if the implementor needs a GUI

- dontUseGui

```java
public void dontUseGui()
```

notify this instance that it may no longer render a GUI.

**Specified by:** dontUseGui

in interface

Visibility

- okToUseGui

```java
public void okToUseGui()
```

Notify this instance that it may now render a GUI

**Specified by:** okToUseGui

in interface

Visibility

- avoidingGui

```java
public boolean avoidingGui()
```

Used to determine if the

BeanContext

child is avoiding using its GUI.

**Specified by:** avoidingGui

in interface

Visibility
**Returns:** is this instance avoiding using its GUI?
**See Also:** Visibility

- isSerializing

```java
public boolean isSerializing()
```

Is this

BeanContext

in the
process of being serialized?

**Returns:** if this

BeanContext

is
currently being serialized

- bcsChildren

```java
protected
Iterator
<
BeanContextSupport.BCSChild
> bcsChildren()
```

Returns an iterator of all children
of this

BeanContext

.

**Returns:** an iterator for all the current BCSChild values

- bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

This method may be overridden by subclasses to perform custom
serialization of their state prior to this superclass serializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of writeObject().

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

called by readObject after defaultReadObject() but prior to
deserialization of any children.

This method may be overridden by subclasses to perform custom
deserialization of their state prior to this superclass deserializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of readObject().

**Parameters:** ois

- the

ObjectInputStream

to use during deserialization
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- childDeserializedHook

```java
protected void childDeserializedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

Called by readObject with the newly deserialized child and BCSChild.

**Parameters:** child

- the newly deserialized child
**Parameters:** bcsc

- the newly deserialized BCSChild

- serialize

```java
protected final void serialize​(
ObjectOutputStream
oos,

Collection
<?> coll)
throws
IOException
```

Used by writeObject to serialize a Collection.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Parameters:** coll

- the

Collection

to serialize
**Throws:** IOException

- if serialization failed

- deserialize

```java
protected final void deserialize​(
ObjectInputStream
ois,

Collection
coll)
throws
IOException
,

ClassNotFoundException
```

used by readObject to deserialize a collection.

**Parameters:** ois

- the ObjectInputStream to use
**Parameters:** coll

- the Collection
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- writeChildren

```java
public final void writeChildren​(
ObjectOutputStream
oos)
throws
IOException
```

Used to serialize all children of
this

BeanContext

.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

- readChildren

```java
public final void readChildren​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

**Parameters:** ois

- the ObjectInputStream to use
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
pce)
throws
PropertyVetoException
```

subclasses may envelope to monitor veto child property changes.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** pce

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
pce)
```

subclasses may envelope to monitor child property changes.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** pce

- A PropertyChangeEvent object describing the event source
and the property that has changed.

- validatePendingAdd

```java
protected boolean validatePendingAdd​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be added to this BeanContext, otherwise false.

- validatePendingRemove

```java
protected boolean validatePendingRemove​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be removed from this BeanContext, otherwise false.

- childJustAddedHook

```java
protected void childJustAddedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- getChildVisibility

```java
protected static final
Visibility
getChildVisibility​(
Object
child)
```

Gets the Component (if any) associated with the specified child.

**Parameters:** child

- the specified child
**Returns:** the Component (if any) associated with the specified child.

- getChildSerializable

```java
protected static final
Serializable
getChildSerializable​(
Object
child)
```

Gets the Serializable (if any) associated with the specified Child

**Parameters:** child

- the specified child
**Returns:** the Serializable (if any) associated with the specified Child

- getChildPropertyChangeListener

```java
protected static final
PropertyChangeListener
getChildPropertyChangeListener​(
Object
child)
```

Gets the PropertyChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the PropertyChangeListener (if any) of the specified child

- getChildVetoableChangeListener

```java
protected static final
VetoableChangeListener
getChildVetoableChangeListener​(
Object
child)
```

Gets the VetoableChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the VetoableChangeListener (if any) of the specified child

- getChildBeanContextMembershipListener

```java
protected static final
BeanContextMembershipListener
getChildBeanContextMembershipListener​(
Object
child)
```

Gets the BeanContextMembershipListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextMembershipListener (if any) of the specified child

- getChildBeanContextChild

```java
protected static final
BeanContextChild
getChildBeanContextChild​(
Object
child)
```

Gets the BeanContextChild (if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextChild (if any) of the specified child
**Throws:** IllegalArgumentException

- if child implements both BeanContextChild and BeanContextProxy

- fireChildrenAdded

```java
protected final void fireChildrenAdded​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

- fireChildrenRemoved

```java
protected final void fireChildrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

- initialize

```java
protected void initialize()
```

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

This class uses this method to instantiate inner class listeners used
to monitor PropertyChange and VetoableChange events on children.

subclasses may envelope this method to add their own initialization
behavior

- copyChildren

```java
protected final
Object
[] copyChildren()
```

Gets a copy of the this BeanContext's children.

**Returns:** a copy of the current nested children

- classEquals

```java
protected static final boolean classEquals​(
Class
<?> first,

Class
<?> second)
```

Tests to see if two class objects,
or their names are equal.

**Parameters:** first

- the first object
**Parameters:** second

- the second object
**Returns:** true if equal, false if not

Field Detail

- children

```java
protected transient
HashMap
<
Object
,​
BeanContextSupport.BCSChild
> children
```

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

- bcmListeners

```java
protected transient
ArrayList
<
BeanContextMembershipListener
> bcmListeners
```

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

- locale

```java
protected
Locale
locale
```

The current locale of this BeanContext.

- okToUseGui

```java
protected boolean okToUseGui
```

A

boolean

indicating if this
instance may now render a GUI.

- designTime

```java
protected boolean designTime
```

A

boolean

indicating whether or not
this object is currently in design time mode.

---

#### Field Detail

children

```java
protected transient
HashMap
<
Object
,​
BeanContextSupport.BCSChild
> children
```

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

---

#### children

protected transient

HashMap

<

Object

,​

BeanContextSupport.BCSChild

> children

all accesses to the

protected HashMap children

field
shall be synchronized on that object.

bcmListeners

```java
protected transient
ArrayList
<
BeanContextMembershipListener
> bcmListeners
```

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

---

#### bcmListeners

protected transient

ArrayList

<

BeanContextMembershipListener

> bcmListeners

all accesses to the

protected ArrayList bcmListeners

field
shall be synchronized on that object.

locale

```java
protected
Locale
locale
```

The current locale of this BeanContext.

---

#### locale

protected

Locale

locale

The current locale of this BeanContext.

okToUseGui

```java
protected boolean okToUseGui
```

A

boolean

indicating if this
instance may now render a GUI.

---

#### okToUseGui

protected boolean okToUseGui

A

boolean

indicating if this
instance may now render a GUI.

designTime

```java
protected boolean designTime
```

A

boolean

indicating whether or not
this object is currently in design time mode.

---

#### designTime

protected boolean designTime

A

boolean

indicating whether or not
this object is currently in design time mode.

Constructor Detail

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextSupport instance

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dTime

- The initial state,

true

if in design mode,

false

if runtime.
**Parameters:** visible

- The initial visibility.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer

BeanContext

we
are supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dtime

- The initial state,

true

if in design mode,

false

if runtime.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are
supplying an implementation for,
or

null

if this object
is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

,
the default locale
is assigned to the

BeanContext

instance.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

- BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer)
```

Create an instance using with a default locale

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object
is its own peer

- BeanContextSupport

```java
public BeanContextSupport()
```

Create an instance that is not a delegate of another object

---

#### Constructor Detail

BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dTime,
boolean visible)
```

Construct a BeanContextSupport instance

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this BeanContext. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dTime

- The initial state,

true

if in design mode,

false

if runtime.
**Parameters:** visible

- The initial visibility.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### BeanContextSupport

public BeanContextSupport​(

BeanContext

peer,

Locale

lcle,
boolean dTime,
boolean visible)

Construct a BeanContextSupport instance

BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle,
boolean dtime)
```

Create an instance using the specified Locale and design mode.

**Parameters:** peer

- The peer

BeanContext

we
are supplying an implementation for,
or

null

if this object is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

, the default locale
is assigned to the

BeanContext

instance.
**Parameters:** dtime

- The initial state,

true

if in design mode,

false

if runtime.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### BeanContextSupport

public BeanContextSupport​(

BeanContext

peer,

Locale

lcle,
boolean dtime)

Create an instance using the specified Locale and design mode.

BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer,

Locale
lcle)
```

Create an instance using the specified locale

**Parameters:** peer

- The peer BeanContext we are
supplying an implementation for,
or

null

if this object
is its own peer
**Parameters:** lcle

- The current Locale for this

BeanContext

. If

lcle

is

null

,
the default locale
is assigned to the

BeanContext

instance.
**See Also:** Locale.getDefault()

,

Locale.setDefault(java.util.Locale)

---

#### BeanContextSupport

public BeanContextSupport​(

BeanContext

peer,

Locale

lcle)

Create an instance using the specified locale

BeanContextSupport

```java
public BeanContextSupport​(
BeanContext
peer)
```

Create an instance using with a default locale

**Parameters:** peer

- The peer

BeanContext

we are
supplying an implementation for,
or

null

if this object
is its own peer

---

#### BeanContextSupport

public BeanContextSupport​(

BeanContext

peer)

Create an instance using with a default locale

BeanContextSupport

```java
public BeanContextSupport()
```

Create an instance that is not a delegate of another object

---

#### BeanContextSupport

public BeanContextSupport()

Create an instance that is not a delegate of another object

Method Detail

- getBeanContextPeer

```java
public
BeanContext
getBeanContextPeer()
```

Gets the instance of

BeanContext

that
this object is providing the implementation for.

**Returns:** the BeanContext instance

- instantiateChild

```java
public
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

**Specified by:** instantiateChild

in interface

BeanContext
**Parameters:** beanName

- the name of the Bean to instantiate within this BeanContext
**Returns:** the new object
**Throws:** IOException

- if there is an I/O error when the bean is being deserialized
**Throws:** ClassNotFoundException

- if the class
identified by the beanName parameter is not found

- size

```java
public int size()
```

Gets the number of children currently nested in
this BeanContext.

**Specified by:** size

in interface

Collection
**Returns:** number of children

- isEmpty

```java
public boolean isEmpty()
```

Reports whether or not this

BeanContext

is empty.
A

BeanContext

is considered
empty when it contains zero
nested children.

**Specified by:** isEmpty

in interface

Collection
**Returns:** if there are not children

- contains

```java
public boolean contains​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Specified by:** contains

in interface

Collection
**Parameters:** o

- the Object in question
**Returns:** if this object is a child

- containsKey

```java
public boolean containsKey​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Parameters:** o

- the Object in question
**Returns:** if this object is a child

- iterator

```java
public
Iterator
<
Object
> iterator()
```

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

**Specified by:** iterator

in interface

Collection
**Specified by:** iterator

in interface

Iterable
**Returns:** an

Iterator

of the nested children

- toArray

```java
public
Object
[] toArray()
```

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

**Specified by:** toArray

in interface

Collection
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

- toArray

```java
public
Object
[] toArray​(
Object
[] arry)
```

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

**Specified by:** toArray

in interface

Collection
**Parameters:** arry

- The array of object
types that are of interest.
**Returns:** an array of children

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

**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the tragetChild and the peer are related by an implementation of BeanContextProxy
**Returns:** Subtype-specific subclass of Child without overriding collection methods

- add

```java
public boolean add​(
Object
targetChild)
```

Adds/nests a child within this

BeanContext

.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

**Specified by:** add

in interface

Collection
**Parameters:** targetChild

- The child objects to nest
within this

BeanContext
**Returns:** true if the child was added successfully.
**See Also:** validatePendingAdd(java.lang.Object)

- remove

```java
public boolean remove​(
Object
targetChild)
```

Removes a child from this BeanContext. If the child object is not
for adding then this method throws an IllegalStateException.

**Specified by:** remove

in interface

Collection
**Parameters:** targetChild

- The child objects to remove
**Returns:** true

if an element was removed as a result of this call
**See Also:** validatePendingRemove(java.lang.Object)

- remove

```java
protected boolean remove​(
Object
targetChild,
boolean callChildSetBC)
```

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

**Parameters:** targetChild

- the JavaBean, BeanContext, or Object to be removed
**Parameters:** callChildSetBC

- used to indicate that
the child should be notified that it is no
longer nested in this

BeanContext

.
**Returns:** whether or not was present before being removed

- containsAll

```java
public boolean containsAll​(
Collection
c)
```

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

**Specified by:** containsAll

in interface

Collection
**Parameters:** c

- the specified

Collection
**Returns:** true

if all objects
in the collection are children of
this

BeanContext

, false if not.
**See Also:** Collection.contains(Object)

- addAll

```java
public boolean addAll​(
Collection
c)
```

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** addAll

in interface

Collection
**Parameters:** c

- collection containing elements to be added to this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.add(Object)

- removeAll

```java
public boolean removeAll​(
Collection
c)
```

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** removeAll

in interface

Collection
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- retainAll

```java
public boolean retainAll​(
Collection
c)
```

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** retainAll

in interface

Collection
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- clear

```java
public void clear()
```

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** clear

in interface

Collection
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation

- addBeanContextMembershipListener

```java
public void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds a BeanContextMembershipListener

**Specified by:** addBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to add
**Throws:** NullPointerException

- if the argument is null

- removeBeanContextMembershipListener

```java
public void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes a BeanContextMembershipListener

**Specified by:** removeBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to remove
**Throws:** NullPointerException

- if the argument is null

- getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResourceAsStream

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream
**Throws:** NullPointerException

- if the argument is null

- getResource

```java
public
URL
getResource​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResource

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream

- setDesignTime

```java
public void setDesignTime​(boolean dTime)
```

Sets the new design time value for this

BeanContext

.

**Specified by:** setDesignTime

in interface

DesignMode
**Parameters:** dTime

- the new designTime value
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

- isDesignTime

```java
public boolean isDesignTime()
```

Reports whether or not this object is in
currently in design time mode.

**Specified by:** isDesignTime

in interface

DesignMode
**Returns:** true

if in design time mode,

false

if not

- setLocale

```java
public void setLocale​(
Locale
newLocale)
throws
PropertyVetoException
```

Sets the locale of this BeanContext.

**Parameters:** newLocale

- the new locale. This method call will have
no effect if newLocale is

null

.
**Throws:** PropertyVetoException

- if the new value is rejected

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale for this

BeanContext

.

**Returns:** the current Locale of the

BeanContext

- needsGui

```java
public boolean needsGui()
```

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

**Specified by:** needsGui

in interface

Visibility
**Returns:** true

if the implementor needs a GUI

- dontUseGui

```java
public void dontUseGui()
```

notify this instance that it may no longer render a GUI.

**Specified by:** dontUseGui

in interface

Visibility

- okToUseGui

```java
public void okToUseGui()
```

Notify this instance that it may now render a GUI

**Specified by:** okToUseGui

in interface

Visibility

- avoidingGui

```java
public boolean avoidingGui()
```

Used to determine if the

BeanContext

child is avoiding using its GUI.

**Specified by:** avoidingGui

in interface

Visibility
**Returns:** is this instance avoiding using its GUI?
**See Also:** Visibility

- isSerializing

```java
public boolean isSerializing()
```

Is this

BeanContext

in the
process of being serialized?

**Returns:** if this

BeanContext

is
currently being serialized

- bcsChildren

```java
protected
Iterator
<
BeanContextSupport.BCSChild
> bcsChildren()
```

Returns an iterator of all children
of this

BeanContext

.

**Returns:** an iterator for all the current BCSChild values

- bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

This method may be overridden by subclasses to perform custom
serialization of their state prior to this superclass serializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of writeObject().

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

called by readObject after defaultReadObject() but prior to
deserialization of any children.

This method may be overridden by subclasses to perform custom
deserialization of their state prior to this superclass deserializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of readObject().

**Parameters:** ois

- the

ObjectInputStream

to use during deserialization
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- childDeserializedHook

```java
protected void childDeserializedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

Called by readObject with the newly deserialized child and BCSChild.

**Parameters:** child

- the newly deserialized child
**Parameters:** bcsc

- the newly deserialized BCSChild

- serialize

```java
protected final void serialize​(
ObjectOutputStream
oos,

Collection
<?> coll)
throws
IOException
```

Used by writeObject to serialize a Collection.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Parameters:** coll

- the

Collection

to serialize
**Throws:** IOException

- if serialization failed

- deserialize

```java
protected final void deserialize​(
ObjectInputStream
ois,

Collection
coll)
throws
IOException
,

ClassNotFoundException
```

used by readObject to deserialize a collection.

**Parameters:** ois

- the ObjectInputStream to use
**Parameters:** coll

- the Collection
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- writeChildren

```java
public final void writeChildren​(
ObjectOutputStream
oos)
throws
IOException
```

Used to serialize all children of
this

BeanContext

.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

- readChildren

```java
public final void readChildren​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

**Parameters:** ois

- the ObjectInputStream to use
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

- vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
pce)
throws
PropertyVetoException
```

subclasses may envelope to monitor veto child property changes.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** pce

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
pce)
```

subclasses may envelope to monitor child property changes.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** pce

- A PropertyChangeEvent object describing the event source
and the property that has changed.

- validatePendingAdd

```java
protected boolean validatePendingAdd​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be added to this BeanContext, otherwise false.

- validatePendingRemove

```java
protected boolean validatePendingRemove​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be removed from this BeanContext, otherwise false.

- childJustAddedHook

```java
protected void childJustAddedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

- getChildVisibility

```java
protected static final
Visibility
getChildVisibility​(
Object
child)
```

Gets the Component (if any) associated with the specified child.

**Parameters:** child

- the specified child
**Returns:** the Component (if any) associated with the specified child.

- getChildSerializable

```java
protected static final
Serializable
getChildSerializable​(
Object
child)
```

Gets the Serializable (if any) associated with the specified Child

**Parameters:** child

- the specified child
**Returns:** the Serializable (if any) associated with the specified Child

- getChildPropertyChangeListener

```java
protected static final
PropertyChangeListener
getChildPropertyChangeListener​(
Object
child)
```

Gets the PropertyChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the PropertyChangeListener (if any) of the specified child

- getChildVetoableChangeListener

```java
protected static final
VetoableChangeListener
getChildVetoableChangeListener​(
Object
child)
```

Gets the VetoableChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the VetoableChangeListener (if any) of the specified child

- getChildBeanContextMembershipListener

```java
protected static final
BeanContextMembershipListener
getChildBeanContextMembershipListener​(
Object
child)
```

Gets the BeanContextMembershipListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextMembershipListener (if any) of the specified child

- getChildBeanContextChild

```java
protected static final
BeanContextChild
getChildBeanContextChild​(
Object
child)
```

Gets the BeanContextChild (if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextChild (if any) of the specified child
**Throws:** IllegalArgumentException

- if child implements both BeanContextChild and BeanContextProxy

- fireChildrenAdded

```java
protected final void fireChildrenAdded​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

- fireChildrenRemoved

```java
protected final void fireChildrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

- initialize

```java
protected void initialize()
```

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

This class uses this method to instantiate inner class listeners used
to monitor PropertyChange and VetoableChange events on children.

subclasses may envelope this method to add their own initialization
behavior

- copyChildren

```java
protected final
Object
[] copyChildren()
```

Gets a copy of the this BeanContext's children.

**Returns:** a copy of the current nested children

- classEquals

```java
protected static final boolean classEquals​(
Class
<?> first,

Class
<?> second)
```

Tests to see if two class objects,
or their names are equal.

**Parameters:** first

- the first object
**Parameters:** second

- the second object
**Returns:** true if equal, false if not

---

#### Method Detail

getBeanContextPeer

```java
public
BeanContext
getBeanContextPeer()
```

Gets the instance of

BeanContext

that
this object is providing the implementation for.

**Returns:** the BeanContext instance

---

#### getBeanContextPeer

public

BeanContext

getBeanContextPeer()

Gets the instance of

BeanContext

that
this object is providing the implementation for.

instantiateChild

```java
public
Object
instantiateChild​(
String
beanName)
throws
IOException
,

ClassNotFoundException
```

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

**Specified by:** instantiateChild

in interface

BeanContext
**Parameters:** beanName

- the name of the Bean to instantiate within this BeanContext
**Returns:** the new object
**Throws:** IOException

- if there is an I/O error when the bean is being deserialized
**Throws:** ClassNotFoundException

- if the class
identified by the beanName parameter is not found

---

#### instantiateChild

public

Object

instantiateChild​(

String

beanName)
throws

IOException

,

ClassNotFoundException

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

The instantiateChild method is a convenience hook
in BeanContext to simplify
the task of instantiating a Bean, nested,
into a

BeanContext

.

The semantics of the beanName parameter are defined by java.beans.Beans.instantiate.

size

```java
public int size()
```

Gets the number of children currently nested in
this BeanContext.

**Specified by:** size

in interface

Collection
**Returns:** number of children

---

#### size

public int size()

Gets the number of children currently nested in
this BeanContext.

isEmpty

```java
public boolean isEmpty()
```

Reports whether or not this

BeanContext

is empty.
A

BeanContext

is considered
empty when it contains zero
nested children.

**Specified by:** isEmpty

in interface

Collection
**Returns:** if there are not children

---

#### isEmpty

public boolean isEmpty()

Reports whether or not this

BeanContext

is empty.
A

BeanContext

is considered
empty when it contains zero
nested children.

contains

```java
public boolean contains​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Specified by:** contains

in interface

Collection
**Parameters:** o

- the Object in question
**Returns:** if this object is a child

---

#### contains

public boolean contains​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

containsKey

```java
public boolean containsKey​(
Object
o)
```

Determines whether or not the specified object
is currently a child of this

BeanContext

.

**Parameters:** o

- the Object in question
**Returns:** if this object is a child

---

#### containsKey

public boolean containsKey​(

Object

o)

Determines whether or not the specified object
is currently a child of this

BeanContext

.

iterator

```java
public
Iterator
<
Object
> iterator()
```

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

**Specified by:** iterator

in interface

Collection
**Specified by:** iterator

in interface

Iterable
**Returns:** an

Iterator

of the nested children

---

#### iterator

public

Iterator

<

Object

> iterator()

Gets all JavaBean or

BeanContext

instances
currently nested in this

BeanContext

.

toArray

```java
public
Object
[] toArray()
```

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

**Specified by:** toArray

in interface

Collection
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

---

#### toArray

public

Object

[] toArray()

Gets all JavaBean or

BeanContext

instances currently nested in this BeanContext.

toArray

```java
public
Object
[] toArray​(
Object
[] arry)
```

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

**Specified by:** toArray

in interface

Collection
**Parameters:** arry

- The array of object
types that are of interest.
**Returns:** an array of children

---

#### toArray

public

Object

[] toArray​(

Object

[] arry)

Gets an array containing all children of
this

BeanContext

that match
the types contained in arry.

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

**Parameters:** targetChild

- the child to create the Child on behalf of
**Parameters:** peer

- the peer if the tragetChild and the peer are related by an implementation of BeanContextProxy
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

add

```java
public boolean add​(
Object
targetChild)
```

Adds/nests a child within this

BeanContext

.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

**Specified by:** add

in interface

Collection
**Parameters:** targetChild

- The child objects to nest
within this

BeanContext
**Returns:** true if the child was added successfully.
**See Also:** validatePendingAdd(java.lang.Object)

---

#### add

public boolean add​(

Object

targetChild)

Adds/nests a child within this

BeanContext

.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

Invoked as a side effect of java.beans.Beans.instantiate().
If the child object is not valid for adding then this method
throws an IllegalStateException.

remove

```java
public boolean remove​(
Object
targetChild)
```

Removes a child from this BeanContext. If the child object is not
for adding then this method throws an IllegalStateException.

**Specified by:** remove

in interface

Collection
**Parameters:** targetChild

- The child objects to remove
**Returns:** true

if an element was removed as a result of this call
**See Also:** validatePendingRemove(java.lang.Object)

---

#### remove

public boolean remove​(

Object

targetChild)

Removes a child from this BeanContext. If the child object is not
for adding then this method throws an IllegalStateException.

remove

```java
protected boolean remove​(
Object
targetChild,
boolean callChildSetBC)
```

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

**Parameters:** targetChild

- the JavaBean, BeanContext, or Object to be removed
**Parameters:** callChildSetBC

- used to indicate that
the child should be notified that it is no
longer nested in this

BeanContext

.
**Returns:** whether or not was present before being removed

---

#### remove

protected boolean remove​(

Object

targetChild,
boolean callChildSetBC)

internal remove used when removal caused by
unexpected

setBeanContext

or
by

remove()

invocation.

containsAll

```java
public boolean containsAll​(
Collection
c)
```

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

**Specified by:** containsAll

in interface

Collection
**Parameters:** c

- the specified

Collection
**Returns:** true

if all objects
in the collection are children of
this

BeanContext

, false if not.
**See Also:** Collection.contains(Object)

---

#### containsAll

public boolean containsAll​(

Collection

c)

Tests to see if all objects in the
specified

Collection

are children of
this

BeanContext

.

addAll

```java
public boolean addAll​(
Collection
c)
```

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** addAll

in interface

Collection
**Parameters:** c

- collection containing elements to be added to this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.add(Object)

---

#### addAll

public boolean addAll​(

Collection

c)

add Collection to set of Children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

removeAll

```java
public boolean removeAll​(
Collection
c)
```

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** removeAll

in interface

Collection
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

---

#### removeAll

public boolean removeAll​(

Collection

c)

remove all specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

retainAll

```java
public boolean retainAll​(
Collection
c)
```

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** retainAll

in interface

Collection
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** this implementation unconditionally throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

---

#### retainAll

public boolean retainAll​(

Collection

c)

retain only specified children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

clear

```java
public void clear()
```

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

**Specified by:** clear

in interface

Collection
**Throws:** UnsupportedOperationException

- thrown unconditionally by this implementation

---

#### clear

public void clear()

clear the children (Unsupported)
implementations must synchronized on the hierarchy lock and "children" protected field

addBeanContextMembershipListener

```java
public void addBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Adds a BeanContextMembershipListener

**Specified by:** addBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to add
**Throws:** NullPointerException

- if the argument is null

---

#### addBeanContextMembershipListener

public void addBeanContextMembershipListener​(

BeanContextMembershipListener

bcml)

Adds a BeanContextMembershipListener

removeBeanContextMembershipListener

```java
public void removeBeanContextMembershipListener​(
BeanContextMembershipListener
bcml)
```

Removes a BeanContextMembershipListener

**Specified by:** removeBeanContextMembershipListener

in interface

BeanContext
**Parameters:** bcml

- the BeanContextMembershipListener to remove
**Throws:** NullPointerException

- if the argument is null

---

#### removeBeanContextMembershipListener

public void removeBeanContextMembershipListener​(

BeanContextMembershipListener

bcml)

Removes a BeanContextMembershipListener

getResourceAsStream

```java
public
InputStream
getResourceAsStream​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResourceAsStream

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream
**Throws:** NullPointerException

- if the argument is null

---

#### getResourceAsStream

public

InputStream

getResourceAsStream​(

String

name,

BeanContextChild

bcc)

Description copied from interface:

BeanContext

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
public
URL
getResource​(
String
name,

BeanContextChild
bcc)
```

Description copied from interface:

BeanContext

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

**Specified by:** getResource

in interface

BeanContext
**Parameters:** name

- the name of the resource requested.
**Parameters:** bcc

- the child object making the request.
**Returns:** the requested resource as an InputStream

---

#### getResource

public

URL

getResource​(

String

name,

BeanContextChild

bcc)

Description copied from interface:

BeanContext

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

setDesignTime

```java
public void setDesignTime​(boolean dTime)
```

Sets the new design time value for this

BeanContext

.

**Specified by:** setDesignTime

in interface

DesignMode
**Parameters:** dTime

- the new designTime value
**See Also:** BeanContext

,

BeanContextMembershipListener

,

PropertyChangeEvent

---

#### setDesignTime

public void setDesignTime​(boolean dTime)

Sets the new design time value for this

BeanContext

.

isDesignTime

```java
public boolean isDesignTime()
```

Reports whether or not this object is in
currently in design time mode.

**Specified by:** isDesignTime

in interface

DesignMode
**Returns:** true

if in design time mode,

false

if not

---

#### isDesignTime

public boolean isDesignTime()

Reports whether or not this object is in
currently in design time mode.

setLocale

```java
public void setLocale​(
Locale
newLocale)
throws
PropertyVetoException
```

Sets the locale of this BeanContext.

**Parameters:** newLocale

- the new locale. This method call will have
no effect if newLocale is

null

.
**Throws:** PropertyVetoException

- if the new value is rejected

---

#### setLocale

public void setLocale​(

Locale

newLocale)
throws

PropertyVetoException

Sets the locale of this BeanContext.

getLocale

```java
public
Locale
getLocale()
```

Gets the locale for this

BeanContext

.

**Returns:** the current Locale of the

BeanContext

---

#### getLocale

public

Locale

getLocale()

Gets the locale for this

BeanContext

.

needsGui

```java
public boolean needsGui()
```

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

**Specified by:** needsGui

in interface

Visibility
**Returns:** true

if the implementor needs a GUI

---

#### needsGui

public boolean needsGui()

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

This method is typically called from the environment in order to determine
if the implementor "needs" a GUI.

The algorithm used herein tests the BeanContextPeer, and its current children
to determine if they are either Containers, Components, or if they implement
Visibility and return needsGui() == true.

dontUseGui

```java
public void dontUseGui()
```

notify this instance that it may no longer render a GUI.

**Specified by:** dontUseGui

in interface

Visibility

---

#### dontUseGui

public void dontUseGui()

notify this instance that it may no longer render a GUI.

okToUseGui

```java
public void okToUseGui()
```

Notify this instance that it may now render a GUI

**Specified by:** okToUseGui

in interface

Visibility

---

#### okToUseGui

public void okToUseGui()

Notify this instance that it may now render a GUI

avoidingGui

```java
public boolean avoidingGui()
```

Used to determine if the

BeanContext

child is avoiding using its GUI.

**Specified by:** avoidingGui

in interface

Visibility
**Returns:** is this instance avoiding using its GUI?
**See Also:** Visibility

---

#### avoidingGui

public boolean avoidingGui()

Used to determine if the

BeanContext

child is avoiding using its GUI.

isSerializing

```java
public boolean isSerializing()
```

Is this

BeanContext

in the
process of being serialized?

**Returns:** if this

BeanContext

is
currently being serialized

---

#### isSerializing

public boolean isSerializing()

Is this

BeanContext

in the
process of being serialized?

bcsChildren

```java
protected
Iterator
<
BeanContextSupport.BCSChild
> bcsChildren()
```

Returns an iterator of all children
of this

BeanContext

.

**Returns:** an iterator for all the current BCSChild values

---

#### bcsChildren

protected

Iterator

<

BeanContextSupport.BCSChild

> bcsChildren()

Returns an iterator of all children
of this

BeanContext

.

bcsPreSerializationHook

```java
protected void bcsPreSerializationHook​(
ObjectOutputStream
oos)
throws
IOException
```

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

This method may be overridden by subclasses to perform custom
serialization of their state prior to this superclass serializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of writeObject().

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

called by writeObject after defaultWriteObject() but prior to
serialization of currently serializable children.

This method may be overridden by subclasses to perform custom
serialization of their state prior to this superclass serializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of writeObject().

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

called by readObject after defaultReadObject() but prior to
deserialization of any children.

This method may be overridden by subclasses to perform custom
deserialization of their state prior to this superclass deserializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of readObject().

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

called by readObject after defaultReadObject() but prior to
deserialization of any children.

This method may be overridden by subclasses to perform custom
deserialization of their state prior to this superclass deserializing
the children.

This method should not however be used by subclasses to replace their
own implementation (if any) of readObject().

childDeserializedHook

```java
protected void childDeserializedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

Called by readObject with the newly deserialized child and BCSChild.

**Parameters:** child

- the newly deserialized child
**Parameters:** bcsc

- the newly deserialized BCSChild

---

#### childDeserializedHook

protected void childDeserializedHook​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

Called by readObject with the newly deserialized child and BCSChild.

serialize

```java
protected final void serialize​(
ObjectOutputStream
oos,

Collection
<?> coll)
throws
IOException
```

Used by writeObject to serialize a Collection.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Parameters:** coll

- the

Collection

to serialize
**Throws:** IOException

- if serialization failed

---

#### serialize

protected final void serialize​(

ObjectOutputStream

oos,

Collection

<?> coll)
throws

IOException

Used by writeObject to serialize a Collection.

deserialize

```java
protected final void deserialize​(
ObjectInputStream
ois,

Collection
coll)
throws
IOException
,

ClassNotFoundException
```

used by readObject to deserialize a collection.

**Parameters:** ois

- the ObjectInputStream to use
**Parameters:** coll

- the Collection
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

---

#### deserialize

protected final void deserialize​(

ObjectInputStream

ois,

Collection

coll)
throws

IOException

,

ClassNotFoundException

used by readObject to deserialize a collection.

writeChildren

```java
public final void writeChildren​(
ObjectOutputStream
oos)
throws
IOException
```

Used to serialize all children of
this

BeanContext

.

**Parameters:** oos

- the

ObjectOutputStream

to use during serialization
**Throws:** IOException

- if serialization failed

---

#### writeChildren

public final void writeChildren​(

ObjectOutputStream

oos)
throws

IOException

Used to serialize all children of
this

BeanContext

.

readChildren

```java
public final void readChildren​(
ObjectInputStream
ois)
throws
IOException
,

ClassNotFoundException
```

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

**Parameters:** ois

- the ObjectInputStream to use
**Throws:** IOException

- if deserialization failed
**Throws:** ClassNotFoundException

- if needed classes are not found

---

#### readChildren

public final void readChildren​(

ObjectInputStream

ois)
throws

IOException

,

ClassNotFoundException

When an instance of this class is used as a delegate for the
implementation of the BeanContext protocols (and its subprotocols)
there exists a 'chicken and egg' problem during deserialization

vetoableChange

```java
public void vetoableChange​(
PropertyChangeEvent
pce)
throws
PropertyVetoException
```

subclasses may envelope to monitor veto child property changes.

**Specified by:** vetoableChange

in interface

VetoableChangeListener
**Parameters:** pce

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

---

#### vetoableChange

public void vetoableChange​(

PropertyChangeEvent

pce)
throws

PropertyVetoException

subclasses may envelope to monitor veto child property changes.

propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
pce)
```

subclasses may envelope to monitor child property changes.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** pce

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

#### propertyChange

public void propertyChange​(

PropertyChangeEvent

pce)

subclasses may envelope to monitor child property changes.

validatePendingAdd

```java
protected boolean validatePendingAdd​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be added to this BeanContext, otherwise false.

---

#### validatePendingAdd

protected boolean validatePendingAdd​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being added to the BeanContext.

validatePendingRemove

```java
protected boolean validatePendingRemove​(
Object
targetChild)
```

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

**Parameters:** targetChild

- the child to create the Child on behalf of
**Returns:** true iff the child may be removed from this BeanContext, otherwise false.

---

#### validatePendingRemove

protected boolean validatePendingRemove​(

Object

targetChild)

Subclasses of this class may override, or envelope, this method to
add validation behavior for the BeanContext to examine child objects
immediately prior to their being removed from the BeanContext.

childJustAddedHook

```java
protected void childJustAddedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred. The method is called with the child synchronized.

**Parameters:** child

- the child
**Parameters:** bcsc

- the BCSChild

---

#### childJustAddedHook

protected void childJustAddedHook​(

Object

child,

BeanContextSupport.BCSChild

bcsc)

subclasses may override this method to simply extend add() semantics
after the child has been added and before the event notification has
occurred. The method is called with the child synchronized.

childJustRemovedHook

```java
protected void childJustRemovedHook​(
Object
child,

BeanContextSupport.BCSChild
bcsc)
```

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred. The method is called with the child synchronized.

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

subclasses may override this method to simply extend remove() semantics
after the child has been removed and before the event notification has
occurred. The method is called with the child synchronized.

getChildVisibility

```java
protected static final
Visibility
getChildVisibility​(
Object
child)
```

Gets the Component (if any) associated with the specified child.

**Parameters:** child

- the specified child
**Returns:** the Component (if any) associated with the specified child.

---

#### getChildVisibility

protected static final

Visibility

getChildVisibility​(

Object

child)

Gets the Component (if any) associated with the specified child.

getChildSerializable

```java
protected static final
Serializable
getChildSerializable​(
Object
child)
```

Gets the Serializable (if any) associated with the specified Child

**Parameters:** child

- the specified child
**Returns:** the Serializable (if any) associated with the specified Child

---

#### getChildSerializable

protected static final

Serializable

getChildSerializable​(

Object

child)

Gets the Serializable (if any) associated with the specified Child

getChildPropertyChangeListener

```java
protected static final
PropertyChangeListener
getChildPropertyChangeListener​(
Object
child)
```

Gets the PropertyChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the PropertyChangeListener (if any) of the specified child

---

#### getChildPropertyChangeListener

protected static final

PropertyChangeListener

getChildPropertyChangeListener​(

Object

child)

Gets the PropertyChangeListener
(if any) of the specified child

getChildVetoableChangeListener

```java
protected static final
VetoableChangeListener
getChildVetoableChangeListener​(
Object
child)
```

Gets the VetoableChangeListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the VetoableChangeListener (if any) of the specified child

---

#### getChildVetoableChangeListener

protected static final

VetoableChangeListener

getChildVetoableChangeListener​(

Object

child)

Gets the VetoableChangeListener
(if any) of the specified child

getChildBeanContextMembershipListener

```java
protected static final
BeanContextMembershipListener
getChildBeanContextMembershipListener​(
Object
child)
```

Gets the BeanContextMembershipListener
(if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextMembershipListener (if any) of the specified child

---

#### getChildBeanContextMembershipListener

protected static final

BeanContextMembershipListener

getChildBeanContextMembershipListener​(

Object

child)

Gets the BeanContextMembershipListener
(if any) of the specified child

getChildBeanContextChild

```java
protected static final
BeanContextChild
getChildBeanContextChild​(
Object
child)
```

Gets the BeanContextChild (if any) of the specified child

**Parameters:** child

- the specified child
**Returns:** the BeanContextChild (if any) of the specified child
**Throws:** IllegalArgumentException

- if child implements both BeanContextChild and BeanContextProxy

---

#### getChildBeanContextChild

protected static final

BeanContextChild

getChildBeanContextChild​(

Object

child)

Gets the BeanContextChild (if any) of the specified child

fireChildrenAdded

```java
protected final void fireChildrenAdded​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

---

#### fireChildrenAdded

protected final void fireChildrenAdded​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

fireChildrenRemoved

```java
protected final void fireChildrenRemoved​(
BeanContextMembershipEvent
bcme)
```

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

**Parameters:** bcme

- the event to fire

---

#### fireChildrenRemoved

protected final void fireChildrenRemoved​(

BeanContextMembershipEvent

bcme)

Fire a BeanContextshipEvent on the BeanContextMembershipListener interface

initialize

```java
protected void initialize()
```

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

This class uses this method to instantiate inner class listeners used
to monitor PropertyChange and VetoableChange events on children.

subclasses may envelope this method to add their own initialization
behavior

---

#### initialize

protected void initialize()

protected method called from constructor and readObject to initialize
transient state of BeanContextSupport instance.

This class uses this method to instantiate inner class listeners used
to monitor PropertyChange and VetoableChange events on children.

subclasses may envelope this method to add their own initialization
behavior

copyChildren

```java
protected final
Object
[] copyChildren()
```

Gets a copy of the this BeanContext's children.

**Returns:** a copy of the current nested children

---

#### copyChildren

protected final

Object

[] copyChildren()

Gets a copy of the this BeanContext's children.

classEquals

```java
protected static final boolean classEquals​(
Class
<?> first,

Class
<?> second)
```

Tests to see if two class objects,
or their names are equal.

**Parameters:** first

- the first object
**Parameters:** second

- the second object
**Returns:** true if equal, false if not

---

#### classEquals

protected static final boolean classEquals​(

Class

<?> first,

Class

<?> second)

Tests to see if two class objects,
or their names are equal.

---

