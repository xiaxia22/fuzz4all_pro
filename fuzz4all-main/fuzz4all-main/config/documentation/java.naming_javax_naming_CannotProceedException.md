# Class CannotProceedException

**Source:** `java.naming\javax\naming\CannotProceedException.html`

### Class Description

```java
public class
CannotProceedException

extends
NamingException
```

This exception is thrown to indicate that the operation reached
a point in the name where the operation cannot proceed any further.
When performing an operation on a composite name, a naming service
provider may reach a part of the name that does not belong to its
namespace. At that point, it can construct a
CannotProceedException and then invoke methods provided by
javax.naming.spi.NamingManager (such as getContinuationContext())
to locate another provider to continue the operation. If this is
not possible, this exception is raised to the caller of the
context operation.

If the program wants to handle this exception in particular, it
should catch CannotProceedException explicitly before attempting to
catch NamingException.

A CannotProceedException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
CannotProceedException should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Name
remainingNewName

Contains the remaining unresolved part of the second
"name" argument to Context.rename().
This information is necessary for
continuing the Context.rename() operation.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

**See Also:**
- getRemainingNewName()

,

setRemainingNewName(javax.naming.Name)

---

#### protected
Hashtable
<?,​?> environment

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

**See Also:**
- getEnvironment()

,

setEnvironment(java.util.Hashtable<?, ?>)

---

#### protected
Name
altName

Contains the name of the resolved object, relative
to the context

altNameCtx

. It is a composite name.
If null, then no name is specified.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

**See Also:**
- getAltName()

,

setAltName(javax.naming.Name)

,

altNameCtx

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### protected
Context
altNameCtx

Contains the context relative to which

altName

is specified. If null, then the default initial
context is implied.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

**See Also:**
- getAltNameCtx()

,

setAltNameCtx(javax.naming.Context)

,

altName

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

### Constructor Details

#### public CannotProceedException​(
String
explanation)

Constructs a new instance of CannotProceedException using an
explanation. All unspecified fields default to null.

**Parameters:**
- explanation

- A possibly null string containing additional
detail about this exception.
If null, this exception has no detail message.

**See Also:**
- Throwable.getMessage()

---

#### public CannotProceedException()

Constructs a new instance of CannotProceedException.
All fields default to null.

---

### Method Details

#### public
Hashtable
<?,​?> getEnvironment()

Retrieves the environment that was in effect when this exception
was created.

**Returns:**
- Possibly null environment property set.
null means no environment was recorded for this exception.

**See Also:**
- setEnvironment(java.util.Hashtable<?, ?>)

---

#### public void setEnvironment​(
Hashtable
<?,​?> environment)

Sets the environment that will be returned when getEnvironment()
is called.

**Parameters:**
- environment

- A possibly null environment property set.
null means no environment is being recorded for
this exception.

**See Also:**
- getEnvironment()

---

#### public
Name
getRemainingNewName()

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

**Returns:**
- The possibly null part of the new name that has not been resolved.
It is a composite name. It can be null, which means
the remaining new name field has not been set.

**See Also:**
- setRemainingNewName(javax.naming.Name)

---

#### public void setRemainingNewName​(
Name
newName)

Sets the "remaining new name" field of this exception.
This is the value returned by

getRemainingNewName()

.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

**Parameters:**
- newName

- The possibly null name to set the "remaining new name" to.
If null, it sets the remaining name field to null.

**See Also:**
- getRemainingNewName()

---

#### public
Name
getAltName()

Retrieves the

altName

field of this exception.
This is the name of the resolved object, relative to the context

altNameCtx

. It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:**
- The name of the resolved object, relative to

altNameCtx

.
It is a composite name. If null, then no name is specified.

**See Also:**
- setAltName(javax.naming.Name)

,

getAltNameCtx()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### public void setAltName​(
Name
altName)

Sets the

altName

field of this exception.

**Parameters:**
- altName

- The name of the resolved object, relative to

altNameCtx

.
It is a composite name.
If null, then no name is specified.

**See Also:**
- getAltName()

,

