# Interface DescriptorAccess

**Source:** `java.management\javax\management\DescriptorAccess.html`

### Class Description

```java
public interface
DescriptorAccess

extends
DescriptorRead
```

This interface is used to gain access to descriptors of the Descriptor class
which are associated with a JMX component, i.e. MBean, MBeanInfo,
MBeanAttributeInfo, MBeanNotificationInfo,
MBeanOperationInfo, MBeanParameterInfo.

ModelMBeans make extensive use of this interface in ModelMBeanInfo classes.

**All Superinterfaces:** DescriptorRead

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setDescriptor​(
Descriptor
inDescriptor)

Sets Descriptor (full replace).

**Parameters:**
- inDescriptor

- replaces the Descriptor associated with the
component implementing this interface. If the inDescriptor is invalid for the
type of Info object it is being set for, an exception is thrown. If the
inDescriptor is null, then the Descriptor will revert to its default value
which should contain, at a minimum, the descriptor name and descriptorType.

**See Also:**
- DescriptorRead.getDescriptor()

---

### Additional Sections

#### Interface DescriptorAccess

**All Superinterfaces:** DescriptorRead

**All Known Implementing Classes:** ModelMBeanAttributeInfo

,

ModelMBeanConstructorInfo

,

ModelMBeanNotificationInfo

,

ModelMBeanOperationInfo

```java
public interface
DescriptorAccess

extends
DescriptorRead
```

This interface is used to gain access to descriptors of the Descriptor class
which are associated with a JMX component, i.e. MBean, MBeanInfo,
MBeanAttributeInfo, MBeanNotificationInfo,
MBeanOperationInfo, MBeanParameterInfo.

ModelMBeans make extensive use of this interface in ModelMBeanInfo classes.

**Since:** 1.5

public interface

DescriptorAccess

extends

DescriptorRead

This interface is used to gain access to descriptors of the Descriptor class
which are associated with a JMX component, i.e. MBean, MBeanInfo,
MBeanAttributeInfo, MBeanNotificationInfo,
MBeanOperationInfo, MBeanParameterInfo.

ModelMBeans make extensive use of this interface in ModelMBeanInfo classes.

ModelMBeans make extensive use of this interface in ModelMBeanInfo classes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets Descriptor (full replace).

- Methods declared in interface javax.management.

DescriptorRead

getDescriptor

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

setDescriptor

​(

Descriptor

inDescriptor)

Sets Descriptor (full replace).

- Methods declared in interface javax.management.

DescriptorRead

getDescriptor

---

#### Method Summary

Sets Descriptor (full replace).

Methods declared in interface javax.management.

DescriptorRead

getDescriptor

---

#### Methods declared in interface javax.management. DescriptorRead

============ METHOD DETAIL ==========

- Method Detail

- setDescriptor

```java
void setDescriptor​(
Descriptor
inDescriptor)
```

Sets Descriptor (full replace).

**Parameters:** inDescriptor

- replaces the Descriptor associated with the
component implementing this interface. If the inDescriptor is invalid for the
type of Info object it is being set for, an exception is thrown. If the
inDescriptor is null, then the Descriptor will revert to its default value
which should contain, at a minimum, the descriptor name and descriptorType.
**See Also:** DescriptorRead.getDescriptor()

Method Detail

- setDescriptor

```java
void setDescriptor​(
Descriptor
inDescriptor)
```

Sets Descriptor (full replace).

**Parameters:** inDescriptor

- replaces the Descriptor associated with the
component implementing this interface. If the inDescriptor is invalid for the
type of Info object it is being set for, an exception is thrown. If the
inDescriptor is null, then the Descriptor will revert to its default value
which should contain, at a minimum, the descriptor name and descriptorType.
**See Also:** DescriptorRead.getDescriptor()

---

#### Method Detail

setDescriptor

```java
void setDescriptor​(
Descriptor
inDescriptor)
```

Sets Descriptor (full replace).

**Parameters:** inDescriptor

- replaces the Descriptor associated with the
component implementing this interface. If the inDescriptor is invalid for the
type of Info object it is being set for, an exception is thrown. If the
inDescriptor is null, then the Descriptor will revert to its default value
which should contain, at a minimum, the descriptor name and descriptorType.
**See Also:** DescriptorRead.getDescriptor()

---

#### setDescriptor

void setDescriptor​(

Descriptor

inDescriptor)

Sets Descriptor (full replace).

---

