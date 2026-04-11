# Class Reference

**Source:** `java.naming\javax\naming\Reference.html`

### Class Description

```java
public class
Reference

extends
Object

implements
Cloneable
,
Serializable
```

This class represents a reference to an object that is found outside of
the naming/directory system.

Reference provides a way of recording address information about
objects which themselves are not directly bound to the naming/directory system.

A Reference consists of an ordered list of addresses and class information
about the object being referenced.
Each address in the list identifies a communications endpoint
for the same conceptual object. The "communications endpoint"
is information that indicates how to contact the object. It could
be, for example, a network address, a location in memory on the
local machine, another process on the same machine, etc.
The order of the addresses in the list may be of significance
to object factories that interpret the reference.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### protected
String
className

Contains the fully-qualified name of the class of the object to which
this Reference refers.

**See Also:**
- Class.getName()

---

#### protected
Vector
<
RefAddr
> addrs

Contains the addresses contained in this Reference.
Initialized by constructor.

---

#### protected
String
classFactory

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.
Initialized to null.

---

#### protected
String
classFactoryLocation

Contains the location of the factory class.
Initialized to null.

---

### Constructor Details

#### public Reference​(
String
className)

Constructs a new reference for an object with class name 'className'.
Class factory and class factory location are set to null.
The newly created reference contains zero addresses.

**Parameters:**
- className

- The non-null class name of the object to which
this reference refers.

---

#### public Reference​(
String
className,

RefAddr
addr)

Constructs a new reference for an object with class name 'className' and
an address.
Class factory and class factory location are set to null.

**Parameters:**
- className

- The non-null class name of the object to
which this reference refers.
- addr

- The non-null address of the object.

---

#### public Reference​(
String
className,

String
factory,

String
factoryLocation)

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

**Parameters:**
- className

- The non-null class name of the object to which
this reference refers.
- factory

- The possibly null class name of the object's factory.
- factoryLocation

- The possibly null location from which to load
the factory (e.g. URL)

**See Also:**
- ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### public Reference​(
String
className,

RefAddr
addr,

String
factory,

String
factoryLocation)

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

**Parameters:**
- className

- The non-null class name of the object to
which this reference refers.
- factory

- The possibly null class name of the object's factory.
- factoryLocation

- The possibly null location from which
to load the factory (e.g. URL)
- addr

- The non-null address of the object.

**See Also:**
- ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

### Method Details

#### public
String
getClassName()

Retrieves the class name of the object to which this reference refers.

**Returns:**
- The non-null fully-qualified class name of the object.
(e.g. "java.lang.String")

---

#### public
String
getFactoryClassName()

Retrieves the class name of the factory of the object
to which this reference refers.

**Returns:**
- The possibly null fully-qualified class name of the factory.
(e.g. "java.lang.String")

---

#### public
String
getFactoryClassLocation()

Retrieves the location of the factory of the object
to which this reference refers.
If it is a codebase, then it is an ordered list of URLs,
separated by spaces, listing locations from where the factory
class definition should be loaded.

**Returns:**
- The possibly null string containing the
location for loading in the factory's class.

---

#### public
RefAddr
get​(
String
addrType)

Retrieves the first address that has the address type 'addrType'.
String.compareTo() is used to test the equality of the address types.

**Parameters:**
- addrType

- The non-null address type for which to find the address.

**Returns:**
- The address in this reference with address type 'addrType';
null if no such address exists.

---

#### public
RefAddr
get​(int posn)

Retrieves the address at index posn.

**Parameters:**
- posn

- The index of the address to retrieve.

**Returns:**
- The address at the 0-based index posn. It must be in the
range [0,getAddressCount()).

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### public
Enumeration
<
RefAddr
> getAll()

Retrieves an enumeration of the addresses in this reference.
When addresses are added, changed or removed from this reference,
its effects on this enumeration are undefined.

**Returns:**
- An non-null enumeration of the addresses
(

RefAddr

) in this reference.
If this reference has zero addresses, an enumeration with
zero elements is returned.

---

#### public int size()

Retrieves the number of addresses in this reference.

**Returns:**
- The nonnegative number of addresses in this reference.

---

#### public void add​(
RefAddr
addr)

Adds an address to the end of the list of addresses.

**Parameters:**
- addr

- The non-null address to add.

---

#### public void add​(int posn,

RefAddr
addr)

