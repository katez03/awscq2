.. _a6_diy:

===
DIY
===

Here’s the full set of steps:

#. In the DIY interface:

   * Read the **DIY ACTIVITIES**.
   * Read the **SOLUTION VALIDATION METHOD**.

   .. image:: pictures/0001-diy-A6.png
      :alt: DIY interface with activities and validation method instructions.
      :align: center
      :width: 600px

#. Select “**Open AWS Console**”.

   .. image:: pictures/0002-diy-A6.png
      :alt: AWS console button highlighted.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **VPC**.
   * Select **VPC**.
   * Select **Your VPCs**.
   * View the VPC.

   .. image:: pictures/0003-diy-A6.png
      :alt: AWS console showing VPC service and Your VPCs list.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **EC2**.
   * Select **EC2**.

   .. image:: pictures/0004-diy-A6.png
      :alt: AWS console showing EC2 service.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **Developer Server**.
   * Select **Details**.
   * View the **VPC ID**.
   * Select **Connect**.

   .. image:: pictures/0005-diy-A6.png
      :alt: EC2 interface showing instances, Developer Server selected, details viewed, and Connect button.
      :align: center
      :width: 600px

#. In the “**Connect to instance**” interface:

   * Select “**EC2 Instance Connect**”.
   * Select **Connect**.

   .. image:: pictures/0006-diy-A6.png
      :alt: Connect to instance options, EC2 Instance Connect selected and Connect button.
      :align: center
      :width: 600px

#. In the **CLI** interface:

   * Enter ``ping 172.31.0.10``.
   * View the results.

   .. image:: pictures/0007-diy-A6.png
      :alt: CLI with ping command and results.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select the **Developer Server**.
   * Select the **Subnet ID**.

   .. image:: pictures/0008-diy-A6.png
      :alt: Developer server details showing Subnet ID link.
      :align: center
      :width: 600px

#. In the **Subnet** interface:

   * Select **DeveloperPublicSubnet1**.
   * Select the **Route table**.

   .. image:: pictures/0009-diy-A6.png
      :alt: Subnet details page showing route table link.
      :align: center
      :width: 600px

#. In the **Route Tables** interface:

   * Select **DeveloperPublicSubnet1**.
   * Select **Routes**.
   * View the route rules.

   .. image:: pictures/00010-diy-A6.png
      :alt: Developer Public Route Table details showing Routes tab and existing rules.
      :align: center
      :width: 600px

#. In the **VPC** interface:

   * Select **Peering Connections**.
   * Select “**Create peering connection**”.

   .. image:: pictures/00011-diy-A6.png
      :alt: VPC menu showing Peering Connections and Create button.
      :align: center
      :width: 600px

#. In the **Peering Connection Settings** interface:

   * For **Name**, enter ``Developer <> Finance``.
   * For **VPC ID**, select your Dev VPC.
   * Under **Account**, select **My account**.
   * Under **Region**, select **This Region (us-east-1)**.

   .. image:: pictures/00012-diy-A6.png
      :alt: Configure peering connection settings.
      :align: center
      :width: 600px

#. In the **Peering Connection Settings** interface:

   * Select “**Create peering connection**”.

   .. image:: pictures/00013-diy-A6.png
      :alt: Clicking the Create peering connection button.
      :align: center
      :width: 600px

#. View the **Initialization result**.

   .. image:: pictures/00014-diy-A6.png
      :alt: Peering connection created, status pending acceptance.
      :align: center
      :width: 600px

#. In the **VPC** interface:

   * Select **Peering Connections**.
   * Select **Developer <> Finance**.
   * View the **Status**.
   * Select **Actions** → **Accept request**.

   .. image:: pictures/00015-diy-A6.png
      :alt: Peering connections list, select connection, view status, select accept action.
      :align: center
      :width: 600px

#. In the “**Accept VPC peering connection request**” interface:

   * Select “**Accept request**”.

   .. image:: pictures/00016-diy-A6.png
      :alt: Confirmation dialog to accept the peering request.
      :align: center
      :width: 600px

#. View the **Result** (the peering connection should be active).

   .. image:: pictures/00017-diy-A6.png
      :alt: Peering connection status is now active.
      :align: center
      :width: 600px

#. In the **VPC** interface:

   * Select **Route Tables**.
   * Select **DeveloperPublicSubnet1**.
   * Select **Routes**.
   * View the route rules.
   * Select **Edit routes**.

   .. image:: pictures/00018-diy-A6.png
      :alt: Navigate to Developer Public Route Table and select edit routes.
      :align: center
      :width: 600px

#. In the **Edit Routes** interface:

   * Select **Add route**.
   * In **Destination**, enter ``172.31.0.0/16``.
   * For **Target**, select **Developer <> Finance**.
   * Select **Save changes**.

   .. image:: pictures/00019-diy-A6.png
      :alt: Add route to Finance VPC in Developer RT.
      :align: center
      :width: 600px

