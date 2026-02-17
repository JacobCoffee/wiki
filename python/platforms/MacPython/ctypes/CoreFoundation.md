# MacPython/ctypes/CoreFoundation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here\'s a rendering of [CoreFoundation](./CoreFoundation.html) types for ctypes, by Thomas Heller\'s xml2py tool. This was done with OS X 10.4.10 on a PowerPC Mac on 10/23/2007.

    from ctypes import *



    kCFSocketDataCallBack = 3
    kCFStringEncodingISO_2022_CN_EXT = 2097
    kCFStringEncodingMacCroatian = 36
    kCFStreamEventHasBytesAvailable = 2
    kCFStreamStatusError = 7
    kCFStringEncodingWindowsLatin5 = 1284
    kCFStringEncodingNonLossyASCII = 3071
    kCFNumberFloat64Type = 6
    kCFURLComponentPort = 9
    kCFStringEncodingMacThai = 21
    kCFNumberFormatterPadBeforeSuffix = 2
    kCFRunLoopAfterWaiting = 64
    kCFCompareNumerically = 64
    kCFStringEncodingMacChineseSimp = 25
    kCFStringEncodingISOLatin5 = 521
    kCFStringEncodingMacJapanese = 1
    kCFURLComponentResourceSpecifier = 4
    kCFCompareAnchored = 8
    kCFStreamStatusOpen = 2
    kCFStringEncodingISO_2022_CN = 2096
    kCFStringEncodingNextStepLatin = 2817
    kCFStringEncodingMacBurmese = 19
    kCFXMLStatusParseSuccessful = 0
    kCFRunLoopExit = 128
    kCFStringEncodingDOSGreek2 = 1052
    kCFSocketReadCallBack = 1
    kCFXMLEntityTypeParsedExternal = 2
    kCFStringEncodingMacVietnamese = 30
    kCFCalendarUnitWeekdayOrdinal = 1024
    kCFStringEncodingEBCDIC_US = 3073
    kCFCharacterSetPunctuation = 11
    kCFStreamErrorDomainPOSIX = 1
    kCFStringEncodingDOSKorean = 1058
    kCFURLRemoteHostUnavailableError = -14
    kCFStringEncodingISOLatin4 = 516
    kCFXMLNodeTypeElementTypeDeclaration = 14
    kCFCharacterSetDecomposable = 9
    kCFNumberFormatterPercentStyle = 3
    kCFNumberFormatterNoStyle = 0
    kCFStringEncodingShiftJIS_X0213_00 = 1576
    kCFCharacterSetLetter = 5
    kCFSocketAutomaticallyReenableReadCallBack = 1
    kCFStringEncodingMacKhmer = 20
    kCFStringEncodingCNS_11643_92_P3 = 1619
    kCFStringEncodingISOLatin1 = 513
    kCFXMLNodeCurrentVersion = 1
    kCFXMLErrorElementlessDocument = 11
    kCFCalendarUnitDay = 16
    kCFCharacterSetLowercaseLetter = 6
    kCFStringEncodingBig5_HKSCS_1999 = 2566
    kCFCompareEqualTo = 0
    kCFDateFormatterLongStyle = 3
    kCFStringEncodingDOSRussian = 1051
    CFByteOrderUnknown = 0
    kCFStringEncodingMacGujarati = 11
    kCFStringEncodingMacInuit = 236
    kCFStringEncodingNextStepJapanese = 2818
    kCFXMLNodeTypeDocumentFragment = 8
    kCFRunLoopRunStopped = 2
    kCFStringEncodingJIS_X0201_76 = 1568
    kCFStringEncodingMacKannada = 16
    kCFSocketAutomaticallyReenableWriteCallBack = 8
    kCFStringEncodingGB_18030_2000 = 1586
    kCFStringEncodingDOSLatinUS = 1024
    kCFStringEncodingMacGreek = 6
    kCFNotFound = -1
    kCFXMLErrorMalformedCloseTag = 8
    kCFPropertyListMutableContainers = 1
    kCFStringEncodingMacTelugu = 15
    kCFXMLNodeTypeAttribute = 3
    CFByteOrderLittleEndian = 1
    kCFStringEncodingShiftJIS = 2561
    kCFNumberFormatterRoundHalfUp = 6
    kCFStringEncodingDOSIcelandic = 1046
    kCFRunLoopBeforeSources = 4
    kCFXMLErrorMalformedStartTag = 9
    kCFStringEncodingISOLatinCyrillic = 517
    kCFStringEncodingMacRomanian = 38
    kCFXMLErrorUnexpectedEOF = 1
    kCFStringEncodingWindowsArabic = 1286
    kCFGregorianUnitsYears = 1
    kCFStringEncodingUTF16BE = 268435712
    kCFCharacterSetIllegal = 12
    kCFStringEncodingMacGeorgian = 23
    kCFNumberFormatterRoundFloor = 1
    kCFURLWindowsPathStyle = 2
    kCFNumberFormatterParseIntegersOnly = 1
    kCFStringEncodingISOLatinThai = 523
    kCFSocketAcceptCallBack = 2
    kCFXMLErrorEncodingConversionFailure = 3
    kCFXMLParserAddImpliedAttributes = 32
    kCFStringEncodingMacRomanLatin1 = 2564
    kCFStringEncodingISO_2022_JP_2 = 2081
    kCFStreamStatusClosed = 6
    kCFStringEncodingISO_2022_KR = 2112
    kCFXMLNodeTypeAttributeListDeclaration = 15
    kCFURLComponentHost = 8
    kCFNumberFormatterPadAfterPrefix = 1
    kCFStringEncodingMacDevanagari = 9
    kCFStringEncodingMacSymbol = 33
    kCFStringEncodingWindowsLatin2 = 1281
    kCFXMLNodeTypeNotation = 13
    kCFURLComponentPath = 3
    kCFStringEncodingMacSinhalese = 18
    kCFMessagePortReceiveTimeout = -2
    kCFURLUnknownPropertyKeyError = -16
    kCFPropertyListBinaryFormat_v1_0 = 200
    kCFCompareBackwards = 4
    kCFStringEncodingISOLatinArabic = 518
    kCFXMLEntityTypeParsedInternal = 1
    kCFStringEncodingGB_2312_80 = 1584
    kCFCharacterSetAlphaNumeric = 10
    kCFNumberDoubleType = 13
    kCFStringEncodingWindowsLatin1 = 1280
    kCFStringEncodingUTF16LE = 335544576
    kCFXMLErrorMalformedDTD = 5
    kCFStringEncodingMacMongolian = 27
    kCFXMLNodeTypeEntityReference = 10
    kCFUserNotificationNoteAlertLevel = 1
    kCFXMLErrorUnknownEncoding = 2
    kCFStringEncodingKOI8_U = 2568
    kCFStringEncodingDOSThai = 1053
    kCFStringEncodingMacBengali = 13
    kCFCompareCaseInsensitive = 1
    kCFStringEncodingMacHFS = 255
    kCFStringEncodingMacTamil = 14
    kCFNumberFormatterPadBeforePrefix = 0
    kCFXMLNodeTypeDocumentType = 11
    kCFStringEncodingJIS_X0208_90 = 1570
    kCFCalendarUnitHour = 32
    kCFStreamEventNone = 0
    kCFStringNormalizationFormD = 0
    kCFDateFormatterMediumStyle = 2
    kCFStringEncodingMacRoman = 0
    kCFXMLParserNoOptions = 0
    kCFXMLErrorMalformedProcessingInstruction = 4
    kCFXMLNodeTypeCDATASection = 7
    kCFCalendarUnitMinute = 64
    kCFStringEncodingASCII = 1536
    kCFStringEncodingDOSCanadianFrench = 1048
    kCFSocketAutomaticallyReenableDataCallBack = 3
    kCFCompareLessThan = -1
    kCFStringEncodingMacHebrew = 5
    kCFXMLNodeTypeElement = 2
    kCFCalendarUnitYear = 4
    kCFStringEncodingWindowsVietnamese = 1288
    kCFStringEncodingUTF32LE = 469762304
    kCFNumberFormatterRoundHalfDown = 5
    kCFStringEncodingISOLatin8 = 526
    kCFXMLErrorMalformedName = 6
    kCFStringEncodingEUC_CN = 2352
    kCFCharacterSetCapitalizedLetter = 13
    kCFNumberFloat32Type = 5
    kCFURLComponentQuery = 11
    kCFStringNormalizationFormKC = 3
    kCFUserNotificationUseRadioButtonsFlag = 64
    kCFURLHFSPathStyle = 1
    kCFStringEncodingDOSCyrillic = 1043
    kCFNumberSInt8Type = 1
    kCFStringEncodingMacTurkish = 35
    kCFURLTimeoutError = -18
    kCFCharacterSetControl = 1
    kCFStreamStatusAtEnd = 5
    kCFStringEncodingWindowsGreek = 1283
    kCFNumberShortType = 8
    kCFCompareLocalized = 32
    kCFStringEncodingISOLatinHebrew = 520
    kCFSocketConnectCallBack = 4
    kCFNumberFormatterRoundDown = 2
    kCFStreamEventOpenCompleted = 1
    kCFNumberMaxType = 14
    kCFStringEncodingISO_2022_JP_3 = 2083
    kCFNumberLongType = 10
    kCFURLComponentNetLocation = 2
    kCFURLPOSIXPathStyle = 0
    kCFStringEncodingKSC_5601_92_Johab = 1601
    kCFXMLParserReplacePhysicalEntities = 4
    kCFStringEncodingMacCentralEurRoman = 29
    kCFNumberFormatterDecimalStyle = 1
    kCFStringEncodingKSC_5601_87 = 1600
    kCFNumberFormatterSpellOutStyle = 5
    kCFStringEncodingWindowsCyrillic = 1282
    kCFStreamStatusNotOpen = 0
    kCFStringEncodingISOLatin3 = 515
    kCFStringEncodingJIS_C6226_78 = 1572
    kCFXMLErrorMalformedParsedCharacterData = 14
    CFNotificationSuspensionBehaviorDeliverImmediately = 4
    kCFRunLoopBeforeWaiting = 32
    kCFStringEncodingCNS_11643_92_P2 = 1618
    kCFURLComponentScheme = 1
    kCFUserNotificationPlainAlertLevel = 3
    kCFStringEncodingDOSBalticRim = 1030
    kCFStreamEventEndEncountered = 16
    kCFStringEncodingHZ_GB_2312 = 2565
    kCFUserNotificationOtherResponse = 2
    kCFDateFormatterShortStyle = 1
    kCFStringEncodingDOSNordic = 1050
    kCFRunLoopRunFinished = 1
    kCFStringEncodingMacGurmukhi = 10
    kCFStringEncodingDOSGreek = 1029
    kCFStringEncodingMacUkrainian = 152
    kCFGregorianUnitsSeconds = 32
    kCFSocketSuccess = 0
    kCFMessagePortIsInvalid = -3
    kCFXMLNodeTypeText = 6
    kCFURLUnknownSchemeError = -11
    kCFStringEncodingISOLatin10 = 528
    kCFStringEncodingMacArabic = 4
    kCFGregorianUnitsHours = 8
    CFNotificationSuspensionBehaviorHold = 3
    kCFStringEncodingMacCyrillic = 7
    kCFStringEncodingUTF32BE = 402653440
    kCFStringEncodingBig5 = 2563
    kCFNumberSInt16Type = 2
    kCFCalendarUnitSecond = 128
    kCFNumberFormatterRoundHalfEven = 4
    kCFUserNotificationStopAlertLevel = 0
    kCFSocketWriteCallBack = 8
    kCFRunLoopEntry = 1
    kCFDateFormatterNoStyle = 0
    kCFStringEncodingDOSPortuguese = 1045
    kCFRunLoopBeforeTimers = 2
    kCFStringEncodingMacIcelandic = 37
    kCFXMLErrorMalformedCDSect = 7
    kCFStringEncodingANSEL = 1537
    kCFStringEncodingWindowsHebrew = 1285
    kCFStringEncodingJIS_X0208_83 = 1569
    kCFStringEncodingUTF16 = 256
    kCFStringEncodingMacLaotian = 22
    kCFNumberFormatterRoundCeiling = 0
    kCFStringEncodingISOLatin6 = 522
    kCFNumberFormatterRoundUp = 3
    kCFCharacterSetWhitespace = 2
    kCFXMLNodeTypeDocument = 1
    kCFStreamStatusWriting = 4
    kCFRunLoopAllActivities = 268435455
    kCFStringEncodingUnicode = 256
    kCFXMLEntityTypeCharacter = 4
    kCFXMLParserSkipWhitespace = 8
    kCFStringEncodingMacExtArabic = 31
    kCFStringEncodingEUC_KR = 2368
    kCFStreamEventErrorOccurred = 8
    kCFStringEncodingEBCDIC_CP037 = 3074
    kCFUserNotificationCautionAlertLevel = 2
    kCFUserNotificationCancelResponse = 3
    kCFStringEncodingDOSChineseTrad = 1059
    kCFStringEncodingMacGaelic = 40
    kCFStringEncodingMacMalayalam = 17
    kCFStringNormalizationFormKD = 1
    kCFURLImproperArgumentsError = -15
    kCFPropertyListXMLFormat_v1_0 = 100
    kCFNumberFormatterCurrencyStyle = 2
    kCFStringEncodingShiftJIS_X0213_MenKuTen = 1577
    kCFNumberFloatType = 12
    kCFXMLErrorMalformedComment = 12
    kCFStringEncodingMacChineseTrad = 2
    kCFStreamErrorDomainMacOSStatus = 2
    kCFStringEncodingISO_2022_JP = 2080
    kCFUserNotificationDefaultResponse = 0
    kCFXMLErrorMalformedCharacterReference = 13
    kCFStringEncodingVISCII = 2567
    kCFCharacterSetUppercaseLetter = 7
    kCFNumberSInt32Type = 3
    kCFStringEncodingMacOriya = 12
    kCFRunLoopRunHandledSource = 4
    kCFUserNotificationAlternateResponse = 1
    kCFXMLNodeTypeComment = 5
    kCFXMLStatusParseInProgress = -1
    kCFStringEncodingKOI8_R = 2562
    kCFCompareGreaterThan = 1
    kCFStringEncodingWindowsBalticRim = 1287
    kCFStringEncodingDOSHebrew = 1047
    kCFURLComponentFragment = 12
    kCFNotificationPostToAllSessions = 2
    kCFStringEncodingMacKorean = 3
    kCFXMLEntityTypeParameter = 0
    kCFStringEncodingMacVT100 = 252
    kCFSocketError = -1
    kCFStringEncodingMacCeltic = 39
    kCFStreamEventCanAcceptBytes = 4
    CFNotificationSuspensionBehaviorCoalesce = 2
    kCFStringEncodingUTF32 = 201326848
    kCFStringEncodingMacArmenian = 24
    kCFCalendarUnitWeek = 256
    kCFStringEncodingISOLatin7 = 525
    kCFStringEncodingDOSChineseSimplif = 1057
    kCFXMLParserResolveExternalEntities = 16
    kCFXMLParserAllOptions = 16777215
    kCFXMLParserValidateDocument = 1
    kCFMessagePortTransportError = -4
    kCFStringEncodingEUC_JP = 2336
    kCFCharacterSetSymbol = 14
    kCFURLComponentParameterString = 10
    kCFURLUnknownError = -10
    kCFNumberFormatterPadAfterSuffix = 3
    kCFStringEncodingDOSLatin2 = 1042
    kCFSocketNoCallBack = 0
    kCFXMLParserSkipMetaData = 2
    kCFNotificationDeliverImmediately = 1
    kCFCalendarComponentsWrap = 1
    kCFXMLStatusParseNotBegun = -2
    kCFStreamStatusOpening = 1
    kCFCalendarUnitWeekday = 512
    CFNotificationSuspensionBehaviorDrop = 1
    kCFSocketTimeout = -2
    kCFStreamStatusReading = 3
    kCFNumberIntType = 9
    kCFURLComponentUser = 5
    kCFURLPropertyKeyUnavailableError = -17
    kCFCompareNonliteral = 16
    kCFStringEncodingISOLatinGreek = 519
    kCFSocketCloseOnInvalidate = 128
    kCFXMLEntityTypeUnparsed = 3
    kCFStringEncodingGBK_95 = 1585
    kCFCharacterSetDecimalDigit = 4
    kCFNumberCFIndexType = 14
    kCFStringEncodingISO_2022_JP_1 = 2082
    kCFNumberLongLongType = 11
    kCFUserNotificationNoDefaultButtonFlag = 32
    kCFGregorianUnitsMonths = 2
    kCFPropertyListImmutable = 0
    kCFStringEncodingMacEthiopic = 28
    kCFGregorianUnitsDays = 4
    kCFStringEncodingBig5_E = 2569
    kCFCharacterSetNonBase = 8
    kCFNumberSInt64Type = 4
    kCFCalendarUnitMonth = 8
    kCFStringEncodingUTF8 = 134217984
    kCFStringEncodingDOSJapanese = 1056
    kCFURLResourceNotFoundError = -12
    kCFStringEncodingISOLatin2 = 514
    kCFStreamErrorDomainCustom = -1
    kCFXMLNodeTypeWhitespace = 12
    kCFStringEncodingMacDingbats = 34
    kCFRunLoopRunTimedOut = 3
    kCFNumberFormatterScientificStyle = 4
    kCFStringEncodingJIS_X0212_90 = 1571
    kCFPropertyListOpenStepFormat = 1
    kCFDateFormatterFullStyle = 4
    kCFSocketAutomaticallyReenableAcceptCallBack = 2
    kCFStringEncodingCNS_11643_92_P1 = 1617
    kCFStringEncodingDOSLatin1 = 1040
    kCFStringNormalizationFormC = 2
    kCFNumberCharType = 7
    kCFMessagePortSendTimeout = -1
    kCFXMLErrorNoData = 15
    kCFXMLNodeTypeEntity = 9
    kCFStringEncodingDOSArabic = 1049
    kCFCharacterSetWhitespaceAndNewline = 3
    kCFStringEncodingDOSTurkish = 1044
    kCFPropertyListMutableContainersAndLeaves = 2
    kCFURLComponentUserInfo = 7
    kCFStringEncodingMacFarsi = 140
    kCFMessagePortSuccess = 0
    kCFGregorianAllUnits = 16777215
    kCFXMLNodeTypeProcessingInstruction = 4
    kCFStringEncodingWindowsKoreanJohab = 1296
    CFByteOrderBigEndian = 2
    kCFStringEncodingMacTibetan = 26
    kCFURLResourceAccessViolationError = -13
    kCFXMLErrorMalformedDocument = 10
    kCFStringEncodingISOLatin9 = 527
    kCFURLComponentPassword = 6
    kCFStringEncodingDOSGreek1 = 1041
    kCFGregorianUnitsMinutes = 16
    kCFCalendarUnitEra = 2
    kCFStringEncodingEUC_TW = 2353
    class __CFAllocator(Structure):
        pass
    __CFAllocator._fields_ = [
    ]
    CFArrayRetainCallBack = CFUNCTYPE(c_void_p, POINTER(__CFAllocator), c_void_p)
    CFArrayReleaseCallBack = CFUNCTYPE(None, POINTER(__CFAllocator), c_void_p)
    class __CFString(Structure):
        pass
    __CFString._fields_ = [
    ]
    CFStringRef = POINTER(__CFString)
    CFArrayCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    Boolean = c_ubyte
    CFArrayEqualCallBack = CFUNCTYPE(Boolean, c_void_p, c_void_p)
    class CFArrayCallBacks(Structure):
        pass
    SInt32 = c_long
    CFIndex = SInt32
    CFArrayCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFArrayRetainCallBack),
        ('release', CFArrayReleaseCallBack),
        ('copyDescription', CFArrayCopyDescriptionCallBack),
        ('equal', CFArrayEqualCallBack),
    ]
    CFArrayApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p)
    class __CFArray(Structure):
        pass
    __CFArray._fields_ = [
    ]
    CFArrayRef = POINTER(__CFArray)
    CFMutableArrayRef = POINTER(__CFArray)
    class __CFAttributedString(Structure):
        pass
    __CFAttributedString._fields_ = [
    ]
    CFAttributedStringRef = POINTER(__CFAttributedString)
    CFMutableAttributedStringRef = POINTER(__CFAttributedString)
    CFBagRetainCallBack = CFUNCTYPE(c_void_p, POINTER(__CFAllocator), c_void_p)
    CFBagReleaseCallBack = CFUNCTYPE(None, POINTER(__CFAllocator), c_void_p)
    CFBagCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    CFBagEqualCallBack = CFUNCTYPE(Boolean, c_void_p, c_void_p)
    UInt32 = c_ulong
    CFHashCode = UInt32
    CFBagHashCallBack = CFUNCTYPE(CFHashCode, c_void_p)
    class CFBagCallBacks(Structure):
        pass
    CFBagCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFBagRetainCallBack),
        ('release', CFBagReleaseCallBack),
        ('copyDescription', CFBagCopyDescriptionCallBack),
        ('equal', CFBagEqualCallBack),
        ('hash', CFBagHashCallBack),
    ]
    CFBagApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p)
    class __CFBag(Structure):
        pass
    __CFBag._fields_ = [
    ]
    CFBagRef = POINTER(__CFBag)
    CFMutableBagRef = POINTER(__CFBag)
    CFTypeID = UInt32
    CFOptionFlags = UInt32
    CFTypeRef = c_void_p
    CFMutableStringRef = POINTER(__CFString)
    CFPropertyListRef = CFTypeRef

    # values for enumeration 'CFComparisonResult'
    CFComparisonResult = c_int # enum
    CFComparatorFunction = CFUNCTYPE(CFComparisonResult, c_void_p, c_void_p, c_void_p)
    class CFRange(Structure):
        pass
    CFRange._fields_ = [
        ('location', CFIndex),
        ('length', CFIndex),
    ]
    class __CFNull(Structure):
        pass
    __CFNull._fields_ = [
    ]
    CFNullRef = POINTER(__CFNull)
    CFAllocatorRef = POINTER(__CFAllocator)
    CFAllocatorRetainCallBack = CFUNCTYPE(c_void_p, c_void_p)
    CFAllocatorReleaseCallBack = CFUNCTYPE(None, c_void_p)
    CFAllocatorCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    CFAllocatorAllocateCallBack = CFUNCTYPE(c_void_p, c_long, c_ulong, c_void_p)
    CFAllocatorReallocateCallBack = CFUNCTYPE(c_void_p, c_void_p, c_long, c_ulong, c_void_p)
    CFAllocatorDeallocateCallBack = CFUNCTYPE(None, c_void_p, c_void_p)
    CFAllocatorPreferredSizeCallBack = CFUNCTYPE(CFIndex, c_long, c_ulong, c_void_p)
    class CFAllocatorContext(Structure):
        pass
    CFAllocatorContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFAllocatorRetainCallBack),
        ('release', CFAllocatorReleaseCallBack),
        ('copyDescription', CFAllocatorCopyDescriptionCallBack),
        ('allocate', CFAllocatorAllocateCallBack),
        ('reallocate', CFAllocatorReallocateCallBack),
        ('deallocate', CFAllocatorDeallocateCallBack),
        ('preferredSize', CFAllocatorPreferredSizeCallBack),
    ]
    class CFBinaryHeapCompareContext(Structure):
        pass
    CFBinaryHeapCompareContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    class CFBinaryHeapCallBacks(Structure):
        pass
    CFBinaryHeapCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFUNCTYPE(c_void_p, POINTER(__CFAllocator), c_void_p)),
        ('release', CFUNCTYPE(None, POINTER(__CFAllocator), c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
        ('compare', CFUNCTYPE(CFComparisonResult, c_void_p, c_void_p, c_void_p)),
    ]
    CFBinaryHeapApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p)
    class __CFBinaryHeap(Structure):
        pass
    CFBinaryHeapRef = POINTER(__CFBinaryHeap)
    CFBit = UInt32
    class __CFBitVector(Structure):
        pass
    __CFBitVector._fields_ = [
    ]
    CFBitVectorRef = POINTER(__CFBitVector)
    CFMutableBitVectorRef = POINTER(__CFBitVector)
    class __CFBundle(Structure):
        pass
    CFBundleRef = POINTER(__CFBundle)
    CFPlugInRef = POINTER(__CFBundle)

    # values for enumeration '__CFByteOrder'
    __CFByteOrder = c_int # enum
    CFByteOrder = __CFByteOrder
    class CFSwappedFloat32(Structure):
        pass
    u_int32_t = c_uint
    uint32_t = u_int32_t
    CFSwappedFloat32._fields_ = [
        ('v', uint32_t),
    ]
    class CFSwappedFloat64(Structure):
        pass
    u_int64_t = c_ulonglong
    uint64_t = u_int64_t
    CFSwappedFloat64._fields_ = [
        ('v', uint64_t),
    ]
    class __CFCalendar(Structure):
        pass
    CFCalendarRef = POINTER(__CFCalendar)

    # values for enumeration 'CFCalendarUnit'
    CFCalendarUnit = c_int # enum
    class __CFCharacterSet(Structure):
        pass
    __CFCharacterSet._fields_ = [
    ]
    CFCharacterSetRef = POINTER(__CFCharacterSet)
    CFMutableCharacterSetRef = POINTER(__CFCharacterSet)

    # values for enumeration 'CFCharacterSetPredefinedSet'
    CFCharacterSetPredefinedSet = c_int # enum
    class __CFData(Structure):
        pass
    __CFData._fields_ = [
    ]
    CFDataRef = POINTER(__CFData)
    CFMutableDataRef = POINTER(__CFData)
    CFTimeInterval = c_double
    CFAbsoluteTime = CFTimeInterval
    class __CFDate(Structure):
        pass
    __CFDate._fields_ = [
    ]
    CFDateRef = POINTER(__CFDate)
    class __CFTimeZone(Structure):
        pass
    __CFTimeZone._fields_ = [
    ]
    CFTimeZoneRef = POINTER(__CFTimeZone)
    class CFGregorianDate(Structure):
        pass
    SInt8 = c_byte
    CFGregorianDate._pack_ = 4
    CFGregorianDate._fields_ = [
        ('year', SInt32),
        ('month', SInt8),
        ('day', SInt8),
        ('hour', SInt8),
        ('minute', SInt8),
        ('second', c_double),
    ]
    class CFGregorianUnits(Structure):
        pass
    CFGregorianUnits._pack_ = 4
    CFGregorianUnits._fields_ = [
        ('years', SInt32),
        ('months', SInt32),
        ('days', SInt32),
        ('hours', SInt32),
        ('minutes', SInt32),
        ('seconds', c_double),
    ]

    # values for enumeration 'CFGregorianUnitFlags'
    CFGregorianUnitFlags = c_int # enum
    class __CFDateFormatter(Structure):
        pass
    CFDateFormatterRef = POINTER(__CFDateFormatter)

    # values for enumeration 'CFDateFormatterStyle'
    CFDateFormatterStyle = c_int # enum
    CFDictionaryRetainCallBack = CFUNCTYPE(c_void_p, POINTER(__CFAllocator), c_void_p)
    CFDictionaryReleaseCallBack = CFUNCTYPE(None, POINTER(__CFAllocator), c_void_p)
    CFDictionaryCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    CFDictionaryEqualCallBack = CFUNCTYPE(Boolean, c_void_p, c_void_p)
    CFDictionaryHashCallBack = CFUNCTYPE(CFHashCode, c_void_p)
    class CFDictionaryKeyCallBacks(Structure):
        pass
    CFDictionaryKeyCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFDictionaryRetainCallBack),
        ('release', CFDictionaryReleaseCallBack),
        ('copyDescription', CFDictionaryCopyDescriptionCallBack),
        ('equal', CFDictionaryEqualCallBack),
        ('hash', CFDictionaryHashCallBack),
    ]
    class CFDictionaryValueCallBacks(Structure):
        pass
    CFDictionaryValueCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFDictionaryRetainCallBack),
        ('release', CFDictionaryReleaseCallBack),
        ('copyDescription', CFDictionaryCopyDescriptionCallBack),
        ('equal', CFDictionaryEqualCallBack),
    ]
    CFDictionaryApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)
    class __CFDictionary(Structure):
        pass
    __CFDictionary._fields_ = [
    ]
    CFDictionaryRef = POINTER(__CFDictionary)
    CFMutableDictionaryRef = POINTER(__CFDictionary)
    class __CFLocale(Structure):
        pass
    __CFLocale._fields_ = [
    ]
    CFLocaleRef = POINTER(__CFLocale)
    class __CFMachPort(Structure):
        pass
    CFMachPortRef = POINTER(__CFMachPort)
    class CFMachPortContext(Structure):
        pass
    CFMachPortContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    CFMachPortCallBack = CFUNCTYPE(None, POINTER(__CFMachPort), c_void_p, c_long, c_void_p)
    CFMachPortInvalidationCallBack = CFUNCTYPE(None, POINTER(__CFMachPort), c_void_p)
    class __CFMessagePort(Structure):
        pass
    CFMessagePortRef = POINTER(__CFMessagePort)
    class CFMessagePortContext(Structure):
        pass
    CFMessagePortContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    CFMessagePortCallBack = CFUNCTYPE(CFDataRef, POINTER(__CFMessagePort), c_long, POINTER(__CFData), c_void_p)
    CFMessagePortInvalidationCallBack = CFUNCTYPE(None, POINTER(__CFMessagePort), c_void_p)
    class __CFNotificationCenter(Structure):
        pass
    CFNotificationCenterRef = POINTER(__CFNotificationCenter)
    CFNotificationCallback = CFUNCTYPE(None, POINTER(__CFNotificationCenter), c_void_p, POINTER(__CFString), c_void_p, POINTER(__CFDictionary))

    # values for enumeration 'CFNotificationSuspensionBehavior'
    CFNotificationSuspensionBehavior = c_int # enum
    class __CFBoolean(Structure):
        pass
    __CFBoolean._fields_ = [
    ]
    CFBooleanRef = POINTER(__CFBoolean)

    # values for enumeration 'CFNumberType'
    CFNumberType = c_int # enum
    class __CFNumber(Structure):
        pass
    __CFNumber._fields_ = [
    ]
    CFNumberRef = POINTER(__CFNumber)
    class __CFNumberFormatter(Structure):
        pass
    CFNumberFormatterRef = POINTER(__CFNumberFormatter)

    # values for enumeration 'CFNumberFormatterStyle'
    CFNumberFormatterStyle = c_int # enum

    # values for enumeration 'CFNumberFormatterOptionFlags'
    CFNumberFormatterOptionFlags = c_int # enum

    # values for enumeration 'CFNumberFormatterRoundingMode'
    CFNumberFormatterRoundingMode = c_int # enum

    # values for enumeration 'CFNumberFormatterPadPosition'
    CFNumberFormatterPadPosition = c_int # enum
    CFPlugInDynamicRegisterFunction = CFUNCTYPE(None, POINTER(__CFBundle))
    CFPlugInUnloadFunction = CFUNCTYPE(None, POINTER(__CFBundle))
    class __CFUUID(Structure):
        pass
    __CFUUID._fields_ = [
    ]
    CFPlugInFactoryFunction = CFUNCTYPE(c_void_p, POINTER(__CFAllocator), POINTER(__CFUUID))
    class __CFPlugInInstance(Structure):
        pass
    CFPlugInInstanceRef = POINTER(__CFPlugInInstance)
    CFPlugInInstanceGetInterfaceFunction = CFUNCTYPE(Boolean, POINTER(__CFPlugInInstance), POINTER(__CFString), POINTER(c_void_p))
    CFPlugInInstanceDeallocateInstanceDataFunction = CFUNCTYPE(None, c_void_p)

    # values for enumeration 'CFPropertyListMutabilityOptions'
    CFPropertyListMutabilityOptions = c_int # enum

    # values for enumeration 'CFPropertyListFormat'
    CFPropertyListFormat = c_int # enum
    class __CFRunLoop(Structure):
        pass
    CFRunLoopRef = POINTER(__CFRunLoop)
    class __CFRunLoopSource(Structure):
        pass
    CFRunLoopSourceRef = POINTER(__CFRunLoopSource)
    class __CFRunLoopObserver(Structure):
        pass
    CFRunLoopObserverRef = POINTER(__CFRunLoopObserver)
    class __CFRunLoopTimer(Structure):
        pass
    CFRunLoopTimerRef = POINTER(__CFRunLoopTimer)

    # values for enumeration 'CFRunLoopActivity'
    CFRunLoopActivity = c_int # enum
    class CFRunLoopSourceContext(Structure):
        pass
    CFRunLoopSourceContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
        ('equal', CFUNCTYPE(Boolean, c_void_p, c_void_p)),
        ('hash', CFUNCTYPE(CFHashCode, c_void_p)),
        ('schedule', CFUNCTYPE(None, c_void_p, POINTER(__CFRunLoop), POINTER(__CFString))),
        ('cancel', CFUNCTYPE(None, c_void_p, POINTER(__CFRunLoop), POINTER(__CFString))),
        ('perform', CFUNCTYPE(None, c_void_p)),
    ]
    class CFRunLoopSourceContext1(Structure):
        pass
    __darwin_natural_t = c_uint
    natural_t = __darwin_natural_t
    mach_port_name_t = natural_t
    mach_port_t = mach_port_name_t
    CFRunLoopSourceContext1._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
        ('equal', CFUNCTYPE(Boolean, c_void_p, c_void_p)),
        ('hash', CFUNCTYPE(CFHashCode, c_void_p)),
        ('getPort', CFUNCTYPE(mach_port_t, c_void_p)),
        ('perform', CFUNCTYPE(c_void_p, c_void_p, c_long, POINTER(__CFAllocator), c_void_p)),
    ]
    class CFRunLoopObserverContext(Structure):
        pass
    CFRunLoopObserverContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    CFRunLoopObserverCallBack = CFUNCTYPE(None, POINTER(__CFRunLoopObserver), CFRunLoopActivity, c_void_p)
    class CFRunLoopTimerContext(Structure):
        pass
    CFRunLoopTimerContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    CFRunLoopTimerCallBack = CFUNCTYPE(None, POINTER(__CFRunLoopTimer), c_void_p)
    CFSetRetainCallBack = CFUNCTYPE(c_void_p, POINTER(__CFAllocator), c_void_p)
    CFSetReleaseCallBack = CFUNCTYPE(None, POINTER(__CFAllocator), c_void_p)
    CFSetCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    CFSetEqualCallBack = CFUNCTYPE(Boolean, c_void_p, c_void_p)
    CFSetHashCallBack = CFUNCTYPE(CFHashCode, c_void_p)
    class CFSetCallBacks(Structure):
        pass
    CFSetCallBacks._fields_ = [
        ('version', CFIndex),
        ('retain', CFSetRetainCallBack),
        ('release', CFSetReleaseCallBack),
        ('copyDescription', CFSetCopyDescriptionCallBack),
        ('equal', CFSetEqualCallBack),
        ('hash', CFSetHashCallBack),
    ]
    CFSetApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p)
    class __CFSet(Structure):
        pass
    __CFSet._fields_ = [
    ]
    CFSetRef = POINTER(__CFSet)
    CFMutableSetRef = POINTER(__CFSet)
    CFSocketNativeHandle = c_int
    class __CFSocket(Structure):
        pass
    CFSocketRef = POINTER(__CFSocket)

    # values for enumeration 'CFSocketError'
    CFSocketError = c_int # enum
    class CFSocketSignature(Structure):
        pass
    CFSocketSignature._fields_ = [
        ('protocolFamily', SInt32),
        ('socketType', SInt32),
        ('protocol', SInt32),
        ('address', CFDataRef),
    ]

    # values for enumeration 'CFSocketCallBackType'
    CFSocketCallBackType = c_int # enum
    CFSocketCallBack = CFUNCTYPE(None, POINTER(__CFSocket), CFSocketCallBackType, POINTER(__CFData), c_void_p, c_void_p)
    class CFSocketContext(Structure):
        pass
    CFSocketContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]

    # values for enumeration 'CFStreamStatus'
    CFStreamStatus = c_int # enum

    # values for enumeration 'CFStreamErrorDomain'
    CFStreamErrorDomain = c_int # enum
    class CFStreamError(Structure):
        pass
    CFStreamError._fields_ = [
        ('domain', CFStreamErrorDomain),
        ('error', SInt32),
    ]

    # values for enumeration 'CFStreamEventType'
    CFStreamEventType = c_int # enum
    class CFStreamClientContext(Structure):
        pass
    CFStreamClientContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFUNCTYPE(c_void_p, c_void_p)),
        ('release', CFUNCTYPE(None, c_void_p)),
        ('copyDescription', CFUNCTYPE(CFStringRef, c_void_p)),
    ]
    class __CFReadStream(Structure):
        pass
    CFReadStreamRef = POINTER(__CFReadStream)
    class __CFWriteStream(Structure):
        pass
    CFWriteStreamRef = POINTER(__CFWriteStream)
    CFReadStreamClientCallBack = CFUNCTYPE(None, POINTER(__CFReadStream), CFStreamEventType, c_void_p)
    CFWriteStreamClientCallBack = CFUNCTYPE(None, POINTER(__CFWriteStream), CFStreamEventType, c_void_p)
    CFStringEncoding = UInt32

    # values for enumeration 'CFStringBuiltInEncodings'
    CFStringBuiltInEncodings = c_int # enum

    # values for enumeration 'CFStringCompareFlags'
    CFStringCompareFlags = c_int # enum

    # values for enumeration 'CFStringNormalizationForm'
    CFStringNormalizationForm = c_int # enum
    class CFStringInlineBuffer(Structure):
        pass
    UInt16 = c_ushort
    UniChar = UInt16
    CFStringInlineBuffer._fields_ = [
        ('buffer', UniChar * 64),
        ('theString', CFStringRef),
        ('directBuffer', POINTER(UniChar)),
        ('rangeToBuffer', CFRange),
        ('bufferedRangeStart', CFIndex),
        ('bufferedRangeEnd', CFIndex),
    ]

    # values for enumeration 'CFStringEncodings'
    CFStringEncodings = c_int # enum
    CFTreeRetainCallBack = CFUNCTYPE(c_void_p, c_void_p)
    CFTreeReleaseCallBack = CFUNCTYPE(None, c_void_p)
    CFTreeCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    class CFTreeContext(Structure):
        pass
    CFTreeContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFTreeRetainCallBack),
        ('release', CFTreeReleaseCallBack),
        ('copyDescription', CFTreeCopyDescriptionCallBack),
    ]
    CFTreeApplierFunction = CFUNCTYPE(None, c_void_p, c_void_p)
    class __CFTree(Structure):
        pass
    CFTreeRef = POINTER(__CFTree)

    # values for enumeration 'CFURLPathStyle'
    CFURLPathStyle = c_int # enum
    class __CFURL(Structure):
        pass
    __CFURL._fields_ = [
    ]
    CFURLRef = POINTER(__CFURL)

    # values for enumeration 'CFURLComponentType'
    CFURLComponentType = c_int # enum

    # values for enumeration 'CFURLError'
    CFURLError = c_int # enum
    CFUUIDRef = POINTER(__CFUUID)
    class CFUUIDBytes(Structure):
        pass
    UInt8 = c_ubyte
    CFUUIDBytes._fields_ = [
        ('byte0', UInt8),
        ('byte1', UInt8),
        ('byte2', UInt8),
        ('byte3', UInt8),
        ('byte4', UInt8),
        ('byte5', UInt8),
        ('byte6', UInt8),
        ('byte7', UInt8),
        ('byte8', UInt8),
        ('byte9', UInt8),
        ('byte10', UInt8),
        ('byte11', UInt8),
        ('byte12', UInt8),
        ('byte13', UInt8),
        ('byte14', UInt8),
        ('byte15', UInt8),
    ]
    class __CFUserNotification(Structure):
        pass
    CFUserNotificationRef = POINTER(__CFUserNotification)
    CFUserNotificationCallBack = CFUNCTYPE(None, POINTER(__CFUserNotification), c_ulong)
    class __CFXMLNode(Structure):
        pass
    __CFXMLNode._fields_ = [
    ]
    CFXMLNodeRef = POINTER(__CFXMLNode)
    CFXMLTreeRef = CFTreeRef

    # values for enumeration 'CFXMLNodeTypeCode'
    CFXMLNodeTypeCode = c_int # enum
    class CFXMLElementInfo(Structure):
        pass
    CFXMLElementInfo._fields_ = [
        ('attributes', CFDictionaryRef),
        ('attributeOrder', CFArrayRef),
        ('isEmpty', Boolean),
        ('_reserved', c_char * 3),
    ]
    class CFXMLProcessingInstructionInfo(Structure):
        pass
    CFXMLProcessingInstructionInfo._fields_ = [
        ('dataString', CFStringRef),
    ]
    class CFXMLDocumentInfo(Structure):
        pass
    CFXMLDocumentInfo._fields_ = [
        ('sourceURL', CFURLRef),
        ('encoding', CFStringEncoding),
    ]
    class CFXMLExternalID(Structure):
        pass
    CFXMLExternalID._fields_ = [
        ('systemID', CFURLRef),
        ('publicID', CFStringRef),
    ]
    class CFXMLDocumentTypeInfo(Structure):
        pass
    CFXMLDocumentTypeInfo._fields_ = [
        ('externalID', CFXMLExternalID),
    ]
    class CFXMLNotationInfo(Structure):
        pass
    CFXMLNotationInfo._fields_ = [
        ('externalID', CFXMLExternalID),
    ]
    class CFXMLElementTypeDeclarationInfo(Structure):
        pass
    CFXMLElementTypeDeclarationInfo._fields_ = [
        ('contentDescription', CFStringRef),
    ]
    class CFXMLAttributeDeclarationInfo(Structure):
        pass
    CFXMLAttributeDeclarationInfo._fields_ = [
        ('attributeName', CFStringRef),
        ('typeString', CFStringRef),
        ('defaultString', CFStringRef),
    ]
    class CFXMLAttributeListDeclarationInfo(Structure):
        pass
    CFXMLAttributeListDeclarationInfo._fields_ = [
        ('numberOfAttributes', CFIndex),
        ('attributes', POINTER(CFXMLAttributeDeclarationInfo)),
    ]

    # values for enumeration 'CFXMLEntityTypeCode'
    CFXMLEntityTypeCode = c_int # enum
    class CFXMLEntityInfo(Structure):
        pass
    CFXMLEntityInfo._fields_ = [
        ('entityType', CFXMLEntityTypeCode),
        ('replacementText', CFStringRef),
        ('entityID', CFXMLExternalID),
        ('notationName', CFStringRef),
    ]
    class CFXMLEntityReferenceInfo(Structure):
        pass
    CFXMLEntityReferenceInfo._fields_ = [
        ('entityType', CFXMLEntityTypeCode),
    ]
    class __CFXMLParser(Structure):
        pass
    CFXMLParserRef = POINTER(__CFXMLParser)

    # values for enumeration 'CFXMLParserOptions'
    CFXMLParserOptions = c_int # enum

    # values for enumeration 'CFXMLParserStatusCode'
    CFXMLParserStatusCode = c_int # enum
    CFXMLParserCreateXMLStructureCallBack = CFUNCTYPE(c_void_p, POINTER(__CFXMLParser), POINTER(__CFXMLNode), c_void_p)
    CFXMLParserAddChildCallBack = CFUNCTYPE(None, POINTER(__CFXMLParser), c_void_p, c_void_p, c_void_p)
    CFXMLParserEndXMLStructureCallBack = CFUNCTYPE(None, POINTER(__CFXMLParser), c_void_p, c_void_p)
    CFXMLParserResolveExternalEntityCallBack = CFUNCTYPE(CFDataRef, POINTER(__CFXMLParser), POINTER(CFXMLExternalID), c_void_p)
    CFXMLParserHandleErrorCallBack = CFUNCTYPE(Boolean, POINTER(__CFXMLParser), CFXMLParserStatusCode, c_void_p)
    class CFXMLParserCallBacks(Structure):
        pass
    CFXMLParserCallBacks._fields_ = [
        ('version', CFIndex),
        ('createXMLStructure', CFXMLParserCreateXMLStructureCallBack),
        ('addChild', CFXMLParserAddChildCallBack),
        ('endXMLStructure', CFXMLParserEndXMLStructureCallBack),
        ('resolveExternalEntity', CFXMLParserResolveExternalEntityCallBack),
        ('handleError', CFXMLParserHandleErrorCallBack),
    ]
    CFXMLParserRetainCallBack = CFUNCTYPE(c_void_p, c_void_p)
    CFXMLParserReleaseCallBack = CFUNCTYPE(None, c_void_p)
    CFXMLParserCopyDescriptionCallBack = CFUNCTYPE(CFStringRef, c_void_p)
    class CFXMLParserContext(Structure):
        pass
    CFXMLParserContext._fields_ = [
        ('version', CFIndex),
        ('info', c_void_p),
        ('retain', CFXMLParserRetainCallBack),
        ('release', CFXMLParserReleaseCallBack),
        ('copyDescription', CFXMLParserCopyDescriptionCallBack),
    ]
    __CFBinaryHeap._fields_ = [
    ]
    __CFBundle._fields_ = [
    ]
    __CFCalendar._fields_ = [
    ]
    __CFDateFormatter._fields_ = [
    ]
    __CFMachPort._fields_ = [
    ]
    __CFMessagePort._fields_ = [
    ]
    __CFNotificationCenter._fields_ = [
    ]
    __CFNumberFormatter._fields_ = [
    ]
    __CFPlugInInstance._fields_ = [
    ]
    __CFRunLoop._fields_ = [
    ]
    __CFRunLoopSource._fields_ = [
    ]
    __CFRunLoopObserver._fields_ = [
    ]
    __CFRunLoopTimer._fields_ = [
    ]
    __CFSocket._fields_ = [
    ]
    __CFReadStream._fields_ = [
    ]
    __CFWriteStream._fields_ = [
    ]
    __CFTree._fields_ = [
    ]
    __CFUserNotification._fields_ = [
    ]
    __CFXMLParser._fields_ = [
    ]
    __all__ = ['CFCharacterSetPredefinedSet', '__CFBundle',
               'kCFGregorianUnitsMonths', 'kCFCompareAnchored',
               'CFComparatorFunction', 'CFMutableDictionaryRef',
               'kCFCompareBackwards', 'kCFURLHFSPathStyle',
               'kCFStringEncodingMacHebrew', 'CFArrayRef',
               'kCFNumberFormatterPadAfterPrefix',
               'kCFXMLNodeTypeCDATASection', '__CFMachPort',
               'kCFNumberFormatterRoundFloor', 'kCFNumberShortType',
               'kCFURLComponentPassword', 'kCFDateFormatterMediumStyle',
               'kCFStringEncodingUTF32BE', 'kCFStringEncodingGB_2312_80',
               'CFNumberFormatterRoundingMode', 'CFTreeRef',
               'kCFStringEncodingDOSKorean',
               'kCFXMLErrorMalformedComment',
               'kCFStringEncodingMacExtArabic', 'kCFNotFound',
               'kCFRunLoopBeforeWaiting', 'CFRunLoopObserverContext',
               'kCFPropertyListImmutable', 'CFMessagePortContext',
               'kCFStringEncodingMacIcelandic', '__CFRunLoopTimer',
               'kCFStringEncodingEBCDIC_CP037',
               'kCFStringEncodingShiftJIS',
               'kCFStringEncodingMacRomanian', 'CFUUIDRef',
               '__CFBinaryHeap', 'kCFCalendarUnitYear',
               'CFMutableDataRef', 'kCFStringEncodingDOSIcelandic',
               'kCFCharacterSetPunctuation', 'kCFURLUnknownSchemeError',
               'kCFCompareLocalized', 'CFNullRef', 'CFBinaryHeapRef',
               '__CFNumber', 'CFPlugInInstanceRef', 'CFCalendarRef',
               'kCFXMLParserSkipMetaData', 'CFStreamEventType',
               'kCFURLResourceNotFoundError', 'kCFGregorianUnitsSeconds',
               'kCFNumberFormatterPadBeforeSuffix',
               'kCFSocketDataCallBack', 'CFTreeApplierFunction',
               'kCFStringEncodingMacGeorgian', 'CFArrayApplierFunction',
               'CFXMLParserStatusCode', 'CFIndex',
               'kCFStringEncodingJIS_X0208_90',
               'CFTreeCopyDescriptionCallBack',
               'kCFStringEncodingKSC_5601_92_Johab',
               'kCFUserNotificationUseRadioButtonsFlag',
               '__CFPlugInInstance', 'CFPropertyListRef',
               'kCFURLPOSIXPathStyle', 'CFXMLElementInfo',
               'kCFXMLErrorMalformedDTD', 'CFUserNotificationCallBack',
               'kCFXMLNodeTypeComment', 'CFBit',
               'kCFXMLEntityTypeParsedExternal',
               'kCFStringEncodingMacBurmese', 'kCFXMLErrorNoData',
               'kCFCharacterSetLetter', 'kCFCompareGreaterThan',
               '__CFNull', 'kCFStringEncodingANSEL', 'CFMutableSetRef',
               '__CFString', 'kCFStringEncodingMacBengali',
               'CFBagHashCallBack',
               'kCFXMLErrorMalformedCharacterReference',
               'kCFXMLErrorMalformedCloseTag',
               'CFNotificationSuspensionBehavior',
               'CFMutableCharacterSetRef', 'kCFSocketSuccess',
               'kCFXMLErrorMalformedName', '__CFByteOrder',
               'kCFSocketAutomaticallyReenableDataCallBack',
               'CFNumberFormatterStyle', 'CFXMLExternalID',
               'kCFXMLParserResolveExternalEntities',
               'kCFStringEncodingMacGaelic', 'kCFDateFormatterLongStyle',
               '__darwin_natural_t', 'CFWriteStreamClientCallBack',
               'kCFRunLoopRunFinished', 'CFPlugInFactoryFunction',
               'CFRunLoopSourceRef', 'kCFCharacterSetIllegal',
               'kCFURLResourceAccessViolationError',
               'kCFNumberLongLongType',
               'kCFStringEncodingBig5_HKSCS_1999', 'CFSetEqualCallBack',
               'CFXMLAttributeListDeclarationInfo', 'kCFCalendarUnitEra',
               'kCFXMLStatusParseInProgress', 'kCFURLComponentUser',
               'CFNotificationSuspensionBehaviorCoalesce', 'CFDataRef',
               'kCFStringEncodingMacMongolian',
               'kCFStringEncodingWindowsKoreanJohab',
               'kCFPropertyListXMLFormat_v1_0',
               'kCFXMLNodeTypeDocumentType', 'CFNumberRef',
               'kCFCharacterSetNonBase', 'CFAbsoluteTime',
               'kCFStreamErrorDomainPOSIX', 'kCFCalendarUnitSecond',
               'kCFStringEncodingWindowsVietnamese',
               'kCFStringEncodingISOLatinArabic',
               'kCFStringEncodingMacDevanagari',
               'kCFStringEncodingUnicode', '__CFBoolean', 'CFDateRef',
               'CFNotificationSuspensionBehaviorDrop',
               'kCFMessagePortSendTimeout', 'CFNotificationCenterRef',
               'kCFStreamStatusWriting', 'CFTreeReleaseCallBack',
               'kCFStringEncodingMacCeltic',
               'kCFStreamEventOpenCompleted',
               'kCFStreamEventHasBytesAvailable',
               'kCFStringEncodingUTF16BE', '__CFSocket',
               'CFMutableBitVectorRef', 'CFBagReleaseCallBack',
               'kCFStringEncodingMacUkrainian',
               'kCFNumberFormatterRoundHalfEven',
               'CFRunLoopTimerCallBack', 'CFNumberFormatterOptionFlags',
               'CFXMLParserContext', 'kCFUserNotificationDefaultResponse',
               'kCFStringEncodingMacSymbol',
               'kCFCharacterSetDecimalDigit', 'kCFStringEncodingKOI8_U',
               'kCFStringEncodingKOI8_R', 'kCFStringEncodingMacCyrillic',
               'CFBagCallBacks', 'kCFPropertyListOpenStepFormat',
               'kCFStringEncodingISO_2022_CN', '__CFCharacterSet',
               'kCFNumberMaxType', 'CFBundleRef', 'CFURLError',
               'kCFUserNotificationPlainAlertLevel', 'CFUUIDBytes',
               'kCFStringEncodingISO_2022_JP',
               'kCFStringEncodingMacGujarati',
               'kCFSocketAutomaticallyReenableReadCallBack',
               'kCFStringEncodingDOSLatinUS', 'kCFNumberFloat64Type',
               'kCFXMLParserAllOptions', 'kCFURLWindowsPathStyle',
               'SInt8', 'kCFCompareEqualTo', 'UniChar', 'CFBagRef',
               'kCFStringEncodingMacThai', 'CFXMLParserOptions',
               'kCFXMLNodeTypeEntityReference',
               'kCFURLComponentResourceSpecifier',
               'kCFStringEncodingISOLatin8',
               'kCFXMLNodeTypeElementTypeDeclaration',
               'kCFStringEncodingDOSThai', 'CFByteOrderBigEndian',
               'kCFXMLNodeTypeElement', 'UInt32', 'CFMachPortContext',
               'kCFSocketError', '__CFBitVector', 'CFRunLoopRef',
               'CFStreamErrorDomain', 'kCFStringEncodingMacRoman',
               'kCFStringEncodingEUC_CN', '__CFUUID',
               'CFSetApplierFunction', 'kCFRunLoopAllActivities',
               '__CFNumberFormatter', 'kCFSocketNoCallBack', 'u_int64_t',
               'kCFXMLErrorMalformedProcessingInstruction',
               'kCFStreamEventEndEncountered',
               'CFDictionaryApplierFunction', 'CFGregorianDate',
               'CFGregorianUnitFlags', 'CFSetRef',
               'kCFStringEncodingMacArabic',
               'kCFCharacterSetAlphaNumeric', 'CFRunLoopSourceContext1',
               'CFNotificationCallback', 'kCFGregorianUnitsHours',
               'kCFStringNormalizationFormKD',
               'kCFStringNormalizationFormKC',
               'kCFStringEncodingWindowsLatin2', 'kCFNumberFloatType',
               'kCFNumberFormatterScientificStyle',
               'kCFUserNotificationOtherResponse',
               'kCFSocketAcceptCallBack', 'kCFDateFormatterNoStyle',
               'CFSocketContext', 'CFBagCopyDescriptionCallBack',
               'kCFStringEncodingDOSChineseSimplif',
               'CFStringNormalizationForm', 'CFSocketSignature',
               'kCFStringNormalizationFormC', 'kCFGregorianUnitsDays',
               'CFAttributedStringRef', 'CFArrayReleaseCallBack',
               'kCFStringNormalizationFormD', 'kCFStringEncodingUTF16',
               'CFXMLDocumentInfo', 'kCFStreamStatusClosed',
               'kCFStringEncodingDOSGreek1', 'kCFStringEncodingDOSGreek2',
               'kCFStringEncodingCNS_11643_92_P1',
               'kCFStringEncodingCNS_11643_92_P3',
               'kCFStringEncodingCNS_11643_92_P2',
               'kCFStringEncodingGBK_95', '__CFWriteStream',
               'kCFStringEncodingISOLatinCyrillic', 'u_int32_t',
               'CFSetReleaseCallBack', 'CFMachPortCallBack',
               'kCFPropertyListMutableContainersAndLeaves',
               'kCFCharacterSetControl', 'kCFStreamStatusOpen',
               'CFUserNotificationRef', 'CFNumberFormatterRef',
               'kCFCalendarUnitWeekdayOrdinal',
               'kCFStringEncodingDOSCanadianFrench', 'mach_port_name_t',
               'kCFStringEncodingShiftJIS_X0213_00',
               'kCFNumberFormatterPadAfterSuffix',
               'kCFStringEncodingKSC_5601_87', '__CFArray', 'CFPlugInRef',
               'CFNotificationSuspensionBehaviorDeliverImmediately',
               'kCFStringEncodingDOSPortuguese', 'CFSocketCallBack',
               'kCFStringEncodingMacGreek',
               'kCFStreamEventCanAcceptBytes', 'kCFCompareLessThan',
               'kCFStringEncodingISOLatinThai', 'CFComparisonResult',
               'kCFStringEncodingISOLatin9',
               'kCFXMLParserValidateDocument',
               'kCFStringEncodingISOLatin7', 'kCFStringEncodingISOLatin6',
               'kCFStringEncodingISOLatin5', 'kCFStringEncodingISOLatin4',
               'kCFStringEncodingISOLatin3', 'kCFStringEncodingISOLatin2',
               'kCFStringEncodingISOLatin1',
               'kCFXMLStatusParseSuccessful', 'kCFCompareNonliteral',
               'CFStringRef', 'kCFCharacterSetWhitespace',
               'kCFStringEncodingMacOriya',
               'kCFStringEncodingMacDingbats',
               'kCFStringEncodingDOSLatin2', 'kCFStringEncodingDOSLatin1',
               'kCFStringEncodingDOSCyrillic',
               'kCFXMLNodeTypeProcessingInstruction',
               'CFXMLParserEndXMLStructureCallBack',
               'CFRunLoopObserverCallBack', 'kCFStringEncodingMacInuit',
               'kCFURLComponentQuery', 'kCFStringEncodingISOLatinGreek',
               'kCFRunLoopBeforeTimers', '__CFTree',
               'CFXMLParserResolveExternalEntityCallBack',
               'kCFStringEncodingMacMalayalam',
               'kCFStringEncodingMacTurkish', 'CFXMLEntityTypeCode',
               'kCFCharacterSetDecomposable',
               'CFSetCopyDescriptionCallBack',
               'CFXMLElementTypeDeclarationInfo', 'CFURLRef',
               'CFTimeInterval', 'CFXMLParserRef',
               'CFBinaryHeapCompareContext', 'kCFStringEncodingASCII',
               'kCFStringEncodingEUC_JP', 'kCFXMLNodeTypeEntity',
               'kCFStringEncodingNextStepLatin', 'kCFNumberIntType',
               'kCFUserNotificationNoDefaultButtonFlag',
               'kCFStringEncodingHZ_GB_2312', 'uint64_t',
               'kCFXMLParserSkipWhitespace',
               'kCFXMLErrorMalformedStartTag',
               'kCFXMLEntityTypeCharacter',
               'CFPlugInInstanceGetInterfaceFunction',
               'kCFNumberFormatterPadBeforePrefix',
               'kCFStringEncodingMacTelugu', 'kCFStreamStatusError',
               'CFRunLoopActivity',
               'kCFSocketAutomaticallyReenableWriteCallBack',
               'CFTreeRetainCallBack', 'kCFStringEncodingMacVietnamese',
               'kCFNumberFormatterSpellOutStyle', 'kCFSocketTimeout',
               'CFSwappedFloat32', '__CFRunLoopObserver',
               'kCFXMLParserNoOptions', 'CFCharacterSetRef',
               'CFByteOrderLittleEndian', '__CFDictionary',
               'kCFStreamEventNone', 'CFXMLParserCopyDescriptionCallBack',
               'kCFNumberFormatterNoStyle', 'kCFURLComponentNetLocation',
               'UInt8', 'CFDictionaryKeyCallBacks',
               'kCFNotificationPostToAllSessions',
               'kCFNumberFormatterRoundHalfUp',
               'kCFStringEncodingShiftJIS_X0213_MenKuTen',
               'CFXMLParserCallBacks', 'kCFPropertyListBinaryFormat_v1_0',
               'Boolean', 'CFPropertyListMutabilityOptions',
               'CFMutableStringRef', 'kCFDateFormatterShortStyle',
               'kCFStringEncodingMacKorean', 'kCFSocketWriteCallBack',
               'CFArrayEqualCallBack', 'CFAllocatorReleaseCallBack',
               'kCFURLComponentHost', 'CFAllocatorReallocateCallBack',
               'CFURLComponentType', 'kCFXMLNodeTypeDocumentFragment',
               'CFSocketNativeHandle', 'kCFStringEncodingNonLossyASCII',
               'kCFStringEncodingDOSGreek', 'kCFXMLNodeTypeAttribute',
               '__CFNotificationCenter', 'kCFStringEncodingMacCroatian',
               'kCFCalendarUnitMonth', 'kCFStreamStatusNotOpen',
               '__CFData', 'CFMachPortInvalidationCallBack', '__CFDate',
               'CFTypeRef', '__CFAllocator',
               'kCFStringEncodingISOLatinHebrew', 'CFXMLTreeRef',
               'kCFStringEncodingMacKhmer', 'kCFRunLoopRunTimedOut',
               'kCFCalendarUnitMinute', 'kCFMessagePortIsInvalid',
               'kCFXMLParserReplacePhysicalEntities', 'CFURLPathStyle',
               'kCFXMLNodeTypeText', 'kCFXMLEntityTypeParameter',
               'CFGregorianUnits', 'kCFNumberFormatterRoundUp',
               'CFRunLoopSourceContext', 'kCFURLUnknownPropertyKeyError',
               'kCFNumberFormatterRoundHalfDown', 'kCFCompareNumerically',
               '__CFAttributedString', 'kCFStringEncodingDOSNordic',
               'kCFStringEncodingMacCentralEurRoman', 'CFStringEncoding',
               'CFTimeZoneRef', 'CFBinaryHeapCallBacks', '__CFSet',
               'kCFXMLErrorElementlessDocument',
               'kCFStreamErrorDomainMacOSStatus',
               'kCFGregorianUnitsMinutes', 'kCFXMLNodeTypeNotation',
               'kCFMessagePortSuccess', 'kCFStringEncodingMacTamil',
               'kCFNumberCFIndexType', 'CFStringEncodings',
               'CFAllocatorCopyDescriptionCallBack',
               'kCFRunLoopAfterWaiting', 'CFXMLNodeTypeCode',
               'kCFRunLoopRunHandledSource',
               'kCFStringEncodingMacEthiopic', 'kCFStringEncodingUTF32LE',
               'kCFStreamEventErrorOccurred', 'CFTreeContext',
               'kCFStreamStatusReading',
               'kCFNotificationDeliverImmediately', '__CFTimeZone',
               'CFSocketCallBackType', 'CFRunLoopTimerContext',
               'kCFNumberSInt16Type', 'kCFCalendarUnitWeek',
               'kCFStringEncodingDOSArabic', 'CFXMLParserReleaseCallBack',
               'kCFXMLErrorEncodingConversionFailure',
               'kCFRunLoopBeforeSources', 'kCFXMLNodeTypeDocument',
               'kCFRunLoopExit', 'kCFStringEncodingNextStepJapanese',
               'kCFStringEncodingJIS_C6226_78', 'kCFNumberLongType',
               'CFAllocatorAllocateCallBack', 'kCFNumberDoubleType',
               'CFMutableArrayRef', 'kCFXMLErrorMalformedCDSect',
               'kCFStringEncodingMacTibetan',
               'kCFPropertyListMutableContainers',
               'kCFStringEncodingDOSBalticRim', 'CFLocaleRef',
               'CFSocketRef', 'kCFXMLParserAddImpliedAttributes',
               'kCFStringEncodingMacArmenian',
               'kCFStringEncodingDOSHebrew',
               'kCFXMLEntityTypeParsedInternal', '__CFBag',
               'kCFStringEncodingEUC_KR',
               'CFMessagePortInvalidationCallBack',
               'CFDateFormatterStyle', 'CFSocketError',
               'CFDateFormatterRef', 'CFAllocatorDeallocateCallBack',
               'CFXMLProcessingInstructionInfo', 'CFRange',
               'kCFStringEncodingUTF16LE',
               'CFDictionaryCopyDescriptionCallBack',
               'kCFXMLStatusParseNotBegun', 'kCFSocketCloseOnInvalidate',
               'kCFStringEncodingMacVT100', 'kCFNumberFloat32Type',
               'kCFStreamErrorDomainCustom', 'kCFStreamStatusOpening',
               'CFStringBuiltInEncodings', 'CFXMLNotationInfo',
               'kCFSocketConnectCallBack',
               'kCFStringEncodingMacChineseTrad', 'CFSwappedFloat64',
               'kCFNumberSInt64Type', 'kCFStringEncodingMacFarsi',
               'kCFNumberFormatterParseIntegersOnly',
               'kCFXMLNodeTypeAttributeListDeclaration',
               'kCFStringEncodingWindowsGreek',
               'kCFStringEncodingDOSJapanese', 'kCFXMLNodeCurrentVersion',
               'SInt32', 'kCFURLComponentFragment',
               'kCFURLPropertyKeyUnavailableError', 'CFByteOrderUnknown',
               'CFStringCompareFlags', 'kCFNumberFormatterPercentStyle',
               'CFTypeID', 'kCFURLComponentScheme',
               'CFNotificationSuspensionBehaviorHold',
               'kCFURLComponentPath', 'kCFStringEncodingJIS_X0201_76',
               'kCFURLComponentUserInfo', 'CFRunLoopObserverRef',
               'kCFUserNotificationCancelResponse',
               'kCFXMLErrorUnexpectedEOF', '__CFXMLNode', 'UInt16',
               'kCFStringEncodingWindowsCyrillic',
               'kCFXMLErrorMalformedParsedCharacterData',
               'kCFStringEncodingWindowsHebrew',
               'kCFStringEncodingGB_18030_2000',
               'kCFNumberFormatterRoundDown',
               'kCFStringEncodingISO_2022_JP_2',
               'kCFStringEncodingISO_2022_JP_3',
               'kCFStringEncodingWindowsLatin1',
               'kCFStringEncodingISO_2022_JP_1',
               'kCFStringEncodingWindowsLatin5',
               'kCFUserNotificationCautionAlertLevel',
               'kCFNumberCharType',
               'kCFUserNotificationAlternateResponse',
               'kCFStringEncodingEBCDIC_US', 'kCFNumberSInt32Type',
               'CFXMLEntityInfo', 'kCFCalendarUnitWeekday',
               'CFArrayRetainCallBack', 'uint32_t',
               'CFDictionaryHashCallBack',
               'kCFCharacterSetUppercaseLetter',
               'kCFUserNotificationNoteAlertLevel',
               'kCFCharacterSetCapitalizedLetter', 'CFBagEqualCallBack',
               'kCFStringEncodingMacRomanLatin1',
               'CFXMLParserCreateXMLStructureCallBack',
               'CFXMLAttributeDeclarationInfo',
               'kCFStringEncodingISOLatin10', 'kCFStringEncodingVISCII',
               'CFMutableBagRef', '__CFRunLoopSource',
               'CFAllocatorPreferredSizeCallBack', 'CFNumberType',
               'CFHashCode', 'kCFStringEncodingBig5_E',
               'CFXMLParserHandleErrorCallBack', 'CFPlugInUnloadFunction',
               'CFArrayCallBacks', 'kCFXMLEntityTypeUnparsed',
               'kCFCharacterSetWhitespaceAndNewline',
               'kCFStringEncodingMacJapanese',
               'kCFStringEncodingDOSChineseTrad', 'CFByteOrder',
               'kCFCharacterSetSymbol', '__CFURL',
               'CFPlugInInstanceDeallocateInstanceDataFunction',
               'natural_t', '__CFXMLParser', 'mach_port_t',
               'CFAllocatorContext', 'kCFNumberFormatterRoundCeiling',
               'CFDictionaryEqualCallBack', 'kCFStringEncodingBig5',
               'CFOptionFlags', 'kCFStringEncodingJIS_X0208_83',
               'kCFURLTimeoutError', 'CFPropertyListFormat',
               'CFBagRetainCallBack', 'kCFURLRemoteHostUnavailableError',
               'kCFStringEncodingISO_2022_CN_EXT', 'kCFURLComponentPort',
               'kCFNumberFormatterDecimalStyle',
               'kCFCalendarComponentsWrap', 'CFStreamClientContext',
               'CFBagApplierFunction', 'kCFURLUnknownError',
               'kCFNumberSInt8Type', 'kCFXMLErrorMalformedDocument',
               'kCFStringEncodingUTF8', 'kCFStringEncodingDOSTurkish',
               'kCFRunLoopRunStopped', 'CFXMLParserRetainCallBack',
               'CFArrayCopyDescriptionCallBack', 'kCFStreamStatusAtEnd',
               'kCFURLImproperArgumentsError', 'kCFSocketReadCallBack',
               'CFNumberFormatterPadPosition', 'CFRunLoopTimerRef',
               'kCFGregorianUnitsYears', 'CFDictionaryRef',
               'kCFStringEncodingJIS_X0212_90', 'CFBooleanRef',
               'CFXMLDocumentTypeInfo', 'CFStringInlineBuffer',
               'CFBitVectorRef', 'CFReadStreamClientCallBack',
               'CFWriteStreamRef', '__CFDateFormatter',
               'kCFStringEncodingMacGurmukhi',
               'CFXMLParserAddChildCallBack', 'kCFStringEncodingUTF32',
               'CFSetCallBacks', 'kCFStringEncodingISO_2022_KR',
               'CFCalendarUnit', 'kCFURLComponentParameterString',
               'kCFUserNotificationStopAlertLevel',
               'kCFStringEncodingDOSRussian', '__CFLocale',
               'kCFStringEncodingMacChineseSimp',
               'kCFMessagePortTransportError', 'CFStreamError',
               'kCFStringEncodingWindowsArabic', 'CFSetRetainCallBack',
               'kCFSocketAutomaticallyReenableAcceptCallBack',
               'CFDictionaryReleaseCallBack',
               'CFPlugInDynamicRegisterFunction',
               'CFDictionaryRetainCallBack',
               'kCFStringEncodingWindowsBalticRim', 'CFStreamStatus',
               'kCFStringEncodingMacHFS', 'kCFRunLoopEntry',
               'CFDictionaryValueCallBacks', '__CFRunLoop',
               'kCFXMLErrorUnknownEncoding', 'kCFCompareCaseInsensitive',
               'kCFNumberFormatterCurrencyStyle',
               'kCFXMLNodeTypeWhitespace', 'CFMessagePortCallBack',
               'kCFStringEncodingMacSinhalese',
               'CFMutableAttributedStringRef', 'CFMachPortRef',
               'kCFMessagePortReceiveTimeout', 'CFSetHashCallBack',
               'CFBinaryHeapApplierFunction',
               'kCFStringEncodingMacLaotian', 'CFXMLEntityReferenceInfo',
               'CFAllocatorRetainCallBack', 'kCFGregorianAllUnits',
               '__CFReadStream', 'CFAllocatorRef',
               'kCFCharacterSetLowercaseLetter', 'CFReadStreamRef',
               'kCFCalendarUnitDay', 'kCFDateFormatterFullStyle',
               '__CFCalendar', '__CFMessagePort',
               'kCFStringEncodingMacKannada', '__CFUserNotification',
               'kCFStringEncodingEUC_TW', 'kCFCalendarUnitHour',
               'CFMessagePortRef', 'CFXMLNodeRef']
