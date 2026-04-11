# Interface AttributeException

**Source:** `java.desktop\javax\print\AttributeException.html`

### Class Description

```java
public interface
AttributeException
```

Interface

AttributeException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving one or more printing attributes that a particular Print
Service instance does not support. Either the attribute is not supported at
all, or the attribute is supported but the particular specified value is not
supported. The Print Service API does not define any print exception classes
that implement interface

AttributeException

, that being left to the
Print Service implementor's discretion.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Class
<?>[] getUnsupportedAttributes()

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes. The objects in the returned array are
classes that extend the base interface

Attribute

.

**Returns:**
- unsupported attribute classes

---

#### Attribute
[] getUnsupportedValues()

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

**Returns:**
- unsupported attribute values

---

### Additional Sections

#### Interface AttributeException

```java
public interface
AttributeException
```

Interface

AttributeException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving one or more printing attributes that a particular Print
Service instance does not support. Either the attribute is not supported at
all, or the attribute is supported but the particular specified value is not
supported. The Print Service API does not define any print exception classes
that implement interface

AttributeException

, that being left to the
Print Service implementor's discretion.

public interface

AttributeException

Interface

AttributeException

is a mixin interface which a subclass of

PrintException

can implement to report an error
condition involving one or more printing attributes that a particular Print
Service instance does not support. Either the attribute is not supported at
all, or the attribute is supported but the particular specified value is not
supported. The Print Service API does not define any print exception classes
that implement interface

AttributeException

, that being left to the
Print Service implementor's discretion.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>[]

getUnsupportedAttributes

()

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes.

Attribute

[]

getUnsupportedValues

()

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>[]

getUnsupportedAttributes

()

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes.

Attribute

[]

getUnsupportedValues

()

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

---

#### Method Summary

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes.

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

============ METHOD DETAIL ==========

- Method Detail

- getUnsupportedAttributes

```java
Class
<?>[] getUnsupportedAttributes()
```

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes. The objects in the returned array are
classes that extend the base interface

Attribute

.

**Returns:** unsupported attribute classes

- getUnsupportedValues

```java
Attribute
[] getUnsupportedValues()
```

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

**Returns:** unsupported attribute values

Method Detail

- getUnsupportedAttributes

```java
Class
<?>[] getUnsupportedAttributes()
```

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes. The objects in the returned array are
classes that extend the base interface

Attribute

.

**Returns:** unsupported attribute classes

- getUnsupportedValues

```java
Attribute
[] getUnsupportedValues()
```

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

**Returns:** unsupported attribute values

---

#### Method Detail

getUnsupportedAttributes

```java
Class
<?>[] getUnsupportedAttributes()
```

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes. The objects in the returned array are
classes that extend the base interface

Attribute

.

**Returns:** unsupported attribute classes

---

#### getUnsupportedAttributes

Class

<?>[] getUnsupportedAttributes()

Returns the array of printing attribute classes for which the Print
Service instance does not support the attribute at all, or

null

if there are no such attributes. The objects in the returned array are
classes that extend the base interface

Attribute

.

getUnsupportedValues

```java
Attribute
[] getUnsupportedValues()
```

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

**Returns:** unsupported attribute values

---

#### getUnsupportedValues

Attribute

[] getUnsupportedValues()

Returns the array of printing attributes for which the Print Service
instance supports the attribute but does not support that particular
value of the attribute, or

null

if there are no such attribute
values.

---