setAltNameCtx(javax.naming.Context)

---

#### public
Context
getAltNameCtx()

Retrieves the

altNameCtx

field of this exception.
This is the context relative to which

altName

is named.
It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:**
- The context relative to which

altName

is named.
If null, then the default initial context is implied.

**See Also:**
- setAltNameCtx(javax.naming.Context)

,

getAltName()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### public void setAltNameCtx​(
Context
altNameCtx)

Sets the

altNameCtx

field of this exception.

**Parameters:**
- altNameCtx

- The context relative to which

altName

is named. If null, then the default initial context
is implied.

**See Also:**
- getAltNameCtx()

,

setAltName(javax.naming.Name)

---

### Additional Sections

#### Class CannotProceedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.CannotProceedException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.CannotProceedException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.CannotProceedException

javax.naming.NamingException

- javax.naming.CannotProceedException

javax.naming.CannotProceedException

**All Implemented Interfaces:** Serializable

```java
public class
CannotProceedException

extends
NamingException
```

This exception is thrown to indicate that the operation reached
a point in the name where the operation cannot proceed any further.
When performing an operation on a composite name, a naming service
provider may reach a part of the name that does not belong to its
namespace. At that point, it can construct a
CannotProceedException and then invoke methods provided by
javax.naming.spi.NamingManager (such as getContinuationContext())
to locate another provider to continue the operation. If this is
not possible, this exception is raised to the caller of the
context operation.

If the program wants to handle this exception in particular, it
should catch CannotProceedException explicitly before attempting to
catch NamingException.

A CannotProceedException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
CannotProceedException should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

CannotProceedException

extends

NamingException

This exception is thrown to indicate that the operation reached
a point in the name where the operation cannot proceed any further.
When performing an operation on a composite name, a naming service
provider may reach a part of the name that does not belong to its
namespace. At that point, it can construct a
CannotProceedException and then invoke methods provided by
javax.naming.spi.NamingManager (such as getContinuationContext())
to locate another provider to continue the operation. If this is
not possible, this exception is raised to the caller of the
context operation.

If the program wants to handle this exception in particular, it
should catch CannotProceedException explicitly before attempting to
catch NamingException.

A CannotProceedException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
CannotProceedException should lock the object.

If the program wants to handle this exception in particular, it
should catch CannotProceedException explicitly before attempting to
catch NamingException.

A CannotProceedException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
CannotProceedException should lock the object.

A CannotProceedException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
CannotProceedException should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Name

altName

Contains the name of the resolved object, relative
to the context

altNameCtx

.

protected

Context

altNameCtx

Contains the context relative to which

altName

is specified.

protected

Hashtable

<?,​?>

environment

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

protected

Name

remainingNewName

Contains the remaining unresolved part of the second
"name" argument to Context.rename().

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CannotProceedException

()

Constructs a new instance of CannotProceedException.

CannotProceedException

​(

String

explanation)

Constructs a new instance of CannotProceedException using an
explanation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Name

getAltName

()

Retrieves the

altName

field of this exception.

Context

getAltNameCtx

()

Retrieves the

altNameCtx

field of this exception.

Hashtable

<?,​?>

getEnvironment

()

Retrieves the environment that was in effect when this exception
was created.

Name

getRemainingNewName

()

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

void

setAltName

​(

Name

altName)

Sets the

altName

field of this exception.

void

setAltNameCtx

​(

Context

altNameCtx)

Sets the

altNameCtx

field of this exception.

void

setEnvironment

​(

Hashtable

<?,​?> environment)

Sets the environment that will be returned when getEnvironment()
is called.

void

setRemainingNewName

​(

Name

newName)

Sets the "remaining new name" field of this exception.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Name

altName

Contains the name of the resolved object, relative
to the context

altNameCtx

.

protected

Context

altNameCtx

Contains the context relative to which

altName

is specified.

protected

Hashtable

<?,​?>

environment

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

protected

Name

remainingNewName

Contains the remaining unresolved part of the second
"name" argument to Context.rename().

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Field Summary

