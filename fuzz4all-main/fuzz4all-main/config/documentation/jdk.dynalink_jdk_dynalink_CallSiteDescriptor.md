# Class CallSiteDescriptor

**Source:** `jdk.dynalink\jdk\dynalink\CallSiteDescriptor.html`

### Class Description

```java
public class
CallSiteDescriptor

extends
SecureLookupSupplier
```

Call site descriptors contain all the information necessary for linking a
call site. This information is normally passed as parameters to bootstrap
methods and consists of the

MethodHandles.Lookup

object on the caller
class in which the call site occurs, the dynamic operation at the call
site, and the method type of the call site.

CallSiteDescriptor

objects are used in Dynalink to capture and store these parameters for
subsequent use by the

DynamicLinker

.

The constructors of built-in

RelinkableCallSite

implementations all
take a call site descriptor.

Call site descriptors must be immutable. You can use this class as-is or you
can subclass it, especially if you need to add further information to the
descriptors (typically, values passed in additional parameters to the
bootstrap method. Since the descriptors must be immutable, you can set up a
cache for equivalent descriptors to have the call sites share them.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

---

### Field Details

*No entries found.*

### Constructor Details

#### public CallSiteDescriptor​(
MethodHandles.Lookup
lookup,

Operation
operation,

MethodType
methodType)

Creates a new call site descriptor.

**Parameters:**
- lookup

- the lookup object describing the class the call site belongs to.
When creating descriptors from a

java.lang.invoke

bootstrap method,
it should be the lookup passed to the bootstrap.
- operation

- the dynamic operation at the call site.
- methodType

- the method type of the call site. When creating
descriptors from a

java.lang.invoke

bootstrap method, it should be
the method type passed to the bootstrap.

---

### Method Details

#### public final
Operation
getOperation()

Returns the operation at the call site.

**Returns:**
- the operation at the call site.

---

#### public final
MethodType
getMethodType()

The type of the method at the call site.

**Returns:**
- type of the method at the call site.

---

