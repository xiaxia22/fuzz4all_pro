# Class ICC_ProfileRGB

**Source:** `java.desktop\java\awt\color\ICC_ProfileRGB.html`

### Class Description

```java
public class
ICC_ProfileRGB

extends
ICC_Profile
```

The ICC_ProfileRGB class is a subclass of the ICC_Profile class
that represents profiles which meet the following criteria:

- The profile's color space type is RGB.
- The profile includes the

redColorantTag

,

greenColorantTag

,

blueColorantTag

,

redTRCTag

,

greenTRCTag

,

blueTRCTag

, and

mediaWhitePointTag

tags.

The

ICC_Profile getInstance

method will
return an

ICC_ProfileRGB

object when these conditions are met.
Three-component, matrix-based input profiles and RGB display profiles are
examples of this type of profile.

This profile class provides color transform matrices and lookup tables
that Java or native methods can use directly to
optimize color conversion in some cases.

To transform from a device profile color space to the CIEXYZ Profile
Connection Space, each device color component is first linearized by
a lookup through the corresponding tone reproduction curve (TRC).
The resulting linear RGB components are converted to the CIEXYZ PCS
using a a 3x3 matrix constructed from the RGB colorants.

```java
linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]
```

The inverse transform is performed by converting PCS XYZ components to linear
RGB components through the inverse of the above 3x3 matrix, and then converting
linear RGB to device RGB through inverses of the TRCs.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int REDCOMPONENT

Used to get a gamma value or TRC for the red component.

**See Also:**
- Constant Field Values

---

#### public static final int GREENCOMPONENT

Used to get a gamma value or TRC for the green component.

**See Also:**
- Constant Field Values

---

#### public static final int BLUECOMPONENT

Used to get a gamma value or TRC for the blue component.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public float[] getMediaWhitePoint()

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

**Returns:**
- A 3-element

float

array containing the x, y,
and z components of the profile's

mediaWhitePointTag

.

---

#### public float[][] getMatrix()

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

**Returns:**
- A 3x3

float

array that contains the x, y, and z
components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

---

#### public float getGamma​(int component)

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component. The component parameter
must be one of REDCOMPONENT, GREENCOMPONENT, or BLUECOMPONENT.

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

**Parameters:**
- component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve

**Returns:**
- the gamma value as a float.

**Throws:**
- ProfileDataException

- if the profile does not specify
the corresponding TRC as a single gamma value.

---

#### public short[] getTRC​(int component)

Returns the TRC for a particular component as an array.
Component must be

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
Otherwise the returned array
represents a lookup table where the input component value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation might be used to generate output values for
input values that do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF. In other words, the values are really unsigned

short

values even though they are returned in a

short

array.

If the profile has specified the corresponding TRC
as linear (gamma = 1.0) or as a simple gamma value, this method
throws an exception. In this case, the

getGamma(int)

method should be used to get the gamma value.

**Parameters:**
- component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve:

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.

**Returns:**
- a short array representing the TRC.

**Throws:**
- ProfileDataException

- if the profile does not specify
the corresponding TRC as a table.

---

### Additional Sections

#### Class ICC_ProfileRGB

java.lang.Object

- java.awt.color.ICC_Profile
- - java.awt.color.ICC_ProfileRGB

java.awt.color.ICC_Profile

- java.awt.color.ICC_ProfileRGB

java.awt.color.ICC_ProfileRGB

**All Implemented Interfaces:** Serializable

```java
public class
ICC_ProfileRGB

extends
ICC_Profile
```

The ICC_ProfileRGB class is a subclass of the ICC_Profile class
that represents profiles which meet the following criteria:

- The profile's color space type is RGB.
- The profile includes the

redColorantTag

,

greenColorantTag

,

blueColorantTag

,

redTRCTag

,

greenTRCTag

,

blueTRCTag

, and

mediaWhitePointTag

tags.

The

ICC_Profile getInstance

method will
return an

ICC_ProfileRGB

object when these conditions are met.
Three-component, matrix-based input profiles and RGB display profiles are
examples of this type of profile.

