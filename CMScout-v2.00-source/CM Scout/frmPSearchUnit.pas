unit frmPSearchUnit;

{ $Id: frmPSearchUnit.pas,v 1.1.1.1 2002/04/24 12:15:43 michael Exp $ }

interface

uses
  Forms, StdCtrls, Spin, Controls, ComCtrls, Classes, Windows;

type
  TFfrmPSearch = class(TForm)
    FpcSearchOptions: TPageControl;
    FtsGeneral: TTabSheet;
    FtsAttributes1: TTabSheet;
    FgbGeneral: TGroupBox;
    FlblName: TLabel;
    FedName: TEdit;
    FlblAge: TLabel;
    FlblNation: TLabel;
    FcbEUNational: TCheckBox;
    FlblDivision: TLabel;
    FlblBased: TLabel;
    FspeMinAge: TSpinEdit;
    FcmbNation: TComboBox;
    FcmbBased: TComboBox;
    FcmbDivision: TComboBox;
    FspeMaxAge: TSpinEdit;
    FlblAgeLine: TLabel;
    FgbPositions: TGroupBox;
    FcbGoalkeeper: TCheckBox;
    FcbDefender: TCheckBox;
    FcbDefensiveMidfielder: TCheckBox;
    FcbMidfielder: TCheckBox;
    FcbAttackingMidfielder: TCheckBox;
    FcbAttacker: TCheckBox;
    FcbSweeper: TCheckBox;
    FcbLeftSide: TCheckBox;
    FcbFreeRole: TCheckBox;
    FcbCentral: TCheckBox;
    FcbRightSide: TCheckBox;
    FcbWingBack: TCheckBox;
    FgbAbility: TGroupBox;
    FlblAbility: TLabel;
    FlblPotentialAbility: TLabel;
    FlblScoutRating: TLabel;
    FspeAbilityMin: TSpinEdit;
    FspePotentialAbilityMin: TSpinEdit;
    FspeScoutRatingMin: TSpinEdit;
    FspeAbilityMax: TSpinEdit;
    FspePotentialAbilityMax: TSpinEdit;
    FspeScoutRatingMax: TSpinEdit;
    FlblAbilityLine: TLabel;
    FlblPotentialAbilityLine: TLabel;
    FlblScoutRatingLine: TLabel;
    FgbReputation: TGroupBox;
    FlblHomeReputation: TLabel;
    FspeHomeReputationMin: TSpinEdit;
    FspeHomeReputationMax: TSpinEdit;
    FlblHomeReputationLine: TLabel;
    FlblCurrentReputation: TLabel;
    FspeCurrentReputationMin: TSpinEdit;
    FspeCurrentReputationMax: TSpinEdit;
    FlblCurrentReputationLine: TLabel;
    FlblWorldReputation: TLabel;
    FspeWorldReputationMin: TSpinEdit;
    FspeWorldReputationMax: TSpinEdit;
    FlblWorldReputationLine: TLabel;
    FlblClubReputation: TLabel;
    FspeClubReputationMin: TSpinEdit;
    FspeClubReputationMax: TSpinEdit;
    FlblClubReputationLine: TLabel;
    FbtnOK: TButton;
    FbtnCancel: TButton;
    FbtnReset: TButton;
    FtsContract: TTabSheet;
    FgbContract: TGroupBox;
    FlblContract: TLabel;
    FcmbContract: TComboBox;
    FcbBosman: TCheckBox;
    FcbTransferArranged: TCheckBox;
    FgbStatus: TGroupBox;
    FlblTransferStatus: TLabel;
    FcmbTransferStatus: TComboBox;
    FlblSquadStatus: TLabel;
    FcmbSquadStatus: TComboBox;
    FgbReleaseClauses: TGroupBox;
    FcbNonPromotion: TCheckBox;
    FcbNonPromotionActive: TCheckBox;
    FcbRelegation: TCheckBox;
    FcbRelegationActive: TCheckBox;
    FcbNonPlaying: TCheckBox;
    FcbNonPlayingActive: TCheckBox;
    FcbMinimumFee: TCheckBox;
    FlblReleaseFee: TLabel;
    FlblReleaseFeeLine: TLabel;
    FspeMinReleaseFee: TSpinEdit;
    FspeMaxReleaseFee: TSpinEdit;
    FgbContractDetails: TGroupBox;
    FlblContractType: TLabel;
    FcmbContractType: TComboBox;
    FlblValue: TLabel;
    FlblWage: TLabel;
    FspeMinValue: TSpinEdit;
    FspeMaxValue: TSpinEdit;
    FlblValueLine: TLabel;
    FlblWageLine: TLabel;
    FspeMinWage: TSpinEdit;
    FspeMaxWage: TSpinEdit;
    FlblAcceleration: TLabel;
    FspeMinAcceleration: TSpinEdit;
    FspeMaxAcceleration: TSpinEdit;
    FlblAccelerationLine: TLabel;
    FlblDecisions: TLabel;
    FspeMinDecisions: TSpinEdit;
    FspeMaxDecisions: TSpinEdit;
    FlblDecisionsLine: TLabel;
    FlblAdaptability: TLabel;
    FspeMinAdaptability: TSpinEdit;
    FspeMaxAdaptability: TSpinEdit;
    FlblAdaptabilityLine: TLabel;
    FlblDetermination: TLabel;
    FspeMinDetermination: TSpinEdit;
    FspeMaxDetermination: TSpinEdit;
    FlblDeterminationLine: TLabel;
    FlblAggression: TLabel;
    FspeMinAggression: TSpinEdit;
    FspeMaxAggression: TSpinEdit;
    FlblAggressionLine: TLabel;
    FlblDirtiness: TLabel;
    FspeMinDirtiness: TSpinEdit;
    FspeMaxDirtiness: TSpinEdit;
    FlblDirtinessLine: TLabel;
    FlblAgility: TLabel;
    FspeMinAgility: TSpinEdit;
    FspeMaxAgility: TSpinEdit;
    FlblAgilityLine: TLabel;
    FlblDribbling: TLabel;
    FspeMinDribbling: TSpinEdit;
    FspeMaxDribbling: TSpinEdit;
    FlblDribblingLine: TLabel;
    FlblAmbition: TLabel;
    FspeMinAmbition: TSpinEdit;
    FspeMaxAmbition: TSpinEdit;
    FlblAmbitionLine: TLabel;
    FlblFinishing: TLabel;
    FspeMinFinishing: TSpinEdit;
    FspeMaxFinishing: TSpinEdit;
    FlblFinishingLine: TLabel;
    FlblAnticipation: TLabel;
    FspeMinAnticipation: TSpinEdit;
    FspeMaxAnticipation: TSpinEdit;
    FlblAnticipationLine: TLabel;
    FlblFlair: TLabel;
    FspeMinFlair: TSpinEdit;
    FspeMaxFlair: TSpinEdit;
    FlblFlairLine: TLabel;
    FlblBalance: TLabel;
    FspeMinBalance: TSpinEdit;
    FspeMaxBalance: TSpinEdit;
    FlblBalanceLine: TLabel;
    FlblHandling: TLabel;
    FspeMinHandling: TSpinEdit;
    FspeMaxHandling: TSpinEdit;
    FlblHandlingLine: TLabel;
    FlblBravery: TLabel;
    FspeMinBravery: TSpinEdit;
    FspeMaxBravery: TSpinEdit;
    FlblBraveryLine: TLabel;
    FlblConsistency: TLabel;
    FspeMinConsistency: TSpinEdit;
    FspeMaxConsistency: TSpinEdit;
    FlblConsistencyLine: TLabel;
    FlblCorners: TLabel;
    FspeMinCorners: TSpinEdit;
    FspeMaxCorners: TSpinEdit;
    FlblCornersLine: TLabel;
    FlblVision: TLabel;
    FspeMinVision: TSpinEdit;
    FspeMaxVision: TSpinEdit;
    FlblVisionLine: TLabel;
    FlblCrossing: TLabel;
    FspeMinCrossing: TSpinEdit;
    FspeMaxCrossing: TSpinEdit;
    FlblCrossingLine: TLabel;
    FtsAttributes2: TTabSheet;
    FlblHeading: TLabel;
    FlblHeadingLine: TLabel;
    FspeMinHeading: TSpinEdit;
    FspeMaxHeading: TSpinEdit;
    FlblLeadership: TLabel;
    FlblLeadershipLine: TLabel;
    FspeMinLeadership: TSpinEdit;
    FspeMaxLeadership: TSpinEdit;
    FlblImportantMatches: TLabel;
    FlblImportantMatchesLine: TLabel;
    FspeMinImportantMatches: TSpinEdit;
    FspeMaxImportantMatches: TSpinEdit;
    FlblInjuryProneness: TLabel;
    FlblInjuryPronenessLine: TLabel;
    FspeMinInjuryProneness: TSpinEdit;
    FspeMaxInjuryProneness: TSpinEdit;
    FlblJumping: TLabel;
    FlblJumpingLine: TLabel;
    FspeMaxJumping: TSpinEdit;
    FspeMinJumping: TSpinEdit;
    FlblLongShots: TLabel;
    FlblLongShotsLine: TLabel;
    FspeMinLongShots: TSpinEdit;
    FspeMaxLongShots: TSpinEdit;
    FlblLoyality: TLabel;
    FlblLoyalityLine: TLabel;
    FspeMinLoyality: TSpinEdit;
    FspeMaxLoyality: TSpinEdit;
    FlblMarking: TLabel;
    FlblMarkingLine: TLabel;
    FspeMinMarking: TSpinEdit;
    FspeMaxMarking: TSpinEdit;
    FlblNaturalFitness: TLabel;
    FlblNaturalFitnessLine: TLabel;
    FspeMinNaturalFitness: TSpinEdit;
    FspeMaxNaturalFitness: TSpinEdit;
    FlblMovement: TLabel;
    FlblMovementLine: TLabel;
    FspeMinMovement: TSpinEdit;
    FspeMaxMovement: TSpinEdit;
    FlblOneOnOnes: TLabel;
    FlblOneOnOnesLine: TLabel;
    FspeMinOneOnOnes: TSpinEdit;
    FspeMaxOneOnOnes: TSpinEdit;
    FlblPlayerPace: TLabel;
    FlblPlayerPaceLine: TLabel;
    FspeMinPlayerPace: TSpinEdit;
    FspeMaxPlayerPace: TSpinEdit;
    FlblPassing: TLabel;
    FlblPassingLine: TLabel;
    FspeMinPassing: TSpinEdit;
    FspeMaxPassing: TSpinEdit;
    FlblPenalties: TLabel;
    FlblPenaltiesLine: TLabel;
    FspeMinPenalties: TSpinEdit;
    FspeMaxPenalties: TSpinEdit;
    FlblPositioning: TLabel;
    FlblPositioningLine: TLabel;
    FspeMinPositioning: TSpinEdit;
    FspeMaxPositioning: TSpinEdit;
    FlblPressure: TLabel;
    FlblPressureLine: TLabel;
    FspeMinPressure: TSpinEdit;
    FspeMaxPressure: TSpinEdit;
    FlblProfessionalism: TLabel;
    FlblProfessionalismLine: TLabel;
    FspeMinProfessionalism: TSpinEdit;
    FspeMaxProfessionalism: TSpinEdit;
    FlblReflexes: TLabel;
    FlblReflexesLine: TLabel;
    FspeMinReflexes: TSpinEdit;
    FspeMaxReflexes: TSpinEdit;
    FlblFreeKicks: TLabel;
    FlblFreeKicksLine: TLabel;
    FspeMinFreeKicks: TSpinEdit;
    FspeMaxFreeKicks: TSpinEdit;
    FlblSportsmanship: TLabel;
    FlblSportsmanshipLine: TLabel;
    FspeMinSportsmanship: TSpinEdit;
    FspeMaxSportsmanship: TSpinEdit;
    FlblStamina: TLabel;
    FlblStaminaLine: TLabel;
    FspeMinStamina: TSpinEdit;
    FspeMaxStamina: TSpinEdit;
    FlblStrength: TLabel;
    FlblStrengthLine: TLabel;
    FspeMinStrength: TSpinEdit;
    FspeMaxStrength: TSpinEdit;
    FlblTackling: TLabel;
    FlblTacklingLine: TLabel;
    FspeMinTackling: TSpinEdit;
    FspeMaxTackling: TSpinEdit;
    FlblTeamwork: TLabel;
    FlblTeamworkLine: TLabel;
    FspeMinTeamwork: TSpinEdit;
    FspeMaxTeamwork: TSpinEdit;
    FlblTechnique: TLabel;
    FlblTechniqueLine: TLabel;
    FspeMinTechnique: TSpinEdit;
    FspeMaxTechnique: TSpinEdit;
    FlblTemperament: TLabel;
    FlblTemperamentLine: TLabel;
    FspeMinTemperament: TSpinEdit;
    FspeMaxTemperament: TSpinEdit;
    FlblThrowIns: TLabel;
    FlblThrowInsLine: TLabel;
    FspeMinThrowIns: TSpinEdit;
    FspeMaxThrowIns: TSpinEdit;
    FlblVersatility: TLabel;
    FlblVersatilityLine: TLabel;
    FspeMinVersatility: TSpinEdit;
    FspeMaxVersatility: TSpinEdit;
    FlblWorkRate: TLabel;
    FlblWorkRateLine: TLabel;
    FspeMinWorkRate: TSpinEdit;
    FspeMaxWorkRate: TSpinEdit;
    procedure FspeKeyDown(Sender: TObject; var Key: Word;
      Shift: TShiftState);
    procedure FbtnResetClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FfrmPSearch: TFfrmPSearch;