Contains the name of the resolved object, relative
to the context

altNameCtx

.

Contains the context relative to which

altName

is specified.

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

Contains the remaining unresolved part of the second
"name" argument to Context.rename().

Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Fields declared in class javax.naming. NamingException

Constructor Summary

Constructors

Constructor

Description

CannotProceedException

()

Constructs a new instance of CannotProceedException.

CannotProceedException

​(

String

explanation)

Constructs a new instance of CannotProceedException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of CannotProceedException.

Constructs a new instance of CannotProceedException using an
explanation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Name

getAltName

()

Retrieves the

altName

field of this exception.

Context

getAltNameCtx

()

Retrieves the

altNameCtx

field of this exception.

Hashtable

<?,​?>

getEnvironment

()

Retrieves the environment that was in effect when this exception
was created.

Name

getRemainingNewName

()

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

void

setAltName

​(

Name

altName)

Sets the

altName

field of this exception.

void

setAltNameCtx

​(

Context

altNameCtx)

Sets the

altNameCtx

field of this exception.

void

setEnvironment

​(

Hashtable

<?,​?> environment)

Sets the environment that will be returned when getEnvironment()
is called.

void

setRemainingNewName

​(

Name

newName)

Sets the "remaining new name" field of this exception.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Retrieves the

altName

field of this exception.

Retrieves the

altNameCtx

field of this exception.

Retrieves the environment that was in effect when this exception
was created.

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

Sets the

altName

field of this exception.

Sets the

altNameCtx

field of this exception.

Sets the environment that will be returned when getEnvironment()
is called.

Sets the "remaining new name" field of this exception.

Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

---

#### Methods declared in class javax.naming. NamingException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

---

#### Methods declared in class java.lang. Throwable

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

- remainingNewName

```java
protected
Name
remainingNewName
```

Contains the remaining unresolved part of the second
"name" argument to Context.rename().
This information is necessary for
continuing the Context.rename() operation.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

**See Also:** getRemainingNewName()

,

setRemainingNewName(javax.naming.Name)

- environment

```java
protected
Hashtable
<?,​?> environment
```

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

**See Also:** getEnvironment()

,

setEnvironment(java.util.Hashtable<?, ?>)

- altName

```java
protected
Name
altName
```

Contains the name of the resolved object, relative
to the context

altNameCtx

. It is a composite name.
If null, then no name is specified.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

**See Also:** getAltName()

,

setAltName(javax.naming.Name)

,

altNameCtx

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- altNameCtx

```java
protected
Context
altNameCtx
```

Contains the context relative to which

altName

is specified. If null, then the default initial
context is implied.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

**See Also:** getAltNameCtx()

,

setAltNameCtx(javax.naming.Context)

,

altName

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CannotProceedException

```java
public CannotProceedException​(
String
explanation)
```

Constructs a new instance of CannotProceedException using an
explanation. All unspecified fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

- CannotProceedException

```java
public CannotProceedException()
```

Constructs a new instance of CannotProceedException.
All fields default to null.

============ METHOD DETAIL ==========

- Method Detail

- getEnvironment

```java
public
Hashtable
<?,​?> getEnvironment()
```

Retrieves the environment that was in effect when this exception
was created.

**Returns:** Possibly null environment property set.
null means no environment was recorded for this exception.
**See Also:** setEnvironment(java.util.Hashtable<?, ?>)

- setEnvironment

```java
public void setEnvironment​(
Hashtable
<?,​?> environment)
```

Sets the environment that will be returned when getEnvironment()
is called.

**Parameters:** environment

- A possibly null environment property set.
null means no environment is being recorded for
this exception.
**See Also:** getEnvironment()

- getRemainingNewName

```java
public
Name
getRemainingNewName()
```

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

**Returns:** The possibly null part of the new name that has not been resolved.
It is a composite name. It can be null, which means
the remaining new name field has not been set.
**See Also:** setRemainingNewName(javax.naming.Name)

- setRemainingNewName

```java
public void setRemainingNewName​(
Name
newName)
```

Sets the "remaining new name" field of this exception.
This is the value returned by