Adds an address to the list of addresses at index posn.
All addresses at index posn or greater are shifted up
the list by one (away from index 0).

**Parameters:**
- posn

- The 0-based index of the list to insert addr.
- addr

- The non-null address to add.

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### public
Object
remove​(int posn)

Deletes the address at index posn from the list of addresses.
All addresses at index greater than posn are shifted down
the list by one (towards index 0).

**Parameters:**
- posn

- The 0-based index of in address to delete.

**Returns:**
- The address removed.

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### public void clear()

Deletes all addresses from this reference.

---

#### public boolean equals​(
Object
obj)

Determines whether obj is a reference with the same addresses
(in same order) as this reference.
The addresses are checked using RefAddr.equals().
In addition to having the same addresses, the Reference also needs to
have the same class name as this reference.
The class factory and class factory location are not checked.
If obj is null or not an instance of Reference, null is returned.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The possibly null object to check.

**Returns:**
- true if obj is equal to this reference; false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Computes the hash code of this reference.
The hash code is the sum of the hash code of its addresses.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash code of this reference as an int.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Generates the string representation of this reference.
The string consists of the class name to which this reference refers,
and the string representation of each of its addresses.
This representation is intended for display only and not to be parsed.

**Overrides:**
- toString

in class

Object

**Returns:**
- The non-null string representation of this reference.

---

#### public
Object
clone()

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.
Changes to the newly created copy does not affect this Reference
and vice versa.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Reference

java.lang.Object

- javax.naming.Reference

javax.naming.Reference

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** LinkRef

```java
public class
Reference

extends
Object

implements
Cloneable
,
Serializable
```

This class represents a reference to an object that is found outside of
the naming/directory system.

Reference provides a way of recording address information about
objects which themselves are not directly bound to the naming/directory system.

A Reference consists of an ordered list of addresses and class information
about the object being referenced.
Each address in the list identifies a communications endpoint
for the same conceptual object. The "communications endpoint"
is information that indicates how to contact the object. It could
be, for example, a network address, a location in memory on the
local machine, another process on the same machine, etc.
The order of the addresses in the list may be of significance
to object factories that interpret the reference.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

**Since:** 1.3
**See Also:** RefAddr

,

StringRefAddr

,

BinaryRefAddr

,

Serialized Form

public class

Reference

extends

Object

implements

Cloneable

,

Serializable

This class represents a reference to an object that is found outside of
the naming/directory system.

Reference provides a way of recording address information about
objects which themselves are not directly bound to the naming/directory system.

A Reference consists of an ordered list of addresses and class information
about the object being referenced.
Each address in the list identifies a communications endpoint
for the same conceptual object. The "communications endpoint"
is information that indicates how to contact the object. It could
be, for example, a network address, a location in memory on the
local machine, another process on the same machine, etc.
The order of the addresses in the list may be of significance
to object factories that interpret the reference.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

Reference provides a way of recording address information about
objects which themselves are not directly bound to the naming/directory system.

A Reference consists of an ordered list of addresses and class information
about the object being referenced.
Each address in the list identifies a communications endpoint
for the same conceptual object. The "communications endpoint"
is information that indicates how to contact the object. It could
be, for example, a network address, a location in memory on the
local machine, another process on the same machine, etc.
The order of the addresses in the list may be of significance
to object factories that interpret the reference.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

A Reference consists of an ordered list of addresses and class information
about the object being referenced.
Each address in the list identifies a communications endpoint
for the same conceptual object. The "communications endpoint"
is information that indicates how to contact the object. It could
be, for example, a network address, a location in memory on the
local machine, another process on the same machine, etc.
The order of the addresses in the list may be of significance
to object factories that interpret the reference.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

Multiple addresses may arise for
various reasons, such as replication or the object offering interfaces
over more than one communication mechanism. The addresses are indexed
starting with zero.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

A Reference also contains information to assist in creating an instance
of the object to which this Reference refers. It contains the class name
of that object, and the class name and location of the factory to be used
to create the object.
The class factory location is a space-separated list of URLs representing
the class path used to load the factory. When the factory class (or
any class or resource upon which it depends) needs to be loaded,
each URL is used (in order) to attempt to load the class.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

A Reference instance is not synchronized against concurrent access by multiple
threads. Threads that need to access a single Reference concurrently should
synchronize amongst themselves and provide the necessary locking.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

RefAddr

>