#### public final
CallSiteDescriptor
changeMethodType​(
MethodType
newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.
Invokes

changeMethodTypeInternal(MethodType)

.

**Parameters:**
- newMethodType

- the new method type

**Returns:**
- a call site descriptor with changed method type.

**Throws:**
- NullPointerException

- if

newMethodType

is null.

---

#### protected
CallSiteDescriptor
changeMethodTypeInternal​(
MethodType
newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the method type in the descriptor (its class, lookup,
or operation), or returns null, an

AssertionError

will be thrown
from

changeMethodType(MethodType)

.

**Parameters:**
- newMethodType

- the new method type

**Returns:**
- a call site descriptor with the changed method type.

---

#### public final
CallSiteDescriptor
changeOperation​(
Operation
newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.
Invokes

changeOperationInternal(Operation)

.

**Parameters:**
- newOperation

- the new operation

**Returns:**
- a call site descriptor with the changed operation.

**Throws:**
- NullPointerException

- if

newOperation

is null.
- SecurityException

- if the descriptor's lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.
This is necessary as changing the operation in the call site descriptor
allows fabrication of descriptors for arbitrary operations with the lookup.

---

#### protected
CallSiteDescriptor
changeOperationInternal​(
Operation
newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the operation in the descriptor (its class, lookup,
or method type), or returns null, an

AssertionError

will be thrown
from

changeOperation(Operation)

.

**Parameters:**
- newOperation

- the new operation

**Returns:**
- a call site descriptor with the changed operation.

---

#### public boolean equals​(
Object
obj)

Returns true if this call site descriptor is equal to the passed object.
It is considered equal if the other object is of the exact same class,
their operations and method types are equal, and their lookups have the
same

MethodHandles.Lookup.lookupClass()

and

MethodHandles.Lookup.lookupModes()

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- value-based hash code for this call site descriptor.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class CallSiteDescriptor

java.lang.Object

- jdk.dynalink.SecureLookupSupplier
- - jdk.dynalink.CallSiteDescriptor

jdk.dynalink.SecureLookupSupplier

- jdk.dynalink.CallSiteDescriptor

jdk.dynalink.CallSiteDescriptor

```java
public class
CallSiteDescriptor

extends
SecureLookupSupplier
```

Call site descriptors contain all the information necessary for linking a
call site. This information is normally passed as parameters to bootstrap
methods and consists of the

MethodHandles.Lookup

object on the caller
class in which the call site occurs, the dynamic operation at the call
site, and the method type of the call site.

CallSiteDescriptor

objects are used in Dynalink to capture and store these parameters for
subsequent use by the

DynamicLinker

.

The constructors of built-in

RelinkableCallSite

implementations all
take a call site descriptor.

Call site descriptors must be immutable. You can use this class as-is or you
can subclass it, especially if you need to add further information to the
descriptors (typically, values passed in additional parameters to the
bootstrap method. Since the descriptors must be immutable, you can set up a
cache for equivalent descriptors to have the call sites share them.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

public class

CallSiteDescriptor

extends

SecureLookupSupplier

Call site descriptors contain all the information necessary for linking a
call site. This information is normally passed as parameters to bootstrap
methods and consists of the

MethodHandles.Lookup

object on the caller
class in which the call site occurs, the dynamic operation at the call
site, and the method type of the call site.

CallSiteDescriptor

objects are used in Dynalink to capture and store these parameters for
subsequent use by the

DynamicLinker

.

The constructors of built-in

RelinkableCallSite

implementations all
take a call site descriptor.

Call site descriptors must be immutable. You can use this class as-is or you
can subclass it, especially if you need to add further information to the
descriptors (typically, values passed in additional parameters to the
bootstrap method. Since the descriptors must be immutable, you can set up a
cache for equivalent descriptors to have the call sites share them.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

The constructors of built-in

RelinkableCallSite

implementations all
take a call site descriptor.

Call site descriptors must be immutable. You can use this class as-is or you
can subclass it, especially if you need to add further information to the
descriptors (typically, values passed in additional parameters to the
bootstrap method. Since the descriptors must be immutable, you can set up a
cache for equivalent descriptors to have the call sites share them.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

Call site descriptors must be immutable. You can use this class as-is or you
can subclass it, especially if you need to add further information to the
descriptors (typically, values passed in additional parameters to the
bootstrap method. Since the descriptors must be immutable, you can set up a
cache for equivalent descriptors to have the call sites share them.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

The class extends

SecureLookupSupplier

for security-checked access to
the

MethodHandles.Lookup

object it carries. This lookup should be used
to find method handles to set as targets of the call site described by this
descriptor.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class jdk.dynalink.

SecureLookupSupplier

GET_LOOKUP_PERMISSION_NAME

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CallSiteDescriptor

​(

MethodHandles.Lookup

lookup,

Operation

operation,

MethodType

methodType)

Creates a new call site descriptor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CallSiteDescriptor

changeMethodType

​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.

protected

CallSiteDescriptor

changeMethodTypeInternal

​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.

CallSiteDescriptor

changeOperation

​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.

protected

CallSiteDescriptor

changeOperationInternal

​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.

boolean

equals

​(

Object

obj)

Returns true if this call site descriptor is equal to the passed object.

MethodType

getMethodType

()

The type of the method at the call site.

Operation

getOperation

()

Returns the operation at the call site.

int

hashCode

()

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

String

toString

()

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

- Methods declared in class jdk.dynalink.

SecureLookupSupplier

getLookup

,

getLookupPrivileged

- Methods declared in class java.lang.

Object

clone

,

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

- Fields declared in class jdk.dynalink.

SecureLookupSupplier

GET_LOOKUP_PERMISSION_NAME

---

#### Field Summary

Fields declared in class jdk.dynalink.

SecureLookupSupplier

GET_LOOKUP_PERMISSION_NAME

---

#### Fields declared in class jdk.dynalink. SecureLookupSupplier

Constructor Summary

Constructors

Constructor

Description

CallSiteDescriptor

​(

MethodHandles.Lookup

lookup,

Operation

operation,

MethodType

methodType)

Creates a new call site descriptor.

---

#### Constructor Summary

Creates a new call site descriptor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CallSiteDescriptor

changeMethodType

​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.

protected

CallSiteDescriptor

changeMethodTypeInternal

​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.

CallSiteDescriptor

changeOperation

​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.

protected

CallSiteDescriptor

changeOperationInternal

​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.

boolean

equals

​(

Object

obj)

Returns true if this call site descriptor is equal to the passed object.

MethodType

getMethodType

()

The type of the method at the call site.

Operation

getOperation

()

Returns the operation at the call site.

int

hashCode

()

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

String

toString

()

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

- Methods declared in class jdk.dynalink.

SecureLookupSupplier

getLookup

,

getLookupPrivileged

- Methods declared in class java.lang.

Object

clone

,

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

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.

Returns true if this call site descriptor is equal to the passed object.

The type of the method at the call site.

Returns the operation at the call site.

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

Methods declared in class jdk.dynalink.

SecureLookupSupplier

getLookup

,

getLookupPrivileged

---

#### Methods declared in class jdk.dynalink. SecureLookupSupplier

Methods declared in class java.lang.

Object

clone

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CallSiteDescriptor

```java
public CallSiteDescriptor​(
MethodHandles.Lookup
lookup,

Operation
operation,

MethodType
methodType)
```

Creates a new call site descriptor.

**Parameters:** lookup

- the lookup object describing the class the call site belongs to.
When creating descriptors from a

java.lang.invoke

bootstrap method,
it should be the lookup passed to the bootstrap.
**Parameters:** operation

- the dynamic operation at the call site.
**Parameters:** methodType

- the method type of the call site. When creating
descriptors from a

java.lang.invoke

bootstrap method, it should be
the method type passed to the bootstrap.

============ METHOD DETAIL ==========

- Method Detail

- getOperation

```java
public final
Operation
getOperation()
```

Returns the operation at the call site.

**Returns:** the operation at the call site.

- getMethodType

```java
public final
MethodType
getMethodType()
```

The type of the method at the call site.

**Returns:** type of the method at the call site.

- changeMethodType

```java
public final
CallSiteDescriptor
changeMethodType​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.
Invokes

changeMethodTypeInternal(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with changed method type.
**Throws:** NullPointerException

- if

newMethodType

is null.

- changeMethodTypeInternal

```java
protected
CallSiteDescriptor
changeMethodTypeInternal​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the method type in the descriptor (its class, lookup,
or operation), or returns null, an

AssertionError

will be thrown
from

changeMethodType(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with the changed method type.

- changeOperation

```java
public final
CallSiteDescriptor
changeOperation​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.
Invokes

changeOperationInternal(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.
**Throws:** NullPointerException

- if

newOperation

is null.
**Throws:** SecurityException

- if the descriptor's lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.
This is necessary as changing the operation in the call site descriptor
allows fabrication of descriptors for arbitrary operations with the lookup.

- changeOperationInternal

```java
protected
CallSiteDescriptor
changeOperationInternal​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the operation in the descriptor (its class, lookup,
or method type), or returns null, an

AssertionError

will be thrown
from

changeOperation(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if this call site descriptor is equal to the passed object.
It is considered equal if the other object is of the exact same class,
their operations and method types are equal, and their lookups have the
same

MethodHandles.Lookup.lookupClass()

and

MethodHandles.Lookup.lookupModes()

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

**Overrides:** hashCode

in class

Object
**Returns:** value-based hash code for this call site descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- CallSiteDescriptor

```java
public CallSiteDescriptor​(
MethodHandles.Lookup
lookup,

Operation
operation,

MethodType
methodType)
```

Creates a new call site descriptor.

**Parameters:** lookup

- the lookup object describing the class the call site belongs to.
When creating descriptors from a

java.lang.invoke

bootstrap method,
it should be the lookup passed to the bootstrap.
**Parameters:** operation

- the dynamic operation at the call site.
**Parameters:** methodType

- the method type of the call site. When creating
descriptors from a

java.lang.invoke

bootstrap method, it should be
the method type passed to the bootstrap.

---

#### Constructor Detail

CallSiteDescriptor

```java
public CallSiteDescriptor​(
MethodHandles.Lookup
lookup,

Operation
operation,

MethodType
methodType)
```

Creates a new call site descriptor.

**Parameters:** lookup

- the lookup object describing the class the call site belongs to.
When creating descriptors from a

java.lang.invoke

bootstrap method,
it should be the lookup passed to the bootstrap.
**Parameters:** operation

- the dynamic operation at the call site.
**Parameters:** methodType

- the method type of the call site. When creating
descriptors from a

java.lang.invoke

bootstrap method, it should be
the method type passed to the bootstrap.

---

#### CallSiteDescriptor

public CallSiteDescriptor​(

MethodHandles.Lookup

lookup,

Operation

operation,

MethodType

methodType)

Creates a new call site descriptor.

Method Detail

- getOperation

```java
public final
Operation
getOperation()
```

Returns the operation at the call site.

**Returns:** the operation at the call site.

- getMethodType

```java
public final
MethodType
getMethodType()
```

The type of the method at the call site.

**Returns:** type of the method at the call site.

- changeMethodType

```java
public final
CallSiteDescriptor
changeMethodType​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.
Invokes

changeMethodTypeInternal(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with changed method type.
**Throws:** NullPointerException

- if

newMethodType

is null.

- changeMethodTypeInternal

```java
protected
CallSiteDescriptor
changeMethodTypeInternal​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the method type in the descriptor (its class, lookup,
or operation), or returns null, an

AssertionError

will be thrown
from

changeMethodType(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with the changed method type.

- changeOperation

```java
public final
CallSiteDescriptor
changeOperation​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.
Invokes

changeOperationInternal(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.
**Throws:** NullPointerException

- if

newOperation

is null.
**Throws:** SecurityException

- if the descriptor's lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.
This is necessary as changing the operation in the call site descriptor
allows fabrication of descriptors for arbitrary operations with the lookup.

- changeOperationInternal

```java
protected
CallSiteDescriptor
changeOperationInternal​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the operation in the descriptor (its class, lookup,
or method type), or returns null, an

AssertionError

will be thrown
from

changeOperation(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if this call site descriptor is equal to the passed object.
It is considered equal if the other object is of the exact same class,
their operations and method types are equal, and their lookups have the
same

MethodHandles.Lookup.lookupClass()

and

MethodHandles.Lookup.lookupModes()

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

**Overrides:** hashCode

in class

Object
**Returns:** value-based hash code for this call site descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getOperation

```java
public final
Operation
getOperation()
```

Returns the operation at the call site.

**Returns:** the operation at the call site.

---

#### getOperation

public final

Operation

getOperation()

Returns the operation at the call site.

getMethodType

```java
public final
MethodType
getMethodType()
```

The type of the method at the call site.

**Returns:** type of the method at the call site.

---

#### getMethodType

public final

MethodType

getMethodType()

The type of the method at the call site.

changeMethodType

```java
public final
CallSiteDescriptor
changeMethodType​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.
Invokes

changeMethodTypeInternal(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with changed method type.
**Throws:** NullPointerException

- if

newMethodType

is null.

---

#### changeMethodType

public final

CallSiteDescriptor

changeMethodType​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor.
Invokes

changeMethodTypeInternal(MethodType)

.

changeMethodTypeInternal

```java
protected
CallSiteDescriptor
changeMethodTypeInternal​(
MethodType
newMethodType)
```

Finds or creates a call site descriptor that only differs in its
method type from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the method type in the descriptor (its class, lookup,
or operation), or returns null, an

AssertionError

will be thrown
from

changeMethodType(MethodType)

.

**Parameters:** newMethodType

- the new method type
**Returns:** a call site descriptor with the changed method type.

---

#### changeMethodTypeInternal

protected

CallSiteDescriptor

changeMethodTypeInternal​(

MethodType

newMethodType)

Finds or creates a call site descriptor that only differs in its
method type from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the method type in the descriptor (its class, lookup,
or operation), or returns null, an

AssertionError

will be thrown
from

changeMethodType(MethodType)

.

changeOperation

```java
public final
CallSiteDescriptor
changeOperation​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.
Invokes

changeOperationInternal(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.
**Throws:** NullPointerException

- if

newOperation

is null.
**Throws:** SecurityException

- if the descriptor's lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.
This is necessary as changing the operation in the call site descriptor
allows fabrication of descriptors for arbitrary operations with the lookup.

---

#### changeOperation

public final

CallSiteDescriptor

changeOperation​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor.
Invokes

changeOperationInternal(Operation)

.

changeOperationInternal

```java
protected
CallSiteDescriptor
changeOperationInternal​(
Operation
newOperation)
```

Finds or creates a call site descriptor that only differs in its
operation from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the operation in the descriptor (its class, lookup,
or method type), or returns null, an

AssertionError

will be thrown
from

changeOperation(Operation)

.

**Parameters:** newOperation

- the new operation
**Returns:** a call site descriptor with the changed operation.

---

#### changeOperationInternal

protected

CallSiteDescriptor

changeOperationInternal​(

Operation

newOperation)

Finds or creates a call site descriptor that only differs in its
operation from this descriptor. Subclasses must override this method
to return an object of their exact class. If an overridden method changes
something other than the operation in the descriptor (its class, lookup,
or method type), or returns null, an

AssertionError

will be thrown
from

changeOperation(Operation)

.

equals

```java
public boolean equals​(
Object
obj)
```

Returns true if this call site descriptor is equal to the passed object.
It is considered equal if the other object is of the exact same class,
their operations and method types are equal, and their lookups have the
same

MethodHandles.Lookup.lookupClass()

and

MethodHandles.Lookup.lookupModes()

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns true if this call site descriptor is equal to the passed object.
It is considered equal if the other object is of the exact same class,
their operations and method types are equal, and their lookups have the
same

MethodHandles.Lookup.lookupClass()

and

MethodHandles.Lookup.lookupModes()

.

hashCode

```java
public int hashCode()
```

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

**Overrides:** hashCode

in class

Object
**Returns:** value-based hash code for this call site descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a value-based hash code of this call site descriptor computed
from its operation, method type, and lookup object's lookup class and
lookup modes.

toString

```java
public
String
toString()
```

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representation of this call site descriptor, of the
format

name(parameterTypes)returnType@lookup

.

---

