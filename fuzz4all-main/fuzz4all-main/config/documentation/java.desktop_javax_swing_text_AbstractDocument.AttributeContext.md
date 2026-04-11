# Interface AbstractDocument.AttributeContext

**Source:** `java.desktop\javax\swing\text\AbstractDocument.AttributeContext.html`

### Class Description

```java
public static interface
AbstractDocument.AttributeContext
```

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques. Each mutation of the attribute set can be
used to exchange a previous AttributeSet instance with
another, preserving the possibility of the AttributeSet
remaining immutable. An implementation is provided by
the StyleContext class.

The Element implementations provided by this class use
this interface to provide their MutableAttributeSet
implementations, so that different AttributeSet compression
techniques can be employed. The method

getAttributeContext

should be implemented to
return the object responsible for implementing the desired
compression technique.

**All Known Implementing Classes:** StyleContext

,

StyleSheet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)

Adds an attribute to the given set, and returns
the new representative set.

**Parameters:**
- old

- the old attribute set
- name

- the non-null attribute name
- value

- the attribute value

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)

Adds a set of attributes to the element.

**Parameters:**
- old

- the old attribute set
- attr

- the attributes to add

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)

Removes an attribute from the set.

**Parameters:**
- old

- the old attribute set
- name

- the non-null attribute name

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttribute(java.lang.Object)

---

#### AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)

Removes a set of attributes for the element.

**Parameters:**
- old

- the old attribute set
- names

- the attribute names

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)

Removes a set of attributes for the element.

**Parameters:**
- old

- the old attribute set
- attrs

- the attributes

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### AttributeSet
getEmptySet()

Fetches an empty AttributeSet.

**Returns:**
- the attribute set

---

#### void reclaim​(
AttributeSet
a)

Reclaims an attribute set.
This is a way for a MutableAttributeSet to mark that it no
longer need a particular immutable set. This is only necessary
in 1.1 where there are no weak references. A 1.1 implementation
would call this in its finalize method.

**Parameters:**
- a

- the attribute set to reclaim

---

### Additional Sections

#### Interface AbstractDocument.AttributeContext

**All Known Implementing Classes:** StyleContext

,

StyleSheet

**Enclosing class:** AbstractDocument

```java
public static interface
AbstractDocument.AttributeContext
```

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques. Each mutation of the attribute set can be
used to exchange a previous AttributeSet instance with
another, preserving the possibility of the AttributeSet
remaining immutable. An implementation is provided by
the StyleContext class.

The Element implementations provided by this class use
this interface to provide their MutableAttributeSet
implementations, so that different AttributeSet compression
techniques can be employed. The method

getAttributeContext

should be implemented to
return the object responsible for implementing the desired
compression technique.

**See Also:** StyleContext

public static interface

AbstractDocument.AttributeContext

An interface that can be used to allow MutableAttributeSet
implementations to use pluggable attribute compression
techniques. Each mutation of the attribute set can be
used to exchange a previous AttributeSet instance with
another, preserving the possibility of the AttributeSet
remaining immutable. An implementation is provided by
the StyleContext class.

The Element implementations provided by this class use
this interface to provide their MutableAttributeSet
implementations, so that different AttributeSet compression
techniques can be employed. The method

getAttributeContext

should be implemented to
return the object responsible for implementing the desired
compression technique.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AttributeSet

addAttribute

​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

AttributeSet

addAttributes

​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

AttributeSet

getEmptySet

()

Fetches an empty AttributeSet.

void

reclaim

​(

AttributeSet

a)

Reclaims an attribute set.

AttributeSet

removeAttribute

​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

AttributeSet

removeAttributes

​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

AttributeSet

removeAttributes

​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AttributeSet

addAttribute

​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

AttributeSet

addAttributes

​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

AttributeSet

getEmptySet

()

Fetches an empty AttributeSet.

void

reclaim

​(

AttributeSet

a)

Reclaims an attribute set.

AttributeSet

removeAttribute

​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

AttributeSet

removeAttributes

​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

AttributeSet

removeAttributes

​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

---

#### Method Summary

Adds an attribute to the given set, and returns
the new representative set.

Adds a set of attributes to the element.

Fetches an empty AttributeSet.

Reclaims an attribute set.

Removes an attribute from the set.

Removes a set of attributes for the element.

============ METHOD DETAIL ==========

- Method Detail

- addAttribute

```java
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- addAttributes

```java
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- removeAttribute

```java
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

- removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- getEmptySet

```java
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Returns:** the attribute set

- reclaim

```java
void reclaim​(
AttributeSet
a)
```

Reclaims an attribute set.
This is a way for a MutableAttributeSet to mark that it no
longer need a particular immutable set. This is only necessary
in 1.1 where there are no weak references. A 1.1 implementation
would call this in its finalize method.

**Parameters:** a

- the attribute set to reclaim

Method Detail

- addAttribute

```java
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- addAttributes

```java
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- removeAttribute

```java
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

- removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- getEmptySet

```java
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Returns:** the attribute set

- reclaim

```java
void reclaim​(
AttributeSet
a)
```

Reclaims an attribute set.
This is a way for a MutableAttributeSet to mark that it no
longer need a particular immutable set. This is only necessary
in 1.1 where there are no weak references. A 1.1 implementation
would call this in its finalize method.

**Parameters:** a

- the attribute set to reclaim

---

#### Method Detail

addAttribute

```java
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### addAttribute

AttributeSet

addAttribute​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

addAttributes

```java
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### addAttributes

AttributeSet

addAttributes​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

removeAttribute

```java
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

---

#### removeAttribute

AttributeSet

removeAttribute​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### removeAttributes

AttributeSet

removeAttributes​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

removeAttributes

```java
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### removeAttributes

AttributeSet

removeAttributes​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

getEmptySet

```java
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Returns:** the attribute set

---

#### getEmptySet

AttributeSet

getEmptySet()

Fetches an empty AttributeSet.

reclaim

```java
void reclaim​(
AttributeSet
a)
```

Reclaims an attribute set.
This is a way for a MutableAttributeSet to mark that it no
longer need a particular immutable set. This is only necessary
in 1.1 where there are no weak references. A 1.1 implementation
would call this in its finalize method.

**Parameters:** a

- the attribute set to reclaim

---

#### reclaim

void reclaim​(

AttributeSet

a)

Reclaims an attribute set.
This is a way for a MutableAttributeSet to mark that it no
longer need a particular immutable set. This is only necessary
in 1.1 where there are no weak references. A 1.1 implementation
would call this in its finalize method.

---