This profile class provides color transform matrices and lookup tables
that Java or native methods can use directly to
optimize color conversion in some cases.

To transform from a device profile color space to the CIEXYZ Profile
Connection Space, each device color component is first linearized by
a lookup through the corresponding tone reproduction curve (TRC).
The resulting linear RGB components are converted to the CIEXYZ PCS
using a a 3x3 matrix constructed from the RGB colorants.

```java
linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]
```

The inverse transform is performed by converting PCS XYZ components to linear
RGB components through the inverse of the above 3x3 matrix, and then converting
linear RGB to device RGB through inverses of the TRCs.

**See Also:** Serialized Form

public class

ICC_ProfileRGB

extends

ICC_Profile

The ICC_ProfileRGB class is a subclass of the ICC_Profile class
that represents profiles which meet the following criteria:

- The profile's color space type is RGB.
- The profile includes the

redColorantTag

,

greenColorantTag

,

blueColorantTag

,

redTRCTag

,

greenTRCTag

,

blueTRCTag

, and

mediaWhitePointTag

tags.

The

ICC_Profile getInstance

method will
return an

ICC_ProfileRGB

object when these conditions are met.
Three-component, matrix-based input profiles and RGB display profiles are
examples of this type of profile.

This profile class provides color transform matrices and lookup tables
that Java or native methods can use directly to
optimize color conversion in some cases.

To transform from a device profile color space to the CIEXYZ Profile
Connection Space, each device color component is first linearized by
a lookup through the corresponding tone reproduction curve (TRC).
The resulting linear RGB components are converted to the CIEXYZ PCS
using a a 3x3 matrix constructed from the RGB colorants.

```java
linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]
```

The inverse transform is performed by converting PCS XYZ components to linear
RGB components through the inverse of the above 3x3 matrix, and then converting
linear RGB to device RGB through inverses of the TRCs.

The profile's color space type is RGB.

The profile includes the

redColorantTag

,

greenColorantTag

,

blueColorantTag

,

redTRCTag

,

greenTRCTag

,

blueTRCTag

, and

mediaWhitePointTag

tags.

This profile class provides color transform matrices and lookup tables
that Java or native methods can use directly to
optimize color conversion in some cases.

To transform from a device profile color space to the CIEXYZ Profile
Connection Space, each device color component is first linearized by
a lookup through the corresponding tone reproduction curve (TRC).
The resulting linear RGB components are converted to the CIEXYZ PCS
using a a 3x3 matrix constructed from the RGB colorants.

```java
linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]
```

The inverse transform is performed by converting PCS XYZ components to linear
RGB components through the inverse of the above 3x3 matrix, and then converting
linear RGB to device RGB through inverses of the TRCs.

To transform from a device profile color space to the CIEXYZ Profile
Connection Space, each device color component is first linearized by
a lookup through the corresponding tone reproduction curve (TRC).
The resulting linear RGB components are converted to the CIEXYZ PCS
using a a 3x3 matrix constructed from the RGB colorants.

```java
linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]
```

The inverse transform is performed by converting PCS XYZ components to linear
RGB components through the inverse of the above 3x3 matrix, and then converting
linear RGB to device RGB through inverses of the TRCs.

linearR = redTRC[deviceR]

linearG = greenTRC[deviceG]

linearB = blueTRC[deviceB]

_ _ _ _ _ _
[ PCSX ] [ redColorantX greenColorantX blueColorantX ] [ linearR ]
[ ] [ ] [ ]
[ PCSY ] = [ redColorantY greenColorantY blueColorantY ] [ linearG ]
[ ] [ ] [ ]
[_ PCSZ _] [_ redColorantZ greenColorantZ blueColorantZ _] [_ linearB _]

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BLUECOMPONENT

Used to get a gamma value or TRC for the blue component.

static int

GREENCOMPONENT

Used to get a gamma value or TRC for the green component.

static int

REDCOMPONENT

Used to get a gamma value or TRC for the red component.

- Fields declared in class java.awt.color.

ICC_Profile

CLASS_ABSTRACT

,

CLASS_COLORSPACECONVERSION

,

CLASS_DEVICELINK

,

