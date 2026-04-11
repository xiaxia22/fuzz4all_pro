# Class ResolveResult

**Source:** `java.naming\javax\naming\spi\ResolveResult.html`

### Class Description

```java
public class
ResolveResult

extends
Object

implements
Serializable
```

This class represents the result of resolution of a name.
It contains the object to which name was resolved, and the portion
of the name that has not been resolved.

A ResolveResult instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ResolveResult instance should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Object
resolvedObj

Field containing the Object that was resolved to successfully.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

---

#### protected
Name
remainingName

Field containing the remaining name yet to be resolved.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

---

### Constructor Details

#### protected ResolveResult()

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

---

#### public ResolveResult​(
Object
robj,

String
rcomp)

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

**Parameters:**
- robj

- The non-null object resolved to.
- rcomp

- The single remaining name component that has yet to be
resolved. Cannot be null (but can be empty).

---

#### public ResolveResult​(
Object
robj,

Name
rname)

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

**Parameters:**
- robj

- The non-null Object resolved to.
- rname

- The non-null remaining name that has yet to be resolved.

---

### Method Details

#### public
Name
getRemainingName()

Retrieves the remaining unresolved portion of the name.

**Returns:**
- The remaining unresolved portion of the name.
Cannot be null but empty OK.

**See Also:**
- appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

,

setRemainingName(javax.naming.Name)

---

#### public
Object
getResolvedObj()

Retrieves the Object to which resolution was successful.

**Returns:**
- The Object to which resolution was successful. Cannot be null.

**See Also:**
- setResolvedObj(java.lang.Object)

---

#### public void setRemainingName​(
Name
name)

Sets the remaining name field of this result to name.
A copy of name is made so that modifying the copy within
this ResolveResult does not affect

name

and
vice versa.

**Parameters:**
- name

- The name to set remaining name to. Cannot be null.

**See Also:**
- getRemainingName()

,

appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

---

#### public void appendRemainingName​(
Name
name)

Adds components to the end of remaining name.

**Parameters:**
- name

- The components to add. Can be null.

**See Also:**
- getRemainingName()

,

setRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

---

#### public void appendRemainingComponent​(
String
name)

Adds a single component to the end of remaining name.

**Parameters:**
- name

- The component to add. Can be null.

**See Also:**
- getRemainingName()

,

appendRemainingName(javax.naming.Name)

---

#### public void setResolvedObj​(
Object
obj)

Sets the resolved Object field of this result to obj.

**Parameters:**
- obj

- The object to use for setting the resolved obj field.
Cannot be null.

**See Also:**
- getResolvedObj()

---

### Additional Sections

#### Class ResolveResult

java.lang.Object

- javax.naming.spi.ResolveResult

javax.naming.spi.ResolveResult

**All Implemented Interfaces:** Serializable

```java
public class
ResolveResult

extends
Object

implements
Serializable
```

This class represents the result of resolution of a name.
It contains the object to which name was resolved, and the portion
of the name that has not been resolved.

A ResolveResult instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ResolveResult instance should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

ResolveResult

extends

Object

implements

Serializable

This class represents the result of resolution of a name.
It contains the object to which name was resolved, and the portion
of the name that has not been resolved.

A ResolveResult instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ResolveResult instance should lock the object.

A ResolveResult instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single ResolveResult instance should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Name

remainingName

Field containing the remaining name yet to be resolved.

protected

Object

resolvedObj

Field containing the Object that was resolved to successfully.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ResolveResult

()

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

ResolveResult

​(

Object

robj,

String

rcomp)

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

ResolveResult

​(

Object

robj,

Name

rname)

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

appendRemainingComponent

​(

String

name)

Adds a single component to the end of remaining name.

void

appendRemainingName

​(

Name

name)

Adds components to the end of remaining name.

Name

getRemainingName

()

Retrieves the remaining unresolved portion of the name.

Object

getResolvedObj

()

Retrieves the Object to which resolution was successful.

void

setRemainingName

​(

Name

name)

Sets the remaining name field of this result to name.

void

setResolvedObj

​(

Object

obj)

Sets the resolved Object field of this result to obj.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Name

remainingName

Field containing the remaining name yet to be resolved.

protected

Object

resolvedObj

Field containing the Object that was resolved to successfully.

---

#### Field Summary

Field containing the remaining name yet to be resolved.

Field containing the Object that was resolved to successfully.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ResolveResult

()

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

ResolveResult

​(

Object

robj,

String

rcomp)

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

ResolveResult

​(

Object

robj,

Name

rname)

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

---

#### Constructor Summary

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

appendRemainingComponent

​(

String

name)

Adds a single component to the end of remaining name.