getRemainingNewName()

.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

**Parameters:** newName

- The possibly null name to set the "remaining new name" to.
If null, it sets the remaining name field to null.
**See Also:** getRemainingNewName()

- getAltName

```java
public
Name
getAltName()
```

Retrieves the

altName

field of this exception.
This is the name of the resolved object, relative to the context

altNameCtx

. It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The name of the resolved object, relative to

altNameCtx

.
It is a composite name. If null, then no name is specified.
**See Also:** setAltName(javax.naming.Name)

,

getAltNameCtx()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- setAltName

```java
public void setAltName​(
Name
altName)
```

Sets the

altName

field of this exception.

**Parameters:** altName

- The name of the resolved object, relative to

altNameCtx

.
It is a composite name.
If null, then no name is specified.
**See Also:** getAltName()

,

setAltNameCtx(javax.naming.Context)

- getAltNameCtx

```java
public
Context
getAltNameCtx()
```

Retrieves the

altNameCtx

field of this exception.
This is the context relative to which

altName

is named.
It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The context relative to which

altName

is named.
If null, then the default initial context is implied.
**See Also:** setAltNameCtx(javax.naming.Context)

,

getAltName()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- setAltNameCtx

```java
public void setAltNameCtx​(
Context
altNameCtx)
```

Sets the

altNameCtx

field of this exception.

**Parameters:** altNameCtx

- The context relative to which

altName

is named. If null, then the default initial context
is implied.
**See Also:** getAltNameCtx()

,

setAltName(javax.naming.Name)

Field Detail

- remainingNewName

```java
protected
Name
remainingNewName
```

Contains the remaining unresolved part of the second
"name" argument to Context.rename().
This information is necessary for
continuing the Context.rename() operation.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

**See Also:** getRemainingNewName()

,

setRemainingNewName(javax.naming.Name)

- environment

```java
protected
Hashtable
<?,​?> environment
```

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

**See Also:** getEnvironment()

,

setEnvironment(java.util.Hashtable<?, ?>)

- altName

```java
protected
Name
altName
```

Contains the name of the resolved object, relative
to the context

altNameCtx

. It is a composite name.
If null, then no name is specified.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

**See Also:** getAltName()

,

setAltName(javax.naming.Name)

,

altNameCtx

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- altNameCtx

```java
protected
Context
altNameCtx
```

Contains the context relative to which

altName

is specified. If null, then the default initial
context is implied.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

**See Also:** getAltNameCtx()

,

setAltNameCtx(javax.naming.Context)

,

altName

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### Field Detail

remainingNewName

```java
protected
Name
remainingNewName
```

Contains the remaining unresolved part of the second
"name" argument to Context.rename().
This information is necessary for
continuing the Context.rename() operation.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

**See Also:** getRemainingNewName()

,

setRemainingNewName(javax.naming.Name)

---

#### remainingNewName

protected

Name

remainingNewName

Contains the remaining unresolved part of the second
"name" argument to Context.rename().
This information is necessary for
continuing the Context.rename() operation.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getRemainingName() and setRemainingName().

environment

```java
protected
Hashtable
<?,​?> environment
```

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

**See Also:** getEnvironment()

,

setEnvironment(java.util.Hashtable<?, ?>)

---

#### environment

protected

Hashtable

<?,​?> environment

Contains the environment
relevant for the Context or DirContext method that cannot proceed.

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

This field is initialized to null.
It should not be manipulated directly: it should be accessed
and updated using getEnvironment() and setEnvironment().

altName

```java
protected
Name
altName
```

Contains the name of the resolved object, relative
to the context

altNameCtx

. It is a composite name.
If null, then no name is specified.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

**See Also:** getAltName()

,

setAltName(javax.naming.Name)

,

altNameCtx

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### altName

protected

Name

altName

Contains the name of the resolved object, relative
to the context

altNameCtx

. It is a composite name.
If null, then no name is specified.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltName() and setAltName().

altNameCtx

```java
protected
Context
altNameCtx
```

Contains the context relative to which