CLASS_DISPLAY

,

CLASS_INPUT

,

CLASS_NAMEDCOLOR

,

CLASS_OUTPUT

,

icAbsoluteColorimetric

,

icCurveCount

,

icCurveData

,

icHdrAttributes

,

icHdrCmmId

,

icHdrColorSpace

,

icHdrCreator

,

icHdrDate

,

icHdrDeviceClass

,

icHdrFlags

,

icHdrIlluminant

,

icHdrMagic

,

icHdrManufacturer

,

icHdrModel

,

icHdrPcs

,

icHdrPlatform

,

icHdrProfileID

,

icHdrRenderingIntent

,

icHdrSize

,

icHdrVersion

,

icICCAbsoluteColorimetric

,

icMediaRelativeColorimetric

,

icPerceptual

,

icRelativeColorimetric

,

icSaturation

,

icSigAbstractClass

,

icSigAToB0Tag

,

icSigAToB1Tag

,

icSigAToB2Tag

,

icSigBlueColorantTag

,

icSigBlueMatrixColumnTag

,

icSigBlueTRCTag

,

icSigBToA0Tag

,

icSigBToA1Tag

,

icSigBToA2Tag

,

icSigCalibrationDateTimeTag

,

icSigCharTargetTag

,

icSigChromaticAdaptationTag

,

icSigChromaticityTag

,

icSigCmyData

,

icSigCmykData

,

icSigColorantOrderTag

,

icSigColorantTableTag

,

icSigColorSpaceClass

,

icSigCopyrightTag

,

icSigCrdInfoTag

,

icSigDeviceMfgDescTag

,

icSigDeviceModelDescTag

,

icSigDeviceSettingsTag

,

icSigDisplayClass

,

icSigGamutTag

,

icSigGrayData

,

icSigGrayTRCTag

,

icSigGreenColorantTag

,

icSigGreenMatrixColumnTag

,

icSigGreenTRCTag

,

icSigHead

,

icSigHlsData

,

icSigHsvData

,

icSigInputClass

,

icSigLabData

,

icSigLinkClass

,

icSigLuminanceTag

,

icSigLuvData

,

icSigMeasurementTag

,

icSigMediaBlackPointTag

,

icSigMediaWhitePointTag

,

icSigNamedColor2Tag

,

icSigNamedColorClass

,

icSigOutputClass

,

icSigOutputResponseTag

,

icSigPreview0Tag

,

icSigPreview1Tag

,

icSigPreview2Tag

,

icSigProfileDescriptionTag

,

icSigProfileSequenceDescTag

,

icSigPs2CRD0Tag

,

icSigPs2CRD1Tag

,

icSigPs2CRD2Tag

,

icSigPs2CRD3Tag

,

icSigPs2CSATag

,

icSigPs2RenderingIntentTag

,

icSigRedColorantTag

,

icSigRedMatrixColumnTag

,

icSigRedTRCTag

,

icSigRgbData

,

icSigScreeningDescTag

,

icSigScreeningTag

,

icSigSpace2CLR

,

icSigSpace3CLR

,

icSigSpace4CLR

,

icSigSpace5CLR

,

icSigSpace6CLR

,

icSigSpace7CLR

,

icSigSpace8CLR

,

icSigSpace9CLR

,

icSigSpaceACLR

,

icSigSpaceBCLR

,

icSigSpaceCCLR

,

icSigSpaceDCLR

,

icSigSpaceECLR

,

icSigSpaceFCLR

,

icSigTechnologyTag

,

icSigUcrBgTag

,

icSigViewingCondDescTag

,

icSigViewingConditionsTag

,

icSigXYZData

,

icSigYCbCrData

,

icSigYxyData

,

icTagReserved

,

icTagType

,

icXYZNumberX

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getGamma

​(int component)

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component.

float[][]

getMatrix

()

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

float[]

getMediaWhitePoint

()

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

short[]

getTRC

​(int component)

Returns the TRC for a particular component as an array.

- Methods declared in class java.awt.color.

ICC_Profile

finalize

,

getColorSpaceType

,

getData

,

getData

,

getInstance

,

getInstance