void

appendRemainingName

​(

Name

name)

Adds components to the end of remaining name.

Name

getRemainingName

()

Retrieves the remaining unresolved portion of the name.

Object

getResolvedObj

()

Retrieves the Object to which resolution was successful.

void

setRemainingName

​(

Name

name)

Sets the remaining name field of this result to name.

void

setResolvedObj

​(

Object

obj)

Sets the resolved Object field of this result to obj.

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

---

#### Method Summary

Adds a single component to the end of remaining name.

Adds components to the end of remaining name.

Retrieves the remaining unresolved portion of the name.

Retrieves the Object to which resolution was successful.

Sets the remaining name field of this result to name.

Sets the resolved Object field of this result to obj.

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

============ FIELD DETAIL ===========

- Field Detail

- resolvedObj

```java
protected
Object
resolvedObj
```

Field containing the Object that was resolved to successfully.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

- remainingName

```java
protected
Name
remainingName
```

Field containing the remaining name yet to be resolved.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ResolveResult

```java
protected ResolveResult()
```

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

- ResolveResult

```java
public ResolveResult​(
Object
robj,

String
rcomp)
```

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

**Parameters:** robj

- The non-null object resolved to.
**Parameters:** rcomp

- The single remaining name component that has yet to be
resolved. Cannot be null (but can be empty).

- ResolveResult

```java
public ResolveResult​(
Object
robj,

Name
rname)
```

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

**Parameters:** robj

- The non-null Object resolved to.
**Parameters:** rname

- The non-null remaining name that has yet to be resolved.

============ METHOD DETAIL ==========

- Method Detail

- getRemainingName

```java
public
Name
getRemainingName()
```

Retrieves the remaining unresolved portion of the name.

**Returns:** The remaining unresolved portion of the name.
Cannot be null but empty OK.
**See Also:** appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

,

setRemainingName(javax.naming.Name)

- getResolvedObj

```java
public
Object
getResolvedObj()
```

Retrieves the Object to which resolution was successful.

**Returns:** The Object to which resolution was successful. Cannot be null.
**See Also:** setResolvedObj(java.lang.Object)

- setRemainingName

```java
public void setRemainingName​(
Name
name)
```

Sets the remaining name field of this result to name.
A copy of name is made so that modifying the copy within
this ResolveResult does not affect

name

and
vice versa.

**Parameters:** name

- The name to set remaining name to. Cannot be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

- appendRemainingName

```java
public void appendRemainingName​(
Name
name)
```

Adds components to the end of remaining name.

**Parameters:** name

- The components to add. Can be null.
**See Also:** getRemainingName()

,

setRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

- appendRemainingComponent

```java
public void appendRemainingComponent​(
String
name)
```

Adds a single component to the end of remaining name.

**Parameters:** name

- The component to add. Can be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

- setResolvedObj

```java
public void setResolvedObj​(
Object
obj)
```

Sets the resolved Object field of this result to obj.

**Parameters:** obj

- The object to use for setting the resolved obj field.
Cannot be null.
**See Also:** getResolvedObj()

Field Detail

- resolvedObj

```java
protected
Object
resolvedObj
```

Field containing the Object that was resolved to successfully.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

- remainingName

```java
protected
Name
remainingName
```

Field containing the remaining name yet to be resolved.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

---

#### Field Detail

resolvedObj

```java
protected
Object
resolvedObj
```

Field containing the Object that was resolved to successfully.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

---

#### resolvedObj

protected

Object

resolvedObj

Field containing the Object that was resolved to successfully.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

remainingName

```java
protected
Name
remainingName
```

Field containing the remaining name yet to be resolved.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

---

#### remainingName

protected

Name

remainingName

Field containing the remaining name yet to be resolved.
It can be null only when constructed using a subclass.
Constructors should always initialize this.

Constructor Detail

- ResolveResult

```java
protected ResolveResult()
```

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

- ResolveResult

```java
public ResolveResult​(
Object
robj,

String
rcomp)
```

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

**Parameters:** robj

- The non-null object resolved to.
**Parameters:** rcomp

- The single remaining name component that has yet to be
resolved. Cannot be null (but can be empty).

- ResolveResult

```java
public ResolveResult​(
Object
robj,

Name
rname)
```

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

**Parameters:** robj

- The non-null Object resolved to.
**Parameters:** rname

- The non-null remaining name that has yet to be resolved.

---

#### Constructor Detail

ResolveResult

```java
protected ResolveResult()
```

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

---

#### ResolveResult

protected ResolveResult()

Constructs an instance of ResolveResult with the
resolved object and remaining name both initialized to null.

ResolveResult

```java
public ResolveResult​(
Object
robj,

String
rcomp)
```

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