addrs

Contains the addresses contained in this Reference.

protected

String

classFactory

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.

protected

String

classFactoryLocation

Contains the location of the factory class.

protected

String

className

Contains the fully-qualified name of the class of the object to which
this Reference refers.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Reference

​(

String

className)

Constructs a new reference for an object with class name 'className'.

Reference

​(

String

className,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

Reference

​(

String

className,

RefAddr

addr)

Constructs a new reference for an object with class name 'className' and
an address.

Reference

​(

String

className,

RefAddr

addr,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int posn,

RefAddr

addr)

Adds an address to the list of addresses at index posn.

void

add

​(

RefAddr

addr)

Adds an address to the end of the list of addresses.

void

clear

()

Deletes all addresses from this reference.

Object

clone

()

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.

boolean

equals

​(

Object

obj)

Determines whether obj is a reference with the same addresses
(in same order) as this reference.

RefAddr

get

​(int posn)

Retrieves the address at index posn.

RefAddr

get

​(

String

addrType)

Retrieves the first address that has the address type 'addrType'.

Enumeration

<

RefAddr

>

getAll

()

Retrieves an enumeration of the addresses in this reference.

String

getClassName

()

Retrieves the class name of the object to which this reference refers.

String

getFactoryClassLocation

()

Retrieves the location of the factory of the object
to which this reference refers.

String

getFactoryClassName

()

Retrieves the class name of the factory of the object
to which this reference refers.

int

hashCode

()

Computes the hash code of this reference.

Object

remove

​(int posn)

Deletes the address at index posn from the list of addresses.

int

size

()

Retrieves the number of addresses in this reference.

String

toString

()

Generates the string representation of this reference.

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

Vector

<

RefAddr

>

addrs

Contains the addresses contained in this Reference.

protected

String

classFactory

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.

protected

String

classFactoryLocation

Contains the location of the factory class.

protected

String

className

Contains the fully-qualified name of the class of the object to which
this Reference refers.

---

#### Field Summary

Contains the addresses contained in this Reference.

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.

Contains the location of the factory class.

Contains the fully-qualified name of the class of the object to which
this Reference refers.

Constructor Summary

Constructors

Constructor

Description

Reference

​(

String

className)

Constructs a new reference for an object with class name 'className'.

Reference

​(

String

className,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

Reference

​(

String

className,

RefAddr

addr)

Constructs a new reference for an object with class name 'className' and
an address.

Reference

​(

String

className,

RefAddr

addr,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

---

#### Constructor Summary

Constructs a new reference for an object with class name 'className'.

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

Constructs a new reference for an object with class name 'className' and
an address.

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(int posn,

RefAddr

addr)

Adds an address to the list of addresses at index posn.

void

add

​(

RefAddr

addr)

Adds an address to the end of the list of addresses.

void

clear

()

Deletes all addresses from this reference.

Object

clone

()

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.

boolean

equals

​(

Object

obj)

Determines whether obj is a reference with the same addresses
(in same order) as this reference.

RefAddr

get

​(int posn)

Retrieves the address at index posn.

RefAddr

get

​(

String

addrType)

Retrieves the first address that has the address type 'addrType'.

Enumeration

<

RefAddr

>

getAll

()

Retrieves an enumeration of the addresses in this reference.

String

getClassName

()

Retrieves the class name of the object to which this reference refers.

String

getFactoryClassLocation

()

Retrieves the location of the factory of the object
to which this reference refers.

String

getFactoryClassName

()

Retrieves the class name of the factory of the object
to which this reference refers.

int

hashCode

()

Computes the hash code of this reference.

Object

remove

​(int posn)

Deletes the address at index posn from the list of addresses.

int

size

()

Retrieves the number of addresses in this reference.

String

toString

()

Generates the string representation of this reference.

- Methods declared in class java.lang.

Object

finalize

,

getClass

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

Adds an address to the list of addresses at index posn.

Adds an address to the end of the list of addresses.

Deletes all addresses from this reference.

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.

Determines whether obj is a reference with the same addresses
(in same order) as this reference.

Retrieves the address at index posn.

Retrieves the first address that has the address type 'addrType'.

Retrieves an enumeration of the addresses in this reference.

Retrieves the class name of the object to which this reference refers.

Retrieves the location of the factory of the object
to which this reference refers.

Retrieves the class name of the factory of the object
to which this reference refers.

Computes the hash code of this reference.

Deletes the address at index posn from the list of addresses.

Retrieves the number of addresses in this reference.

Generates the string representation of this reference.

Methods declared in class java.lang.

Object

finalize

,

getClass

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

- className

```java
protected
String
className
```

Contains the fully-qualified name of the class of the object to which
this Reference refers.

**See Also:** Class.getName()

- addrs

```java
protected
Vector
<
RefAddr
> addrs
```

Contains the addresses contained in this Reference.
Initialized by constructor.

- classFactory

```java
protected
String
classFactory
```

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.
Initialized to null.

- classFactoryLocation

```java
protected
String
classFactoryLocation
```

Contains the location of the factory class.
Initialized to null.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Reference

```java
public Reference​(
String
className)
```

Constructs a new reference for an object with class name 'className'.
Class factory and class factory location are set to null.
The newly created reference contains zero addresses.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.

- Reference

```java
public Reference​(
String
className,

RefAddr
addr)
```

Constructs a new reference for an object with class name 'className' and
an address.
Class factory and class factory location are set to null.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** addr

- The non-null address of the object.

- Reference

```java
public Reference​(
String
className,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which to load
the factory (e.g. URL)
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- Reference

```java
public Reference​(
String
className,

RefAddr
addr,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which
to load the factory (e.g. URL)
**Parameters:** addr

- The non-null address of the object.
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object to which this reference refers.

**Returns:** The non-null fully-qualified class name of the object.
(e.g. "java.lang.String")

- getFactoryClassName

```java
public
String
getFactoryClassName()
```

Retrieves the class name of the factory of the object
to which this reference refers.

**Returns:** The possibly null fully-qualified class name of the factory.
(e.g. "java.lang.String")

- getFactoryClassLocation

```java
public
String
getFactoryClassLocation()
```

Retrieves the location of the factory of the object
to which this reference refers.
If it is a codebase, then it is an ordered list of URLs,
separated by spaces, listing locations from where the factory
class definition should be loaded.

**Returns:** The possibly null string containing the
location for loading in the factory's class.

- get

```java
public
RefAddr
get​(
String
addrType)
```

Retrieves the first address that has the address type 'addrType'.
String.compareTo() is used to test the equality of the address types.

**Parameters:** addrType

- The non-null address type for which to find the address.
**Returns:** The address in this reference with address type 'addrType';
null if no such address exists.

- get

```java
public
RefAddr
get​(int posn)
```

Retrieves the address at index posn.

**Parameters:** posn

- The index of the address to retrieve.
**Returns:** The address at the 0-based index posn. It must be in the
range [0,getAddressCount()).
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- getAll

```java
public
Enumeration
<
RefAddr
> getAll()
```

Retrieves an enumeration of the addresses in this reference.
When addresses are added, changed or removed from this reference,
its effects on this enumeration are undefined.

**Returns:** An non-null enumeration of the addresses
(

RefAddr

) in this reference.
If this reference has zero addresses, an enumeration with
zero elements is returned.

- size

```java
public int size()
```

Retrieves the number of addresses in this reference.

**Returns:** The nonnegative number of addresses in this reference.

- add

```java
public void add​(
RefAddr
addr)
```

Adds an address to the end of the list of addresses.

**Parameters:** addr

- The non-null address to add.

- add

```java
public void add​(int posn,

RefAddr
addr)
```

Adds an address to the list of addresses at index posn.
All addresses at index posn or greater are shifted up
the list by one (away from index 0).

**Parameters:** posn

- The 0-based index of the list to insert addr.
**Parameters:** addr

- The non-null address to add.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- remove

```java
public
Object
remove​(int posn)
```

Deletes the address at index posn from the list of addresses.
All addresses at index greater than posn are shifted down
the list by one (towards index 0).

**Parameters:** posn

- The 0-based index of in address to delete.
**Returns:** The address removed.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- clear

```java
public void clear()
```

Deletes all addresses from this reference.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is a reference with the same addresses
(in same order) as this reference.
The addresses are checked using RefAddr.equals().
In addition to having the same addresses, the Reference also needs to
have the same class name as this reference.
The class factory and class factory location are not checked.
If obj is null or not an instance of Reference, null is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this reference; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash code of this reference.
The hash code is the sum of the hash code of its addresses.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code of this reference as an int.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Generates the string representation of this reference.
The string consists of the class name to which this reference refers,
and the string representation of each of its addresses.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this reference.

- clone

```java
public
Object
clone()
```

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.
Changes to the newly created copy does not affect this Reference
and vice versa.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

Field Detail

- className

```java
protected
String
className
```

Contains the fully-qualified name of the class of the object to which
this Reference refers.

**See Also:** Class.getName()

- addrs

```java
protected
Vector
<
RefAddr
> addrs
```

Contains the addresses contained in this Reference.
Initialized by constructor.

- classFactory

```java
protected
String
classFactory
```

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.
Initialized to null.

- classFactoryLocation

```java
protected
String
classFactoryLocation
```

Contains the location of the factory class.
Initialized to null.

---

#### Field Detail

className

```java
protected
String
className
```

Contains the fully-qualified name of the class of the object to which
this Reference refers.

**See Also:** Class.getName()

---

#### className

protected

String

className

Contains the fully-qualified name of the class of the object to which
this Reference refers.

addrs

```java
protected
Vector
<
RefAddr
> addrs
```

Contains the addresses contained in this Reference.
Initialized by constructor.

---

#### addrs

protected

Vector

<

RefAddr

> addrs

Contains the addresses contained in this Reference.
Initialized by constructor.

classFactory

```java
protected
String
classFactory
```

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.
Initialized to null.

---

#### classFactory

protected

String

classFactory

Contains the name of the factory class for creating
an instance of the object to which this Reference refers.
Initialized to null.

classFactoryLocation

```java
protected
String
classFactoryLocation
```

Contains the location of the factory class.
Initialized to null.

---

#### classFactoryLocation

protected

String

classFactoryLocation

Contains the location of the factory class.
Initialized to null.

Constructor Detail

- Reference

```java
public Reference​(
String
className)
```

Constructs a new reference for an object with class name 'className'.
Class factory and class factory location are set to null.
The newly created reference contains zero addresses.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.

- Reference

```java
public Reference​(
String
className,

RefAddr
addr)
```

Constructs a new reference for an object with class name 'className' and
an address.
Class factory and class factory location are set to null.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** addr

- The non-null address of the object.

- Reference

```java
public Reference​(
String
className,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which to load
the factory (e.g. URL)
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- Reference

```java
public Reference​(
String
className,

RefAddr
addr,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which
to load the factory (e.g. URL)
**Parameters:** addr

- The non-null address of the object.
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### Constructor Detail

Reference

```java
public Reference​(
String
className)
```

Constructs a new reference for an object with class name 'className'.
Class factory and class factory location are set to null.
The newly created reference contains zero addresses.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.

---

#### Reference

public Reference​(

String

className)

Constructs a new reference for an object with class name 'className'.
Class factory and class factory location are set to null.
The newly created reference contains zero addresses.

Reference

```java
public Reference​(
String
className,

RefAddr
addr)
```

Constructs a new reference for an object with class name 'className' and
an address.
Class factory and class factory location are set to null.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** addr

- The non-null address of the object.

---

#### Reference

public Reference​(

String

className,

RefAddr

addr)

Constructs a new reference for an object with class name 'className' and
an address.
Class factory and class factory location are set to null.

Reference

```java
public Reference​(
String
className,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

**Parameters:** className

- The non-null class name of the object to which
this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which to load
the factory (e.g. URL)
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### Reference

public Reference​(

String

className,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
and the class name and location of the object's factory.

Reference

```java
public Reference​(
String
className,

RefAddr
addr,

String
factory,

String
factoryLocation)
```

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

**Parameters:** className

- The non-null class name of the object to
which this reference refers.
**Parameters:** factory

- The possibly null class name of the object's factory.
**Parameters:** factoryLocation

- The possibly null location from which
to load the factory (e.g. URL)
**Parameters:** addr

- The non-null address of the object.
**See Also:** ObjectFactory

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### Reference

public Reference​(

String

className,

RefAddr

addr,

String

factory,

String

factoryLocation)

Constructs a new reference for an object with class name 'className',
the class name and location of the object's factory, and the address for
the object.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object to which this reference refers.

**Returns:** The non-null fully-qualified class name of the object.
(e.g. "java.lang.String")

- getFactoryClassName

```java
public
String
getFactoryClassName()
```

Retrieves the class name of the factory of the object
to which this reference refers.

**Returns:** The possibly null fully-qualified class name of the factory.
(e.g. "java.lang.String")

- getFactoryClassLocation

```java
public
String
getFactoryClassLocation()
```

Retrieves the location of the factory of the object
to which this reference refers.
If it is a codebase, then it is an ordered list of URLs,
separated by spaces, listing locations from where the factory
class definition should be loaded.

**Returns:** The possibly null string containing the
location for loading in the factory's class.

- get

```java
public
RefAddr
get​(
String
addrType)
```

Retrieves the first address that has the address type 'addrType'.
String.compareTo() is used to test the equality of the address types.

**Parameters:** addrType

- The non-null address type for which to find the address.
**Returns:** The address in this reference with address type 'addrType';
null if no such address exists.

- get

```java
public
RefAddr
get​(int posn)
```

Retrieves the address at index posn.

**Parameters:** posn

- The index of the address to retrieve.
**Returns:** The address at the 0-based index posn. It must be in the
range [0,getAddressCount()).
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- getAll

```java
public
Enumeration
<
RefAddr
> getAll()
```

Retrieves an enumeration of the addresses in this reference.
When addresses are added, changed or removed from this reference,
its effects on this enumeration are undefined.

**Returns:** An non-null enumeration of the addresses
(

RefAddr

) in this reference.
If this reference has zero addresses, an enumeration with
zero elements is returned.

- size

```java
public int size()
```

Retrieves the number of addresses in this reference.

**Returns:** The nonnegative number of addresses in this reference.

- add

```java
public void add​(
RefAddr
addr)
```

Adds an address to the end of the list of addresses.

**Parameters:** addr

- The non-null address to add.

- add

```java
public void add​(int posn,

RefAddr
addr)
```

Adds an address to the list of addresses at index posn.
All addresses at index posn or greater are shifted up
the list by one (away from index 0).

**Parameters:** posn

- The 0-based index of the list to insert addr.
**Parameters:** addr

- The non-null address to add.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- remove

```java
public
Object
remove​(int posn)
```

Deletes the address at index posn from the list of addresses.
All addresses at index greater than posn are shifted down
the list by one (towards index 0).

**Parameters:** posn

- The 0-based index of in address to delete.
**Returns:** The address removed.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

- clear

```java
public void clear()
```

Deletes all addresses from this reference.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is a reference with the same addresses
(in same order) as this reference.
The addresses are checked using RefAddr.equals().
In addition to having the same addresses, the Reference also needs to
have the same class name as this reference.
The class factory and class factory location are not checked.
If obj is null or not an instance of Reference, null is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this reference; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash code of this reference.
The hash code is the sum of the hash code of its addresses.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code of this reference as an int.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Generates the string representation of this reference.
The string consists of the class name to which this reference refers,
and the string representation of each of its addresses.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this reference.

- clone

```java
public
Object
clone()
```

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.
Changes to the newly created copy does not affect this Reference
and vice versa.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Retrieves the class name of the object to which this reference refers.

**Returns:** The non-null fully-qualified class name of the object.
(e.g. "java.lang.String")

---

#### getClassName

public

String

getClassName()

Retrieves the class name of the object to which this reference refers.

getFactoryClassName

```java
public
String
getFactoryClassName()
```

Retrieves the class name of the factory of the object
to which this reference refers.

**Returns:** The possibly null fully-qualified class name of the factory.
(e.g. "java.lang.String")

---

#### getFactoryClassName

public

String

getFactoryClassName()

Retrieves the class name of the factory of the object
to which this reference refers.

getFactoryClassLocation

```java
public
String
getFactoryClassLocation()
```

Retrieves the location of the factory of the object
to which this reference refers.
If it is a codebase, then it is an ordered list of URLs,
separated by spaces, listing locations from where the factory
class definition should be loaded.

**Returns:** The possibly null string containing the
location for loading in the factory's class.

---

#### getFactoryClassLocation

public

String

getFactoryClassLocation()

Retrieves the location of the factory of the object
to which this reference refers.
If it is a codebase, then it is an ordered list of URLs,
separated by spaces, listing locations from where the factory
class definition should be loaded.

get

```java
public
RefAddr
get​(
String
addrType)
```

Retrieves the first address that has the address type 'addrType'.
String.compareTo() is used to test the equality of the address types.

**Parameters:** addrType

- The non-null address type for which to find the address.
**Returns:** The address in this reference with address type 'addrType';
null if no such address exists.

---

#### get

public

RefAddr

get​(

String

addrType)

Retrieves the first address that has the address type 'addrType'.
String.compareTo() is used to test the equality of the address types.

get

```java
public
RefAddr
get​(int posn)
```

Retrieves the address at index posn.

**Parameters:** posn

- The index of the address to retrieve.
**Returns:** The address at the 0-based index posn. It must be in the
range [0,getAddressCount()).
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### get

public

RefAddr

get​(int posn)

Retrieves the address at index posn.

getAll

```java
public
Enumeration
<
RefAddr
> getAll()
```

Retrieves an enumeration of the addresses in this reference.
When addresses are added, changed or removed from this reference,
its effects on this enumeration are undefined.

**Returns:** An non-null enumeration of the addresses
(

RefAddr

) in this reference.
If this reference has zero addresses, an enumeration with
zero elements is returned.

---

#### getAll

public

Enumeration

<

RefAddr

> getAll()

Retrieves an enumeration of the addresses in this reference.
When addresses are added, changed or removed from this reference,
its effects on this enumeration are undefined.

size

```java
public int size()
```

Retrieves the number of addresses in this reference.

**Returns:** The nonnegative number of addresses in this reference.

---

#### size

public int size()

Retrieves the number of addresses in this reference.

add

```java
public void add​(
RefAddr
addr)
```

Adds an address to the end of the list of addresses.

**Parameters:** addr

- The non-null address to add.

---

#### add

public void add​(

RefAddr

addr)

Adds an address to the end of the list of addresses.

add

```java
public void add​(int posn,

RefAddr
addr)
```

Adds an address to the list of addresses at index posn.
All addresses at index posn or greater are shifted up
the list by one (away from index 0).

**Parameters:** posn

- The 0-based index of the list to insert addr.
**Parameters:** addr

- The non-null address to add.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### add

public void add​(int posn,

RefAddr

addr)

Adds an address to the list of addresses at index posn.
All addresses at index posn or greater are shifted up
the list by one (away from index 0).

remove

```java
public
Object
remove​(int posn)
```

Deletes the address at index posn from the list of addresses.
All addresses at index greater than posn are shifted down
the list by one (towards index 0).

**Parameters:** posn

- The 0-based index of in address to delete.
**Returns:** The address removed.
**Throws:** ArrayIndexOutOfBoundsException

- If posn not in the specified
range.

---

#### remove

public

Object

remove​(int posn)

Deletes the address at index posn from the list of addresses.
All addresses at index greater than posn are shifted down
the list by one (towards index 0).

clear

```java
public void clear()
```

Deletes all addresses from this reference.

---

#### clear

public void clear()

Deletes all addresses from this reference.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is a reference with the same addresses
(in same order) as this reference.
The addresses are checked using RefAddr.equals().
In addition to having the same addresses, the Reference also needs to
have the same class name as this reference.
The class factory and class factory location are not checked.
If obj is null or not an instance of Reference, null is returned.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to check.
**Returns:** true if obj is equal to this reference; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether obj is a reference with the same addresses
(in same order) as this reference.
The addresses are checked using RefAddr.equals().
In addition to having the same addresses, the Reference also needs to
have the same class name as this reference.
The class factory and class factory location are not checked.
If obj is null or not an instance of Reference, null is returned.

hashCode

```java
public int hashCode()
```

Computes the hash code of this reference.
The hash code is the sum of the hash code of its addresses.

**Overrides:** hashCode

in class

Object
**Returns:** A hash code of this reference as an int.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes the hash code of this reference.
The hash code is the sum of the hash code of its addresses.

toString

```java
public
String
toString()
```

Generates the string representation of this reference.
The string consists of the class name to which this reference refers,
and the string representation of each of its addresses.
This representation is intended for display only and not to be parsed.

**Overrides:** toString

in class

Object
**Returns:** The non-null string representation of this reference.

---

#### toString

public

String

toString()

Generates the string representation of this reference.
The string consists of the class name to which this reference refers,
and the string representation of each of its addresses.
This representation is intended for display only and not to be parsed.

clone

```java
public
Object
clone()
```

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.
Changes to the newly created copy does not affect this Reference
and vice versa.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Makes a copy of this reference using its class name
list of addresses, class factory name and class factory location.
Changes to the newly created copy does not affect this Reference
and vice versa.

---