,

getInstance

,

getInstance

,

getMajorVersion

,

getMinorVersion

,

getNumComponents

,

getPCSType

,

getProfileClass

,

readResolve

,

setData

,

write

,

write

- Methods declared in class java.lang.

Object

clone

,

equals

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

static int

BLUECOMPONENT

Used to get a gamma value or TRC for the blue component.

static int

GREENCOMPONENT

Used to get a gamma value or TRC for the green component.

static int

REDCOMPONENT

Used to get a gamma value or TRC for the red component.

- Fields declared in class java.awt.color.

ICC_Profile

CLASS_ABSTRACT

,

CLASS_COLORSPACECONVERSION

,

CLASS_DEVICELINK

,

CLASS_DISPLAY

,

CLASS_INPUT

,

CLASS_NAMEDCOLOR

,

CLASS_OUTPUT

,

icAbsoluteColorimetric

,

icCurveCount

,

icCurveData

,

icHdrAttributes

,

icHdrCmmId

,

icHdrColorSpace

,

icHdrCreator

,

icHdrDate

,

icHdrDeviceClass

,

icHdrFlags

,

icHdrIlluminant

,

icHdrMagic

,

icHdrManufacturer

,

icHdrModel

,

icHdrPcs

,

icHdrPlatform

,

icHdrProfileID

,

icHdrRenderingIntent

,

icHdrSize

,

icHdrVersion

,

icICCAbsoluteColorimetric

,

icMediaRelativeColorimetric

,

icPerceptual

,

icRelativeColorimetric

,

icSaturation

,

icSigAbstractClass

,

icSigAToB0Tag

,

icSigAToB1Tag

,

icSigAToB2Tag

,

icSigBlueColorantTag

,

icSigBlueMatrixColumnTag

,

icSigBlueTRCTag

,

icSigBToA0Tag

,

icSigBToA1Tag

,

icSigBToA2Tag

,

icSigCalibrationDateTimeTag

,

icSigCharTargetTag

,

icSigChromaticAdaptationTag

,

icSigChromaticityTag

,

icSigCmyData

,

icSigCmykData

,

icSigColorantOrderTag

,

icSigColorantTableTag

,

icSigColorSpaceClass

,

icSigCopyrightTag

,

icSigCrdInfoTag

,

icSigDeviceMfgDescTag

,

icSigDeviceModelDescTag

,

icSigDeviceSettingsTag

,

icSigDisplayClass

,

icSigGamutTag

,

icSigGrayData

,

icSigGrayTRCTag

,

icSigGreenColorantTag

,

icSigGreenMatrixColumnTag

,

icSigGreenTRCTag

,

icSigHead

,

icSigHlsData

,

icSigHsvData

,

icSigInputClass

,

icSigLabData

,

icSigLinkClass

,

icSigLuminanceTag

,

icSigLuvData

,

icSigMeasurementTag

,

icSigMediaBlackPointTag

,

icSigMediaWhitePointTag

,

icSigNamedColor2Tag

,

icSigNamedColorClass

,

icSigOutputClass

,

icSigOutputResponseTag

,

icSigPreview0Tag

,

icSigPreview1Tag

,

icSigPreview2Tag

,

icSigProfileDescriptionTag

,

icSigProfileSequenceDescTag

,

icSigPs2CRD0Tag

,

icSigPs2CRD1Tag

,

icSigPs2CRD2Tag

,

icSigPs2CRD3Tag

,

icSigPs2CSATag

,

icSigPs2RenderingIntentTag

,

icSigRedColorantTag

,

icSigRedMatrixColumnTag

,

icSigRedTRCTag

,

icSigRgbData

,

icSigScreeningDescTag

,

icSigScreeningTag

,

icSigSpace2CLR

,

icSigSpace3CLR

,

icSigSpace4CLR

,

icSigSpace5CLR

,

icSigSpace6CLR

,

icSigSpace7CLR

,

icSigSpace8CLR

,

icSigSpace9CLR

,

icSigSpaceACLR

,

icSigSpaceBCLR

,

icSigSpaceCCLR

,

icSigSpaceDCLR

,