altName

is specified. If null, then the default initial
context is implied.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

**See Also:** getAltNameCtx()

,

setAltNameCtx(javax.naming.Context)

,

altName

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### altNameCtx

protected

Context

altNameCtx

Contains the context relative to which

altName

is specified. If null, then the default initial
context is implied.
See the

javax.naming.spi.ObjectFactory.getObjectInstance

method for details on how this is used.

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

This field is initialized to null.
It should not be manipulated directly: it should
be accessed and updated using getAltNameCtx() and setAltNameCtx().

Constructor Detail

- CannotProceedException

```java
public CannotProceedException​(
String
explanation)
```

Constructs a new instance of CannotProceedException using an
explanation. All unspecified fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

- CannotProceedException

```java
public CannotProceedException()
```

Constructs a new instance of CannotProceedException.
All fields default to null.

---

#### Constructor Detail

CannotProceedException

```java
public CannotProceedException​(
String
explanation)
```

Constructs a new instance of CannotProceedException using an
explanation. All unspecified fields default to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

---

#### CannotProceedException

public CannotProceedException​(

String

explanation)

Constructs a new instance of CannotProceedException using an
explanation. All unspecified fields default to null.

CannotProceedException

```java
public CannotProceedException()
```

Constructs a new instance of CannotProceedException.
All fields default to null.

---

#### CannotProceedException

public CannotProceedException()

Constructs a new instance of CannotProceedException.
All fields default to null.

Method Detail

- getEnvironment

```java
public
Hashtable
<?,​?> getEnvironment()
```

Retrieves the environment that was in effect when this exception
was created.

**Returns:** Possibly null environment property set.
null means no environment was recorded for this exception.
**See Also:** setEnvironment(java.util.Hashtable<?, ?>)

- setEnvironment

```java
public void setEnvironment​(
Hashtable
<?,​?> environment)
```

Sets the environment that will be returned when getEnvironment()
is called.

**Parameters:** environment

- A possibly null environment property set.
null means no environment is being recorded for
this exception.
**See Also:** getEnvironment()

- getRemainingNewName

```java
public
Name
getRemainingNewName()
```

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

**Returns:** The possibly null part of the new name that has not been resolved.
It is a composite name. It can be null, which means
the remaining new name field has not been set.
**See Also:** setRemainingNewName(javax.naming.Name)

- setRemainingNewName

```java
public void setRemainingNewName​(
Name
newName)
```

Sets the "remaining new name" field of this exception.
This is the value returned by

getRemainingNewName()

.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

**Parameters:** newName

- The possibly null name to set the "remaining new name" to.
If null, it sets the remaining name field to null.
**See Also:** getRemainingNewName()

- getAltName

```java
public
Name
getAltName()
```

Retrieves the

altName

field of this exception.
This is the name of the resolved object, relative to the context

altNameCtx

. It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The name of the resolved object, relative to

altNameCtx

.
It is a composite name. If null, then no name is specified.
**See Also:** setAltName(javax.naming.Name)

,

getAltNameCtx()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- setAltName

```java
public void setAltName​(
Name
altName)
```

Sets the

altName

field of this exception.

**Parameters:** altName

- The name of the resolved object, relative to

altNameCtx

.
It is a composite name.
If null, then no name is specified.
**See Also:** getAltName()

,

setAltNameCtx(javax.naming.Context)

- getAltNameCtx

```java
public
Context
getAltNameCtx()
```

Retrieves the

altNameCtx

field of this exception.
This is the context relative to which

altName

is named.
It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The context relative to which

altName

is named.
If null, then the default initial context is implied.
**See Also:** setAltNameCtx(javax.naming.Context)

,

getAltName()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

- setAltNameCtx

```java
public void setAltNameCtx​(
Context
altNameCtx)
```

Sets the

altNameCtx

field of this exception.

**Parameters:** altNameCtx

- The context relative to which

altName

is named. If null, then the default initial context
is implied.
**See Also:** getAltNameCtx()

,

setAltName(javax.naming.Name)

---

#### Method Detail

