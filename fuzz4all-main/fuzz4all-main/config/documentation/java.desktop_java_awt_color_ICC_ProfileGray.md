# Class ICC_ProfileGray

**Source:** `java.desktop\java\awt\color\ICC_ProfileGray.html`

### Class Description

```java
public class
ICC_ProfileGray

extends
ICC_Profile
```

A subclass of the ICC_Profile class which represents profiles
which meet the following criteria: the color space type of the
profile is TYPE_GRAY and the profile includes the grayTRCTag and
mediaWhitePointTag tags. Examples of this kind of profile are
monochrome input profiles, monochrome display profiles, and
monochrome output profiles. The getInstance methods in the
ICC_Profile class will
return an ICC_ProfileGray object when the above conditions are
met. The advantage of this class is that it provides a lookup
table that Java or native methods may be able to use directly to
optimize color conversion in some cases.

To transform from a GRAY device profile color space to the CIEXYZ Profile
Connection Space, the device gray component is transformed by
a lookup through the tone reproduction curve (TRC). The result is
treated as the achromatic component of the PCS.

```java
PCSY = grayTRC[deviceGray]
```

The inverse transform is done by converting the PCS Y components to
device Gray via the inverse of the grayTRC.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public float[] getMediaWhitePoint()

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

**Returns:**
- an array containing the components of the
mediaWhitePointTag in the ICC profile.

---

#### public float getGamma()

Returns a gamma value representing the tone reproduction
curve (TRC). If the profile represents the TRC as a table rather
than a single gamma value, then an exception is thrown. In this
case the actual table can be obtained via getTRC(). When
using a gamma value, the PCS Y component is computed as follows:

```java
gamma
PCSY = deviceGray
```

**Returns:**
- the gamma value as a float.

**Throws:**
- ProfileDataException

- if the profile does not specify
the TRC as a single gamma value.

---

#### public short[] getTRC()

Returns the TRC as an array of shorts. If the profile has
specified the TRC as linear (gamma = 1.0) or as a simple gamma
value, this method throws an exception, and the getGamma() method
should be used to get the gamma value. Otherwise the short array
returned here represents a lookup table where the input Gray value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation may be used to generate output values for
input values which do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF, i.e. the values are really unsigned
short values, although they are returned in a short array.

**Returns:**
- a short array representing the TRC.

**Throws:**
- ProfileDataException

- if the profile does not specify
the TRC as a table.

---

### Additional Sections

#### Class ICC_ProfileGray

java.lang.Object

- java.awt.color.ICC_Profile
- - java.awt.color.ICC_ProfileGray

java.awt.color.ICC_Profile

- java.awt.color.ICC_ProfileGray

java.awt.color.ICC_ProfileGray

**All Implemented Interfaces:** Serializable

```java
public class
ICC_ProfileGray

extends
ICC_Profile
```

A subclass of the ICC_Profile class which represents profiles
which meet the following criteria: the color space type of the
profile is TYPE_GRAY and the profile includes the grayTRCTag and
mediaWhitePointTag tags. Examples of this kind of profile are
monochrome input profiles, monochrome display profiles, and
monochrome output profiles. The getInstance methods in the
ICC_Profile class will
return an ICC_ProfileGray object when the above conditions are
met. The advantage of this class is that it provides a lookup
table that Java or native methods may be able to use directly to
optimize color conversion in some cases.

To transform from a GRAY device profile color space to the CIEXYZ Profile
Connection Space, the device gray component is transformed by
a lookup through the tone reproduction curve (TRC). The result is
treated as the achromatic component of the PCS.

```java
PCSY = grayTRC[deviceGray]
```

The inverse transform is done by converting the PCS Y components to
device Gray via the inverse of the grayTRC.

**See Also:** Serialized Form

public class

ICC_ProfileGray

extends

ICC_Profile

A subclass of the ICC_Profile class which represents profiles
which meet the following criteria: the color space type of the
profile is TYPE_GRAY and the profile includes the grayTRCTag and
mediaWhitePointTag tags. Examples of this kind of profile are
monochrome input profiles, monochrome display profiles, and
monochrome output profiles. The getInstance methods in the
ICC_Profile class will
return an ICC_ProfileGray object when the above conditions are
met. The advantage of this class is that it provides a lookup
table that Java or native methods may be able to use directly to
optimize color conversion in some cases.

To transform from a GRAY device profile color space to the CIEXYZ Profile
Connection Space, the device gray component is transformed by
a lookup through the tone reproduction curve (TRC). The result is
treated as the achromatic component of the PCS.

```java
PCSY = grayTRC[deviceGray]
```

The inverse transform is done by converting the PCS Y components to
device Gray via the inverse of the grayTRC.

To transform from a GRAY device profile color space to the CIEXYZ Profile
Connection Space, the device gray component is transformed by
a lookup through the tone reproduction curve (TRC). The result is
treated as the achromatic component of the PCS.

```java
PCSY = grayTRC[deviceGray]
```

The inverse transform is done by converting the PCS Y components to
device Gray via the inverse of the grayTRC.