icSigSpaceECLR

,

icSigSpaceFCLR

,

icSigTechnologyTag

,

icSigUcrBgTag

,

icSigViewingCondDescTag

,

icSigViewingConditionsTag

,

icSigXYZData

,

icSigYCbCrData

,

icSigYxyData

,

icTagReserved

,

icTagType

,

icXYZNumberX

---

#### Field Summary

Used to get a gamma value or TRC for the blue component.

Used to get a gamma value or TRC for the green component.

Used to get a gamma value or TRC for the red component.

Fields declared in class java.awt.color.

ICC_Profile

CLASS_ABSTRACT

,

CLASS_COLORSPACECONVERSION

,

CLASS_DEVICELINK

,

CLASS_DISPLAY

,

CLASS_INPUT

,

CLASS_NAMEDCOLOR

,

CLASS_OUTPUT

,

icAbsoluteColorimetric

,

icCurveCount

,

icCurveData

,

icHdrAttributes

,

icHdrCmmId

,

icHdrColorSpace

,

icHdrCreator

,

icHdrDate

,

icHdrDeviceClass

,

icHdrFlags

,

icHdrIlluminant

,

icHdrMagic

,

icHdrManufacturer

,

icHdrModel

,

icHdrPcs

,

icHdrPlatform

,

icHdrProfileID

,

icHdrRenderingIntent

,

icHdrSize

,

icHdrVersion

,

icICCAbsoluteColorimetric

,

icMediaRelativeColorimetric

,

icPerceptual

,

icRelativeColorimetric

,

icSaturation

,

icSigAbstractClass

,

icSigAToB0Tag

,

icSigAToB1Tag

,

icSigAToB2Tag

,

icSigBlueColorantTag

,

icSigBlueMatrixColumnTag

,

icSigBlueTRCTag

,

icSigBToA0Tag

,

icSigBToA1Tag

,

icSigBToA2Tag

,

icSigCalibrationDateTimeTag

,

icSigCharTargetTag

,

icSigChromaticAdaptationTag

,

icSigChromaticityTag

,

icSigCmyData

,

icSigCmykData

,

icSigColorantOrderTag

,

icSigColorantTableTag

,

icSigColorSpaceClass

,

icSigCopyrightTag

,

icSigCrdInfoTag

,

icSigDeviceMfgDescTag

,

icSigDeviceModelDescTag

,

icSigDeviceSettingsTag

,

icSigDisplayClass

,

icSigGamutTag

,

icSigGrayData

,

icSigGrayTRCTag

,

icSigGreenColorantTag

,

icSigGreenMatrixColumnTag

,

icSigGreenTRCTag

,

icSigHead

,

icSigHlsData

,

icSigHsvData

,

icSigInputClass

,

icSigLabData

,

icSigLinkClass

,

icSigLuminanceTag

,

icSigLuvData

,

icSigMeasurementTag

,

icSigMediaBlackPointTag

,

icSigMediaWhitePointTag

,

icSigNamedColor2Tag

,

icSigNamedColorClass

,

icSigOutputClass

,

icSigOutputResponseTag

,

icSigPreview0Tag

,

icSigPreview1Tag

,

icSigPreview2Tag

,

icSigProfileDescriptionTag

,

icSigProfileSequenceDescTag

,

icSigPs2CRD0Tag

,

icSigPs2CRD1Tag

,

icSigPs2CRD2Tag

,

icSigPs2CRD3Tag

,

icSigPs2CSATag

,

icSigPs2RenderingIntentTag

,

icSigRedColorantTag

,

icSigRedMatrixColumnTag

,

icSigRedTRCTag

,

icSigRgbData

,

icSigScreeningDescTag

,

icSigScreeningTag

,

icSigSpace2CLR

,

icSigSpace3CLR

,

icSigSpace4CLR

,

icSigSpace5CLR

,

icSigSpace6CLR

,

icSigSpace7CLR

,

icSigSpace8CLR

,

icSigSpace9CLR

,

icSigSpaceACLR

,

icSigSpaceBCLR

,

icSigSpaceCCLR

,

icSigSpaceDCLR

,