#. View **Results after initialization** (Developer RT updated).

   .. image:: pictures/00020-diy-A6.png
      :alt: Developer Route Table with the new route added.
      :align: center
      :width: 600px

#. In the **VPC** interface:

   * Select **Route Tables**.
   * Select **FinancePrivateSubnet1**.
   * Select **Routes**.
   * View the route rules.
   * Select **Edit routes**.

   .. image:: pictures/00021-diy-A6.png
      :alt: Navigate to Finance Private Route Table and select edit routes.
      :align: center
      :width: 600px

#. In the **Edit Routes** interface:

   * Select **Add route**.
   * In **Destination**, enter ``192.168.0.10/32``.
   * In **Target**, select **Developer <> Finance**.
   * Select **Save changes**.

   .. image:: pictures/00022-diy-A6.png
      :alt: Add route to Developer IP in Finance RT.
      :align: center
      :width: 600px

#. View **Initialization result** (Finance RT updated).

   .. image:: pictures/00023-diy-A6.png
      :alt: Finance Route Table with the new route added.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **Developer Server**.
   * Select **Connect**.

   .. image:: pictures/00024-diy-A6.png
      :alt: Select Developer Server and Connect.
      :align: center
      :width: 600px

#. In the “**Connect to instance**” interface:

   * Select “**EC2 Instance Connect**”.
   * Select **Connect**.

   .. image:: pictures/00025-diy-A6.png
      :alt: Connect to instance via EC2 Instance Connect.
      :align: center
      :width: 600px

#. In the **Developer Server CLI**:

   * Enter ``ping 172.31.0.10``.
   * View the results.

   .. image:: pictures/00026-diy-A6.png
      :alt: Ping command and results in Developer Server CLI after route changes.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **Financial Services Server**.
   * Select **Security**.
   * Select **Security groups**.

   .. image:: pictures/00027-diy-A6.png
      :alt: Navigate to Financial Services Server security groups.
      :align: center
      :width: 600px

#. In **FinanceServerSecurityGroup**:

   * Select **Inbound rules**.
   * View the inbound rules.
   * Select **Edit inbound rules**.

   .. image:: pictures/00028-diy-A6.png
      :alt: View and edit inbound rules for Finance server security group.
      :align: center
      :width: 600px

#. In the **Edit Inbound Rules** interface:

   * Select **Add rule**.
   * For **Type**, choose **All ICMP-IPv4**.
   * For **Source**, choose **Custom**.
   * Enter ``192.168.10.32``.
   * Select **Save rules**.

   .. image:: pictures/00029-diy-A6.png
      :alt: Add ICMP rule allowing traffic from specified source IP.
      :align: center
      :width: 600px

#. View **Results after initialization** (updated security group rules).

   .. image:: pictures/00030-diy-A6.png
      :alt: Security group inbound rules showing the new ICMP rule.
      :align: center
      :width: 600px

#. In the **CLI** (Developer Server CLI):

   * Enter ``ping 172.31.0.10``.
   * View the results.

   .. image:: pictures/00031-diy-A6.png
      :alt: Ping command and successful results in Developer Server CLI after security group change.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Enter the Developer instance ID.
   * Enter the Finance instance ID.
   * Then, select **VALIDATE**.

   .. image:: pictures/00032-diy-A6.png
      :alt: DIY interface with fields for instance IDs and validate button.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **Developer Server**.
   * Select **Details**.
   * Copy the **Instance ID**.

   .. image:: pictures/00033-diy-A6.png
      :alt: Developer server details showing instance ID to copy.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **Financial Services Server**.
   * Select **Details**.
   * Copy the **Instance ID**.

   .. image:: pictures/00034-diy-A6.png
      :alt: Financial Services server details showing instance ID to copy.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Paste both Instance IDs into the **VALIDATION FORM**.
   * Select **VALIDATE**.

   .. image:: pictures/00035-diy-A6.png
      :alt: DIY interface with instance IDs pasted in validation form.
      :align: center
      :width: 600px

#. In the **Validation Message** interface:

   * The message “You did it!…” appears.
   * Select **EXIT** to exit.

   .. image:: pictures/00036-diy-A6.png
      :alt: Validation success message.
      :align: center
      :width: 600px

#. In the **City** interface:

   * Select **ASSIGNMENTS**.
   * Select **COLLECT**.

   .. image:: pictures/00037-diy-A6.png
      :alt: City interface showing Assignments and Collect options.
      :align: center
      :width: 600px

#. In the **City** interface:

   * Select **NEXT**.

   .. image:: pictures/00038-diy-A6.png
      :alt: Selecting NEXT after collecting assignment.
      :align: center
      :width: 600px

#. In the **City** interface:

   * Select **COLLECT**.

   .. image:: pictures/00039-diy-A6.png
      :alt: Selecting COLLECT again.
      :align: center
      :width: 600px

#. Congratulations to the player for completing the lab!

   .. image:: pictures/00040-diy-A6.png
      :alt: Congratulations screen.
      :align: center
      :width: 600px
