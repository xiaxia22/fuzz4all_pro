# Interface DescriptorRead

**Source:** `java.management\javax\management\DescriptorRead.html`

### Class Description

```java
public interface
DescriptorRead
```

Interface to read the Descriptor of a management interface element
such as an MBeanInfo.

**All Known Subinterfaces:** DescriptorAccess

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Descriptor
getDescriptor()

Returns a copy of Descriptor.

**Returns:**
- Descriptor associated with the component implementing this interface.
The return value is never null, but the returned descriptor may be empty.

---

### Additional Sections

#### Interface DescriptorRead

**All Known Subinterfaces:** DescriptorAccess

**All Known Implementing Classes:** MBeanAttributeInfo

,

MBeanConstructorInfo

,

MBeanFeatureInfo

,

MBeanInfo

,

MBeanNotificationInfo

,

MBeanOperationInfo

,

MBeanParameterInfo

,

ModelMBeanAttributeInfo

,

ModelMBeanConstructorInfo

,

ModelMBeanInfoSupport

,

ModelMBeanNotificationInfo

,

ModelMBeanOperationInfo

,

OpenMBeanAttributeInfoSupport

,

OpenMBeanConstructorInfoSupport

,

OpenMBeanInfoSupport

,

OpenMBeanOperationInfoSupport

,

OpenMBeanParameterInfoSupport

```java
public interface
DescriptorRead
```

Interface to read the Descriptor of a management interface element
such as an MBeanInfo.

**Since:** 1.6

public interface

DescriptorRead

Interface to read the Descriptor of a management interface element
such as an MBeanInfo.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Descriptor

getDescriptor

()

Returns a copy of Descriptor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Descriptor

getDescriptor

()

Returns a copy of Descriptor.

---

#### Method Summary

Returns a copy of Descriptor.

============ METHOD DETAIL ==========

- Method Detail

- getDescriptor

```java
Descriptor
getDescriptor()
```

Returns a copy of Descriptor.

**Returns:** Descriptor associated with the component implementing this interface.
The return value is never null, but the returned descriptor may be empty.

Method Detail

- getDescriptor

```java
Descriptor
getDescriptor()
```

Returns a copy of Descriptor.

**Returns:** Descriptor associated with the component implementing this interface.
The return value is never null, but the returned descriptor may be empty.

---

#### Method Detail

getDescriptor

```java
Descriptor
getDescriptor()
```

Returns a copy of Descriptor.

**Returns:** Descriptor associated with the component implementing this interface.
The return value is never null, but the returned descriptor may be empty.

---

#### getDescriptor

Descriptor

getDescriptor()

Returns a copy of Descriptor.

---