icSigSpaceECLR

,

icSigSpaceFCLR

,

icSigTechnologyTag

,

icSigUcrBgTag

,

icSigViewingCondDescTag

,

icSigViewingConditionsTag

,

icSigXYZData

,

icSigYCbCrData

,

icSigYxyData

,

icTagReserved

,

icTagType

,

icXYZNumberX

---

#### Fields declared in class java.awt.color. ICC_Profile

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getGamma

​(int component)

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component.

float[][]

getMatrix

()

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

float[]

getMediaWhitePoint

()

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

short[]

getTRC

​(int component)

Returns the TRC for a particular component as an array.

- Methods declared in class java.awt.color.

ICC_Profile

finalize

,

getColorSpaceType

,

getData

,

getData

,

getInstance

,

getInstance

,

getInstance

,

getInstance

,

getMajorVersion

,

getMinorVersion

,

getNumComponents

,

getPCSType

,

getProfileClass

,

readResolve

,

setData

,

write

,

write

- Methods declared in class java.lang.

Object

clone

,

equals

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

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component.

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

Returns the TRC for a particular component as an array.

Methods declared in class java.awt.color.

ICC_Profile

finalize

,

getColorSpaceType

,

getData

,

getData

,

getInstance

,

getInstance

,

getInstance

,

getInstance

,

getMajorVersion

,

getMinorVersion

,

getNumComponents

,

getPCSType

,

getProfileClass

,

readResolve

,

setData

,

write

,

write

---

#### Methods declared in class java.awt.color. ICC_Profile

Methods declared in class java.lang.

Object

clone

,

equals

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

- REDCOMPONENT

```java
public static final int REDCOMPONENT
```

Used to get a gamma value or TRC for the red component.

**See Also:** Constant Field Values

- GREENCOMPONENT

```java
public static final int GREENCOMPONENT
```

Used to get a gamma value or TRC for the green component.

**See Also:** Constant Field Values

- BLUECOMPONENT

```java
public static final int BLUECOMPONENT
```

Used to get a gamma value or TRC for the blue component.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

**Returns:** A 3-element

float

array containing the x, y,
and z components of the profile's

mediaWhitePointTag

.

- getMatrix

```java
public float[][] getMatrix()
```

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

**Returns:** A 3x3

float

array that contains the x, y, and z
components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

- getGamma

```java
public float getGamma​(int component)
```

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component. The component parameter
must be one of REDCOMPONENT, GREENCOMPONENT, or BLUECOMPONENT.

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve
**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a single gamma value.

- getTRC

```java
public short[] getTRC​(int component)
```

Returns the TRC for a particular component as an array.
Component must be

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
Otherwise the returned array
represents a lookup table where the input component value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation might be used to generate output values for
input values that do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF. In other words, the values are really unsigned

short

values even though they are returned in a

short

array.

If the profile has specified the corresponding TRC
as linear (gamma = 1.0) or as a simple gamma value, this method
throws an exception. In this case, the

getGamma(int)

method should be used to get the gamma value.

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve:

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a table.

Field Detail

- REDCOMPONENT

```java
public static final int REDCOMPONENT
```

Used to get a gamma value or TRC for the red component.

**See Also:** Constant Field Values

- GREENCOMPONENT

```java
public static final int GREENCOMPONENT
```

Used to get a gamma value or TRC for the green component.

**See Also:** Constant Field Values

- BLUECOMPONENT

```java
public static final int BLUECOMPONENT
```

Used to get a gamma value or TRC for the blue component.

**See Also:** Constant Field Values

---

#### Field Detail

REDCOMPONENT

```java
public static final int REDCOMPONENT
```

Used to get a gamma value or TRC for the red component.

**See Also:** Constant Field Values

---

#### REDCOMPONENT

public static final int REDCOMPONENT

Used to get a gamma value or TRC for the red component.

GREENCOMPONENT

```java
public static final int GREENCOMPONENT
```

Used to get a gamma value or TRC for the green component.

**See Also:** Constant Field Values

---

#### GREENCOMPONENT

public static final int GREENCOMPONENT

Used to get a gamma value or TRC for the green component.