**Parameters:** robj

- The non-null object resolved to.
**Parameters:** rcomp

- The single remaining name component that has yet to be
resolved. Cannot be null (but can be empty).

---

#### ResolveResult

public ResolveResult​(

Object

robj,

String

rcomp)

Constructs a new instance of ResolveResult consisting of
the resolved object and the remaining unresolved component.

ResolveResult

```java
public ResolveResult​(
Object
robj,

Name
rname)
```

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

**Parameters:** robj

- The non-null Object resolved to.
**Parameters:** rname

- The non-null remaining name that has yet to be resolved.

---

#### ResolveResult

public ResolveResult​(

Object

robj,

Name

rname)

Constructs a new instance of ResolveResult consisting of
the resolved Object and the remaining name.

Method Detail

- getRemainingName

```java
public
Name
getRemainingName()
```

Retrieves the remaining unresolved portion of the name.

**Returns:** The remaining unresolved portion of the name.
Cannot be null but empty OK.
**See Also:** appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

,

setRemainingName(javax.naming.Name)

- getResolvedObj

```java
public
Object
getResolvedObj()
```

Retrieves the Object to which resolution was successful.

**Returns:** The Object to which resolution was successful. Cannot be null.
**See Also:** setResolvedObj(java.lang.Object)

- setRemainingName

```java
public void setRemainingName​(
Name
name)
```

Sets the remaining name field of this result to name.
A copy of name is made so that modifying the copy within
this ResolveResult does not affect

name

and
vice versa.

**Parameters:** name

- The name to set remaining name to. Cannot be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

- appendRemainingName

```java
public void appendRemainingName​(
Name
name)
```

Adds components to the end of remaining name.

**Parameters:** name

- The components to add. Can be null.
**See Also:** getRemainingName()

,

setRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

- appendRemainingComponent

```java
public void appendRemainingComponent​(
String
name)
```

Adds a single component to the end of remaining name.

**Parameters:** name

- The component to add. Can be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

- setResolvedObj

```java
public void setResolvedObj​(
Object
obj)
```

Sets the resolved Object field of this result to obj.

**Parameters:** obj

- The object to use for setting the resolved obj field.
Cannot be null.
**See Also:** getResolvedObj()

---

#### Method Detail

getRemainingName

```java
public
Name
getRemainingName()
```

Retrieves the remaining unresolved portion of the name.

**Returns:** The remaining unresolved portion of the name.
Cannot be null but empty OK.
**See Also:** appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

,

setRemainingName(javax.naming.Name)

---

#### getRemainingName

public

Name

getRemainingName()

Retrieves the remaining unresolved portion of the name.

getResolvedObj

```java
public
Object
getResolvedObj()
```

Retrieves the Object to which resolution was successful.

**Returns:** The Object to which resolution was successful. Cannot be null.
**See Also:** setResolvedObj(java.lang.Object)

---

#### getResolvedObj

public

Object

getResolvedObj()

Retrieves the Object to which resolution was successful.

setRemainingName

```java
public void setRemainingName​(
Name
name)
```

Sets the remaining name field of this result to name.
A copy of name is made so that modifying the copy within
this ResolveResult does not affect

name

and
vice versa.

**Parameters:** name

- The name to set remaining name to. Cannot be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

---

#### setRemainingName

public void setRemainingName​(

Name

name)

Sets the remaining name field of this result to name.
A copy of name is made so that modifying the copy within
this ResolveResult does not affect

name

and
vice versa.

appendRemainingName

```java
public void appendRemainingName​(
Name
name)
```

Adds components to the end of remaining name.

**Parameters:** name

- The components to add. Can be null.
**See Also:** getRemainingName()

,

setRemainingName(javax.naming.Name)

,

appendRemainingComponent(java.lang.String)

---

#### appendRemainingName

public void appendRemainingName​(

Name

name)

Adds components to the end of remaining name.

appendRemainingComponent

```java
public void appendRemainingComponent​(
String
name)
```

Adds a single component to the end of remaining name.

**Parameters:** name

- The component to add. Can be null.
**See Also:** getRemainingName()

,

appendRemainingName(javax.naming.Name)

---

#### appendRemainingComponent

public void appendRemainingComponent​(

String

name)

Adds a single component to the end of remaining name.

setResolvedObj

```java
public void setResolvedObj​(
Object
obj)
```

Sets the resolved Object field of this result to obj.

**Parameters:** obj

- The object to use for setting the resolved obj field.
Cannot be null.
**See Also:** getResolvedObj()

---

#### setResolvedObj

public void setResolvedObj​(

Object

obj)

Sets the resolved Object field of this result to obj.

---

