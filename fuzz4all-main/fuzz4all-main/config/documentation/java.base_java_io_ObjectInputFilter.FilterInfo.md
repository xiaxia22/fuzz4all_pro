# Interface ObjectInputFilter.FilterInfo

**Source:** `java.base\java\io\ObjectInputFilter.FilterInfo.html`

### Class Description

```java
public static interface
ObjectInputFilter.FilterInfo
```

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

**Enclosing interface:** ObjectInputFilter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Class
<?> serialClass()

The class of an object being deserialized.
For arrays, it is the array type.
For example, the array class name of a 2 dimensional array of strings is
"

[[Ljava.lang.String;

".
To check the array's element type, iteratively use

Class.getComponentType

while the result
is an array and then check the class.
The

serialClass is null

in the case where a new object is not being
created and to give the filter a chance to check the depth, number of
references to existing objects, and the stream size.

**Returns:**
- class of an object being deserialized; may be null

---

#### long arrayLength()

The number of array elements when deserializing an array of the class.

**Returns:**
- the non-negative number of array elements when deserializing
an array of the class, otherwise -1

---

#### long depth()

The current depth.
The depth starts at

1

and increases for each nested object and
decrements when each nested object returns.

**Returns:**
- the current depth

---

#### long references()

The current number of object references.

**Returns:**
- the non-negative current number of object references

---

#### long streamBytes()

The current number of bytes consumed.

**Returns:**
- the non-negative current number of bytes consumed

**Implementation Requirements:**
- streamBytes

is implementation specific
and may not be directly related to the object in the stream
that caused the callback.

---

### Additional Sections

#### Interface ObjectInputFilter.FilterInfo

**Enclosing interface:** ObjectInputFilter

```java
public static interface
ObjectInputFilter.FilterInfo
```

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

**Since:** 9

public static interface

ObjectInputFilter.FilterInfo

FilterInfo provides access to information about the current object
being deserialized and the status of the

ObjectInputStream

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

arrayLength

()

The number of array elements when deserializing an array of the class.

long

depth

()

The current depth.

long

references

()

The current number of object references.

Class

<?>

serialClass

()

The class of an object being deserialized.

long

streamBytes

()

The current number of bytes consumed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

arrayLength

()

The number of array elements when deserializing an array of the class.

long

depth

()

The current depth.

long

references

()

The current number of object references.

Class

<?>

serialClass

()

The class of an object being deserialized.

long

streamBytes

()

The current number of bytes consumed.

---

#### Method Summary

The number of array elements when deserializing an array of the class.

The current depth.

The current number of object references.

The class of an object being deserialized.

The current number of bytes consumed.

============ METHOD DETAIL ==========

- Method Detail

- serialClass

```java
Class
<?> serialClass()
```

The class of an object being deserialized.
For arrays, it is the array type.
For example, the array class name of a 2 dimensional array of strings is
"

[[Ljava.lang.String;

".
To check the array's element type, iteratively use

Class.getComponentType

while the result
is an array and then check the class.
The

serialClass is null

in the case where a new object is not being
created and to give the filter a chance to check the depth, number of
references to existing objects, and the stream size.

**Returns:** class of an object being deserialized; may be null

- arrayLength

```java
long arrayLength()
```

The number of array elements when deserializing an array of the class.

**Returns:** the non-negative number of array elements when deserializing
an array of the class, otherwise -1

- depth

```java
long depth()
```

The current depth.
The depth starts at

1

and increases for each nested object and
decrements when each nested object returns.

**Returns:** the current depth

- references

```java
long references()
```

The current number of object references.

**Returns:** the non-negative current number of object references

- streamBytes

```java
long streamBytes()
```

The current number of bytes consumed.

**Implementation Requirements:** streamBytes

is implementation specific
and may not be directly related to the object in the stream
that caused the callback.
**Returns:** the non-negative current number of bytes consumed

Method Detail

- serialClass

```java
Class
<?> serialClass()
```

The class of an object being deserialized.
For arrays, it is the array type.
For example, the array class name of a 2 dimensional array of strings is
"

[[Ljava.lang.String;

".
To check the array's element type, iteratively use

Class.getComponentType

while the result
is an array and then check the class.
The

serialClass is null

in the case where a new object is not being
created and to give the filter a chance to check the depth, number of
references to existing objects, and the stream size.

**Returns:** class of an object being deserialized; may be null

- arrayLength

```java
long arrayLength()
```

The number of array elements when deserializing an array of the class.

**Returns:** the non-negative number of array elements when deserializing
an array of the class, otherwise -1

- depth

```java
long depth()
```

The current depth.
The depth starts at

1

and increases for each nested object and
decrements when each nested object returns.

**Returns:** the current depth

- references

```java
long references()
```

The current number of object references.

**Returns:** the non-negative current number of object references

- streamBytes

```java
long streamBytes()
```

The current number of bytes consumed.

**Implementation Requirements:** streamBytes

is implementation specific
and may not be directly related to the object in the stream
that caused the callback.
**Returns:** the non-negative current number of bytes consumed

---

#### Method Detail

serialClass

```java
Class
<?> serialClass()
```

The class of an object being deserialized.
For arrays, it is the array type.
For example, the array class name of a 2 dimensional array of strings is
"

[[Ljava.lang.String;

".
To check the array's element type, iteratively use

Class.getComponentType

while the result
is an array and then check the class.
The

serialClass is null

in the case where a new object is not being
created and to give the filter a chance to check the depth, number of
references to existing objects, and the stream size.

**Returns:** class of an object being deserialized; may be null

---

#### serialClass

Class

<?> serialClass()

The class of an object being deserialized.
For arrays, it is the array type.
For example, the array class name of a 2 dimensional array of strings is
"

[[Ljava.lang.String;

".
To check the array's element type, iteratively use

Class.getComponentType

while the result
is an array and then check the class.
The

serialClass is null

in the case where a new object is not being
created and to give the filter a chance to check the depth, number of
references to existing objects, and the stream size.

arrayLength

```java
long arrayLength()
```

The number of array elements when deserializing an array of the class.

**Returns:** the non-negative number of array elements when deserializing
an array of the class, otherwise -1

---

#### arrayLength

long arrayLength()

The number of array elements when deserializing an array of the class.

depth

```java
long depth()
```

The current depth.
The depth starts at

1

and increases for each nested object and
decrements when each nested object returns.

**Returns:** the current depth

---

#### depth

long depth()

The current depth.
The depth starts at

1

and increases for each nested object and
decrements when each nested object returns.

references

```java
long references()
```

The current number of object references.

**Returns:** the non-negative current number of object references

---

#### references

long references()

The current number of object references.

streamBytes

```java
long streamBytes()
```

The current number of bytes consumed.

**Implementation Requirements:** streamBytes

is implementation specific
and may not be directly related to the object in the stream
that caused the callback.
**Returns:** the non-negative current number of bytes consumed

---

#### streamBytes

long streamBytes()

The current number of bytes consumed.

---