BLUECOMPONENT

```java
public static final int BLUECOMPONENT
```

Used to get a gamma value or TRC for the blue component.

**See Also:** Constant Field Values

---

#### BLUECOMPONENT

public static final int BLUECOMPONENT

Used to get a gamma value or TRC for the blue component.

Method Detail

- getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

**Returns:** A 3-element

float

array containing the x, y,
and z components of the profile's

mediaWhitePointTag

.

- getMatrix

```java
public float[][] getMatrix()
```

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

**Returns:** A 3x3

float

array that contains the x, y, and z
components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

- getGamma

```java
public float getGamma​(int component)
```

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component. The component parameter
must be one of REDCOMPONENT, GREENCOMPONENT, or BLUECOMPONENT.

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve
**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a single gamma value.

- getTRC

```java
public short[] getTRC​(int component)
```

Returns the TRC for a particular component as an array.
Component must be

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
Otherwise the returned array
represents a lookup table where the input component value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation might be used to generate output values for
input values that do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF. In other words, the values are really unsigned

short

values even though they are returned in a

short

array.

If the profile has specified the corresponding TRC
as linear (gamma = 1.0) or as a simple gamma value, this method
throws an exception. In this case, the

getGamma(int)

method should be used to get the gamma value.

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve:

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a table.

---

#### Method Detail

getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

**Returns:** A 3-element

float

array containing the x, y,
and z components of the profile's

mediaWhitePointTag

.

---

#### getMediaWhitePoint

public float[] getMediaWhitePoint()

Returns an array that contains the components of the profile's

mediaWhitePointTag

.

getMatrix

```java
public float[][] getMatrix()
```

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

**Returns:** A 3x3

float

array that contains the x, y, and z
components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

---

#### getMatrix

public float[][] getMatrix()

Returns a 3x3

float

matrix constructed from the
X, Y, and Z components of the profile's

redColorantTag

,

greenColorantTag

, and

blueColorantTag

.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

This matrix can be used for color transforms in the forward
direction of the profile--from the profile color space
to the CIEXYZ PCS.

getGamma

```java
public float getGamma​(int component)
```

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component. The component parameter
must be one of REDCOMPONENT, GREENCOMPONENT, or BLUECOMPONENT.

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve
**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a single gamma value.

---

#### getGamma

public float getGamma​(int component)

Returns a gamma value representing the tone reproduction curve
(TRC) for a particular component. The component parameter
must be one of REDCOMPONENT, GREENCOMPONENT, or BLUECOMPONENT.

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

If the profile
represents the TRC for the corresponding component
as a table rather than a single gamma value, an
exception is thrown. In this case the actual table
can be obtained through the

getTRC(int)

method.
When using a gamma value,
the linear component (R, G, or B) is computed as follows:

```java
gamma
linearComponent = deviceComponent
```

gamma
linearComponent = deviceComponent

getTRC

```java
public short[] getTRC​(int component)
```

Returns the TRC for a particular component as an array.
Component must be

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
Otherwise the returned array
represents a lookup table where the input component value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation might be used to generate output values for
input values that do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF. In other words, the values are really unsigned

short

values even though they are returned in a

short

array.

If the profile has specified the corresponding TRC
as linear (gamma = 1.0) or as a simple gamma value, this method
throws an exception. In this case, the

getGamma(int)

method should be used to get the gamma value.

**Parameters:** component

- The

ICC_ProfileRGB

constant that
represents the component whose TRC you want to retrieve:

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the corresponding TRC as a table.

---

#### getTRC

public short[] getTRC​(int component)

Returns the TRC for a particular component as an array.
Component must be

REDCOMPONENT

,

GREENCOMPONENT

, or

BLUECOMPONENT

.
Otherwise the returned array
represents a lookup table where the input component value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation might be used to generate output values for
input values that do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF. In other words, the values are really unsigned

short

values even though they are returned in a

short

array.

If the profile has specified the corresponding TRC
as linear (gamma = 1.0) or as a simple gamma value, this method
throws an exception. In this case, the

getGamma(int)

method should be used to get the gamma value.

---