implementation

{$R *.DFM}

procedure TFfrmPSearch.FspeKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
  if (Ord(Key) = VK_RETURN) then
    FbtnOK.Click;
  if (Ord(Key) = VK_ESCAPE) then
    FbtnCancel.Click;
end;

procedure TFfrmPSearch.FbtnResetClick(Sender: TObject);
begin
  FedName.Text:='';
  FspeMinAge.Value:=0;
  FspeMaxAge.Value:=0;
  FcmbNation.ItemIndex:=-1;
  FcmbNation.Text:='';
  FcbEUNational.Checked:=False;
  FcmbBased.ItemIndex:=-1;
  FcmbBased.Text:='';
  FcmbDivision.ItemIndex:=-1;
  FcmbDivision.Text:='';

  FcbGoalkeeper.Checked:=False;
  FcbDefender.Checked:=False;
  FcbMidfielder.Checked:=False;
  FcbAttacker.Checked:=False;
  FcbSweeper.Checked:=False;
  FcbDefensiveMidfielder.Checked:=False;
  FcbAttackingMidfielder.Checked:=False;
  FcbLeftSide.Checked:=False;
  FcbCentral.Checked:=False;
  FcbRightSide.Checked:=False;
  FcbWingBack.Checked:=False;
  FcbFreeRole.Checked:=False;

  FspeAbilityMin.Value:=0;
  FspeAbilityMax.Value:=200;
  FspePotentialAbilityMin.Value:=0;
  FspePotentialAbilityMax.Value:=200;
  FspeScoutRatingMin.Value:=0;
  FspeScoutRatingMax.Value:=100;

  FspeHomeReputationMin.Value:=0;
  FspeHomeReputationMax.Value:=10000;
  FspeCurrentReputationMin.Value:=0;
  FspeCurrentReputationMax.Value:=10000;
  FspeWorldReputationMin.Value:=0;
  FspeWorldReputationMax.Value:=10000;
  FspeClubReputationMin.Value:=0;
  FspeClubReputationMax.Value:=10000;

  FcmbContract.ItemIndex:=-1;
  FcmbContract.Text:='';
  FcbBosman.Checked:=False;
  FcbTransferArranged.Checked:=False;

  FcbNonPromotion.Checked:=False;
  FcbNonPromotionActive.Checked:=False;
  FcbRelegation.Checked:=False;
  FcbRelegationActive.Checked:=False;
  FcbNonPlaying.Checked:=False;
  FcbNonPlayingActive.Checked:=False;
  FcbMinimumFee.Checked:=False;
  FspeMinReleaseFee.Value:=0;
  FspeMaxReleaseFee.Value:=0;

  FcmbTransferStatus.ItemIndex:=-1;
  FcmbTransferStatus.Text:='';
  FcmbSquadStatus.ItemIndex:=-1;
  FcmbSquadStatus.Text:='';

  FcmbContractType.ItemIndex:=-1;
  FcmbContractType.Text:='';
  FspeMinValue.Value:=0;
  FspeMaxValue.Value:=0;
  FspeMinWage.Value:=0;
  FspeMaxWage.Value:=0;

  FspeMinAcceleration.Value:=0;
  FspeMaxAcceleration.Value:=20;
  FspeMinAdaptability.Value:=0;
  FspeMaxAdaptability.Value:=20;
  FspeMinAggression.Value:=0;
  FspeMaxAggression.Value:=20;
  FspeMinAgility.Value:=0;
  FspeMaxAgility.Value:=20;
  FspeMinAmbition.Value:=0;
  FspeMaxAmbition.Value:=20;
  FspeMinAnticipation.Value:=0;
  FspeMaxAnticipation.Value:=20;
  FspeMinBalance.Value:=0;
  FspeMaxBalance.Value:=20;
  FspeMinBravery.Value:=0;
  FspeMaxBravery.Value:=20;
  FspeMinConsistency.Value:=0;
  FspeMaxConsistency.Value:=20;
  FspeMinCorners.Value:=0;
  FspeMaxCorners.Value:=20;
  FspeMinVision.Value:=0;
  FspeMaxVision.Value:=20;
  FspeMinCrossing.Value:=0;
  FspeMaxCrossing.Value:=20;

  FspeMinDecisions.Value:=0;
  FspeMaxDecisions.Value:=20;
  FspeMinDetermination.Value:=0;
  FspeMaxDetermination.Value:=20;
  FspeMinDirtiness.Value:=0;
  FspeMaxDirtiness.Value:=20;
  FspeMinDribbling.Value:=0;
  FspeMaxDribbling.Value:=20;
  FspeMinFinishing.Value:=0;
  FspeMaxFinishing.Value:=20;
  FspeMinFlair.Value:=0;
  FspeMaxFlair.Value:=20;
  FspeMinHandling.Value:=0;
  FspeMaxHandling.Value:=20;
  FspeMinHeading.Value:=0;
  FspeMaxHeading.Value:=20;
  FspeMinLeadership.Value:=0;
  FspeMaxLeadership.Value:=20;
  FspeMinImportantMatches.Value:=0;
  FspeMaxImportantMatches.Value:=20;
  FspeMinInjuryProneness.Value:=0;
  FspeMaxInjuryProneness.Value:=20;
  FspeMinJumping.Value:=0;
  FspeMaxJumping.Value:=20;

  FspeMinLongShots.Value:=0;
  FspeMaxLongShots.Value:=20;
  FspeMinLoyality.Value:=0;
  FspeMaxLoyality.Value:=20;
  FspeMinMarking.Value:=0;
  FspeMaxMarking.Value:=20;
  FspeMinNaturalFitness.Value:=0;
  FspeMaxNaturalFitness.Value:=20;
  FspeMinMovement.Value:=0;
  FspeMaxMovement.Value:=20;
  FspeMinOneOnOnes.Value:=0;
  FspeMaxOneOnOnes.Value:=20;
  FspeMinPlayerPace.Value:=0;
  FspeMaxPlayerPace.Value:=20;
  FspeMinPassing.Value:=0;
  FspeMaxPassing.Value:=20;
  FspeMinPenalties.Value:=0;
  FspeMaxPenalties.Value:=20;
  FspeMinPositioning.Value:=0;
  FspeMaxPositioning.Value:=20;
  FspeMinPressure.Value:=0;
  FspeMaxPressure.Value:=20;
  FspeMinProfessionalism.Value:=0;
  FspeMaxProfessionalism.Value:=20;

  FspeMinReflexes.Value:=0;
  FspeMaxReflexes.Value:=20;
  FspeMinFreeKicks.Value:=0;
  FspeMaxFreeKicks.Value:=20;
  FspeMinSportsmanship.Value:=0;
  FspeMaxSportsmanship.Value:=20;
  FspeMinStamina.Value:=0;
  FspeMaxStamina.Value:=20;
  FspeMinStrength.Value:=0;
  FspeMaxStrength.Value:=20;
  FspeMinTackling.Value:=0;
  FspeMaxTackling.Value:=20;
  FspeMinTeamwork.Value:=0;
  FspeMaxTeamwork.Value:=20;
  FspeMinTechnique.Value:=0;
  FspeMaxTechnique.Value:=20;
  FspeMinTemperament.Value:=0;
  FspeMaxTemperament.Value:=20;
  FspeMinThrowIns.Value:=0;
  FspeMaxThrowIns.Value:=20;
  FspeMinVersatility.Value:=0;
  FspeMaxVersatility.Value:=20;
  FspeMinWorkRate.Value:=0;
  FspeMaxWorkRate.Value:=20;
end;

end.