PCSY = grayTRC[deviceGray]

=========== FIELD SUMMARY ===========

- Field Summary

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

()

Returns a gamma value representing the tone reproduction
curve (TRC).

float[]

getMediaWhitePoint

()

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

short[]

getTRC

()

Returns the TRC as an array of shorts.

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

()

Returns a gamma value representing the tone reproduction
curve (TRC).

float[]

getMediaWhitePoint

()

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

short[]

getTRC

()

Returns the TRC as an array of shorts.

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

Returns a gamma value representing the tone reproduction
curve (TRC).

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

Returns the TRC as an array of shorts.

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

============ METHOD DETAIL ==========

- Method Detail

- getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

**Returns:** an array containing the components of the
mediaWhitePointTag in the ICC profile.

- getGamma

```java
public float getGamma()
```

Returns a gamma value representing the tone reproduction
curve (TRC). If the profile represents the TRC as a table rather
than a single gamma value, then an exception is thrown. In this
case the actual table can be obtained via getTRC(). When
using a gamma value, the PCS Y component is computed as follows:

```java
gamma
PCSY = deviceGray
```

**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a single gamma value.

- getTRC

```java
public short[] getTRC()
```

Returns the TRC as an array of shorts. If the profile has
specified the TRC as linear (gamma = 1.0) or as a simple gamma
value, this method throws an exception, and the getGamma() method
should be used to get the gamma value. Otherwise the short array
returned here represents a lookup table where the input Gray value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation may be used to generate output values for
input values which do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF, i.e. the values are really unsigned
short values, although they are returned in a short array.

**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a table.

Method Detail

- getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

**Returns:** an array containing the components of the
mediaWhitePointTag in the ICC profile.

- getGamma

```java
public float getGamma()
```

Returns a gamma value representing the tone reproduction
curve (TRC). If the profile represents the TRC as a table rather
than a single gamma value, then an exception is thrown. In this
case the actual table can be obtained via getTRC(). When
using a gamma value, the PCS Y component is computed as follows:

```java
gamma
PCSY = deviceGray
```

**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a single gamma value.

- getTRC

```java
public short[] getTRC()
```

Returns the TRC as an array of shorts. If the profile has
specified the TRC as linear (gamma = 1.0) or as a simple gamma
value, this method throws an exception, and the getGamma() method
should be used to get the gamma value. Otherwise the short array
returned here represents a lookup table where the input Gray value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation may be used to generate output values for
input values which do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF, i.e. the values are really unsigned
short values, although they are returned in a short array.

**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a table.

---

#### Method Detail

getMediaWhitePoint

```java
public float[] getMediaWhitePoint()
```

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

**Returns:** an array containing the components of the
mediaWhitePointTag in the ICC profile.

---

#### getMediaWhitePoint

public float[] getMediaWhitePoint()

Returns a float array of length 3 containing the X, Y, and Z
components of the mediaWhitePointTag in the ICC profile.

getGamma

```java
public float getGamma()
```

Returns a gamma value representing the tone reproduction
curve (TRC). If the profile represents the TRC as a table rather
than a single gamma value, then an exception is thrown. In this
case the actual table can be obtained via getTRC(). When
using a gamma value, the PCS Y component is computed as follows:

```java
gamma
PCSY = deviceGray
```

**Returns:** the gamma value as a float.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a single gamma value.

---

#### getGamma

public float getGamma()

Returns a gamma value representing the tone reproduction
curve (TRC). If the profile represents the TRC as a table rather
than a single gamma value, then an exception is thrown. In this
case the actual table can be obtained via getTRC(). When
using a gamma value, the PCS Y component is computed as follows:

```java
gamma
PCSY = deviceGray
```

gamma
PCSY = deviceGray

getTRC

```java
public short[] getTRC()
```

Returns the TRC as an array of shorts. If the profile has
specified the TRC as linear (gamma = 1.0) or as a simple gamma
value, this method throws an exception, and the getGamma() method
should be used to get the gamma value. Otherwise the short array
returned here represents a lookup table where the input Gray value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation may be used to generate output values for
input values which do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF, i.e. the values are really unsigned
short values, although they are returned in a short array.

**Returns:** a short array representing the TRC.
**Throws:** ProfileDataException

- if the profile does not specify
the TRC as a table.

---

#### getTRC

public short[] getTRC()

Returns the TRC as an array of shorts. If the profile has
specified the TRC as linear (gamma = 1.0) or as a simple gamma
value, this method throws an exception, and the getGamma() method
should be used to get the gamma value. Otherwise the short array
returned here represents a lookup table where the input Gray value
is conceptually in the range [0.0, 1.0]. Value 0.0 maps
to array index 0 and value 1.0 maps to array index length-1.
Interpolation may be used to generate output values for
input values which do not map exactly to an index in the
array. Output values also map linearly to the range [0.0, 1.0].
Value 0.0 is represented by an array value of 0x0000 and
value 1.0 by 0xFFFF, i.e. the values are really unsigned
short values, although they are returned in a short array.

---