getEnvironment

```java
public
Hashtable
<?,​?> getEnvironment()
```

Retrieves the environment that was in effect when this exception
was created.

**Returns:** Possibly null environment property set.
null means no environment was recorded for this exception.
**See Also:** setEnvironment(java.util.Hashtable<?, ?>)

---

#### getEnvironment

public

Hashtable

<?,​?> getEnvironment()

Retrieves the environment that was in effect when this exception
was created.

setEnvironment

```java
public void setEnvironment​(
Hashtable
<?,​?> environment)
```

Sets the environment that will be returned when getEnvironment()
is called.

**Parameters:** environment

- A possibly null environment property set.
null means no environment is being recorded for
this exception.
**See Also:** getEnvironment()

---

#### setEnvironment

public void setEnvironment​(

Hashtable

<?,​?> environment)

Sets the environment that will be returned when getEnvironment()
is called.

getRemainingNewName

```java
public
Name
getRemainingNewName()
```

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

**Returns:** The possibly null part of the new name that has not been resolved.
It is a composite name. It can be null, which means
the remaining new name field has not been set.
**See Also:** setRemainingNewName(javax.naming.Name)

---

#### getRemainingNewName

public

Name

getRemainingNewName()

Retrieves the "remaining new name" field of this exception, which is
used when this exception is thrown during a rename() operation.

setRemainingNewName

```java
public void setRemainingNewName​(
Name
newName)
```

Sets the "remaining new name" field of this exception.
This is the value returned by

getRemainingNewName()

.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

**Parameters:** newName

- The possibly null name to set the "remaining new name" to.
If null, it sets the remaining name field to null.
**See Also:** getRemainingNewName()

---

#### setRemainingNewName

public void setRemainingNewName​(

Name

newName)

Sets the "remaining new name" field of this exception.
This is the value returned by

getRemainingNewName()

.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

newName

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

A copy of

newName

is made and stored.
Subsequent changes to

name

does not
affect the copy in this NamingException and vice versa.

getAltName

```java
public
Name
getAltName()
```

Retrieves the

altName

field of this exception.
This is the name of the resolved object, relative to the context

altNameCtx

. It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The name of the resolved object, relative to

altNameCtx

.
It is a composite name. If null, then no name is specified.
**See Also:** setAltName(javax.naming.Name)

,

getAltNameCtx()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### getAltName

public

Name

getAltName()

Retrieves the

altName

field of this exception.
This is the name of the resolved object, relative to the context

altNameCtx

. It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

setAltName

```java
public void setAltName​(
Name
altName)
```

Sets the

altName

field of this exception.

**Parameters:** altName

- The name of the resolved object, relative to

altNameCtx

.
It is a composite name.
If null, then no name is specified.
**See Also:** getAltName()

,

setAltNameCtx(javax.naming.Context)

---

#### setAltName

public void setAltName​(

Name

altName)

Sets the

altName

field of this exception.

getAltNameCtx

```java
public
Context
getAltNameCtx()
```

Retrieves the

altNameCtx

field of this exception.
This is the context relative to which

altName

is named.
It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

**Returns:** The context relative to which

altName

is named.
If null, then the default initial context is implied.
**See Also:** setAltNameCtx(javax.naming.Context)

,

getAltName()

,

ObjectFactory.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

---

#### getAltNameCtx

public

Context

getAltNameCtx()

Retrieves the

altNameCtx

field of this exception.
This is the context relative to which

altName

is named.
It will be used during a subsequent call to the

javax.naming.spi.ObjectFactory.getObjectInstance

method.

setAltNameCtx

```java
public void setAltNameCtx​(
Context
altNameCtx)
```

Sets the

altNameCtx

field of this exception.

**Parameters:** altNameCtx

- The context relative to which

altName

is named. If null, then the default initial context
is implied.
**See Also:** getAltNameCtx()

,

setAltName(javax.naming.Name)

---

#### setAltNameCtx

public void setAltNameCtx​(

Context

altNameCtx)

Sets the

altNameCtx

field of this exception.

---

