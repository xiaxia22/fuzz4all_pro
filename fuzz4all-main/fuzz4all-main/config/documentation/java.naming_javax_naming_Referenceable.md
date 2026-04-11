# Interface Referenceable

**Source:** `java.naming\javax\naming\Referenceable.html`

### Class Description

```java
public interface
Referenceable
```

This interface is implemented by an object that can provide a
Reference to itself.

A Reference represents a way of recording address information about
objects which themselves are not directly bound to the naming system.
Such objects can implement the Referenceable interface as a way
for programs that use that object to determine what its Reference is.
For example, when binding an object, if an object implements the
Referenceable interface, getReference() can be invoked on the object to
get its Reference to use for binding.

**Since:** 1.3
**See Also:** Context.bind(javax.naming.Name, java.lang.Object)

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

Reference

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Reference
getReference()
throws
NamingException

Retrieves the Reference of this object.

**Returns:**
- The non-null Reference of this object.

**Throws:**
- NamingException

- If a naming exception was encountered
while retrieving the reference.

---

### Additional Sections

#### Interface Referenceable

```java
public interface
Referenceable
```

This interface is implemented by an object that can provide a
Reference to itself.

A Reference represents a way of recording address information about
objects which themselves are not directly bound to the naming system.
Such objects can implement the Referenceable interface as a way
for programs that use that object to determine what its Reference is.
For example, when binding an object, if an object implements the
Referenceable interface, getReference() can be invoked on the object to
get its Reference to use for binding.

**Since:** 1.3
**See Also:** Context.bind(javax.naming.Name, java.lang.Object)

,

NamingManager.getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

Reference

public interface

Referenceable

This interface is implemented by an object that can provide a
Reference to itself.

A Reference represents a way of recording address information about
objects which themselves are not directly bound to the naming system.
Such objects can implement the Referenceable interface as a way
for programs that use that object to determine what its Reference is.
For example, when binding an object, if an object implements the
Referenceable interface, getReference() can be invoked on the object to
get its Reference to use for binding.

A Reference represents a way of recording address information about
objects which themselves are not directly bound to the naming system.
Such objects can implement the Referenceable interface as a way
for programs that use that object to determine what its Reference is.
For example, when binding an object, if an object implements the
Referenceable interface, getReference() can be invoked on the object to
get its Reference to use for binding.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Reference

getReference

()

Retrieves the Reference of this object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Reference

getReference

()

Retrieves the Reference of this object.

---

#### Method Summary

Retrieves the Reference of this object.

============ METHOD DETAIL ==========

- Method Detail

- getReference

```java
Reference
getReference()
throws
NamingException
```

Retrieves the Reference of this object.

**Returns:** The non-null Reference of this object.
**Throws:** NamingException

- If a naming exception was encountered
while retrieving the reference.

Method Detail

- getReference

```java
Reference
getReference()
throws
NamingException
```

Retrieves the Reference of this object.

**Returns:** The non-null Reference of this object.
**Throws:** NamingException

- If a naming exception was encountered
while retrieving the reference.

---

#### Method Detail

getReference

```java
Reference
getReference()
throws
NamingException
```

Retrieves the Reference of this object.

**Returns:** The non-null Reference of this object.
**Throws:** NamingException

- If a naming exception was encountered
while retrieving the reference.

---

#### getReference

Reference

getReference()
throws

NamingException

Retrieves the Reference of this object.

---

